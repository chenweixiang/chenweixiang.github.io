#!/bin/python3

import argparse


#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------

# Input regular expression string
orig_regexp_str = ""

# Input regular expression priority
orig_regexp_priority = ""

# All elements of input regular expression.
# The regular expression part will updated in loop.
regexp_elements = []

# Attribute of each regular expression part:
# [ 0: index of regexp_elements,
#   1: start value,
#   2: end value,
#   3: current value ]
regexp_attribute = []

# Priority of each regular expression part.
# Index of this list: specify regular expression
# Value of this list: specify priority of each regular expression, for instance: 0, 1, 2
regexp_priority = []

# File name
file_name = ""

# Prefix and suffix string
prefix_str = ""
suffix_str = ""


#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------

# Parse input arguments
def parse_arguments():
    # Parse arguments
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-r", "--regexp", help="Regular expression")
    parser.add_argument("-p", "--priority", help="Priority")
    parser.add_argument("-f", "--file", help="File name")
    parser.add_argument("-x", "--prefix", help="Prefix string")
    parser.add_argument("-y", "--suffix", help="Suffix string")
    args = parser.parse_args()
    
    # -r, --regexp
    global orig_regexp_str
    if args.regexp:
        orig_regexp_str = args.regexp
    
    # -p, --priority
    global orig_regexp_priority
    if args.priority:
        orig_regexp_priority = args.priority
    
    # -f, --file
    global file_name
    if args.file:
        file_name = args.file
    
    # -x, --prefix
    global prefix_str
    if args.prefix:
        prefix_str = args.prefix
    
    # -y, --suffix
    global suffix_str
    if args.suffix:
        suffix_str = args.suffix


# Parse input regular expression string
def parse_regexp_string():
    regexp_element_idx = 0
    start_idx = 0
    
    if len(prefix_str) > 0:
        regexp_elements.append(prefix_str)
        regexp_element_idx += 1
    
    while True:
        left_bracket_idx = orig_regexp_str.find('[', start_idx)
        if left_bracket_idx != -1:
            right_bracket_idx = orig_regexp_str.find(']', left_bracket_idx)
            if right_bracket_idx != -1:
                regexp_elements.append(orig_regexp_str[start_idx:left_bracket_idx])
                regexp_element_idx += 1
                regexp_elements.append(orig_regexp_str[left_bracket_idx:right_bracket_idx+1])
                
                regexp_attribute.append([regexp_element_idx, '', '', ''])
                
                regexp_element_idx += 1
                start_idx = right_bracket_idx + 1
            else:
                print("ERROR: Cannot find right square bracket corresponding to left one at ", left_bracket_idx)
                exit()
        else:
            if start_idx < len(orig_regexp_str):
                regexp_elements.append(orig_regexp_str[start_idx:-1])
            break
    
    if len(suffix_str) > 0:
        regexp_elements.append(suffix_str)


def parse_regexp_attribute():
    for attr in regexp_attribute:
        regexp_idx = attr[0]
        regexp_str = regexp_elements[regexp_idx]
        minus_idx = regexp_str.find('-')
        if minus_idx != -1:
            attr[1] = int(regexp_str[1:minus_idx])
            attr[2] = int(regexp_str[minus_idx+1:-1])
            attr[3] = attr[1]
    print(regexp_attribute)


def parse_regexp_priority():
    global orig_regexp_priority
    global regexp_priority
    if len(orig_regexp_priority) > 0:
        for element in orig_regexp_priority.split(' '):
            regexp_priority.append(int(element))
    else:
        for element in reversed(range(0, len(regexp_attribute))):
            regexp_priority.append(element)
    print(regexp_priority)


def translation_done():
    for attr in regexp_attribute:
        if attr[3] != attr[2]:
            return False
    return True


def update_regexp_attribute():
    step_forward = True
    for idx in regexp_priority:
        if step_forward:
            if regexp_attribute[idx][3] < regexp_attribute[idx][2]:
                regexp_attribute[idx][3] += 1
                step_forward = False
            elif regexp_attribute[idx][3] == regexp_attribute[idx][2]:
                regexp_attribute[idx][3] = regexp_attribute[idx][1]
                step_forward = True
        regexp_elements[regexp_attribute[idx][0]] = str(regexp_attribute[idx][3])


def print_regexp_string():
    file_content = ""
    while True:
        if translation_done():
            break
        update_regexp_attribute()
        if len(file_name) > 0:
            file_content += ''.join(regexp_elements) + '\n'
        else:
            print(''.join(regexp_elements))
    if len(file_name) > 0:
        with open(file_name, 'w') as f:
            f.write(file_content)
            f.close()


def translate_reg_expression():
    parse_regexp_string()
    parse_regexp_attribute()
    parse_regexp_priority()
    print_regexp_string()


# Entry point
if __name__ == "__main__":
    parse_arguments()
    translate_reg_expression()


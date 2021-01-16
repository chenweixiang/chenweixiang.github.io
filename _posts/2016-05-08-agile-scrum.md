---
layout: post
title: "Agile/Scrum/SAFe"
tag: Methodology
toc: true
---

This article introduces the **Agile software development** and one of its method **Scrum**. Besides, this article also introduces the **SAFe Scaled Agile**.

<!--more-->

# Agile Software Development

**Agile software development** (敏捷软件开发) is a set of principles for software development in which requirements and solutions evolve through collaboration between *self-organizing, cross-functional teams*. It promotes adaptive planning, evolutionary development, early delivery, and continuous improvement, and it encourages rapid and flexible response to change. ***Agile itself has never defined any specific methods to achieve this, but many have grown up as a result and have been recognized as being Agile***.

## Agile Manifesto

In **February 2001**, 17 software developers met at the *Snowbird resort in Utah* to discuss **lightweight development methods**. They published the ***Manifesto for Agile Software Development***, in which they said that by *uncovering better ways of developing software by doing it and helping others do it*, they have come to value:

* ***Individuals and interactions*** over *Processes and tools* (个体和互动 高于 流程和工具)
* ***Working software*** over *Comprehensive documentation* (可工作的软件 高于 详尽的文档)
* ***Customer collaboration*** over *Contract negotiation* (客户的合作 高于 合同谈判)
* ***Responding to change*** over *Following a plan* (相应变化 高于 遵循计划)

where,

* ***Individuals and interactions***: self-organization and motivation are important, as are interactions like co-location and pair programming.
* ***Working software***: working software is more useful and welcome than just presenting documents to clients in meetings.
* ***Customer collaboration***: requirements cannot be fully collected at the beginning of the software development cycle, therefore continuous customer or stakeholder involvement is very important.
* ***Responding to change***: agile methods are focused on quick responses to change and continuous development.

Some of the authors formed the [Agile Alliance](https://www.agilealliance.org/), a non-profit organization that promotes software development according to the manifesto's values and principles. Introducing the manifesto on behalf of the [Agile Alliance](https://www.agilealliance.org/), *Jim Highsmith* said:

*The Agile movement is not anti-methodology, in fact many of us want to restore credibility to the word methodology. We want to restore a balance. We embrace modeling, but not in order to file some diagram in a dusty corporate repository. We embrace documentation, but not hundreds of pages of never-maintained and rarely-used tomes. We plan, but recognize the limits of planning in a turbulent environment. Those who would brand proponents of XP or SCRUM or any of the other Agile Methodologies as "hackers" are ignorant of both the methodologies and the original definition of the term hacker.*

## Agile Principles

The Agile Manifesto is based on twelve principles:

1. Customer satisfaction by early and continuous delivery of valuable software
2. Welcome changing requirements, even in late development
3. Working software is delivered frequently (weeks rather than months)
4. Close, daily cooperation between business people and developers
5. Projects are built around motivated individuals, who should be trusted
6. Face-to-face conversation is the best form of communication (co-location)
7. Working software is the principal measure of progress
8. Sustainable development, able to maintain a constant pace
9. Continuous attention to technical excellence and good design
10. Simplicity - the art of maximizing the amount of work not done - is essential
11. Best architectures, requirements, and designs emerge from self-organizing teams
12. Regularly, the team reflects on how to become more effective, and adjusts accordingly

## Agile Methods

Popular Agile software development methods and/or process frameworks include (but are not limited to):

* Adaptive software development (ASD) / 自适应软件开发
* Agile modeling (AM) / 敏捷建模
* Agile Unified Process (AUP) / 敏捷统一过程
* Business analyst designer method (BADM) / 业务分析师设计方法
* Crystal Clear Methods / 水晶方法
* Disciplined agile delivery
* Dynamic systems development method (DSDM) / 动态系统开发方法
* Extreme programming (XP) / 极限编程
* Feature-driven development (FDD) / 特性驱动开发
* Lean software development / 精益软件开发
* **Kanban**
* **Scrum**
* **Scrumban** (hybrids of **Scrum** and **Kanban**)

## Agile Practices

Agile development is supported by a bundle of concrete practices, covering areas like requirements, design, modelling, coding, testing, project management, process, quality, etc. Some notable agile practices include:

* Acceptance test-driven development (ATDD)
* Agile modeling
* Backlogs (Product and Sprint)
* Behavior-driven development (BDD)
* **Cross-functional team (XFT)**
* Continuous integration (CI)
* Domain-driven design (DDD)
* Information radiators (scrum board, task board, visual management board, burndown chart)
* Iterative and incremental development (IID)
* Pair programming
* Planning poker
* Refactoring
* Scrum events (sprint planning, daily scrum, sprint review and retrospective)
* Test-driven development (TDD)
* Agile testing
* Timeboxing
* User story
* Story-driven modeling
* Retrospective
* Velocity tracking
* User Story Mapping

The [Agile Alliance](https://www.agilealliance.org/) has provided a comprehensive online collection with a map guide to the applying agile practices.

# Scrum

According to the **Scrum Guide** from [Scrum.org](https://www.scrum.org/resources/scrum-guide):

* [Scrum Guide (English)](/docs/Scrum_Guide_US_2017.pdf)
* [Scrum Guide (Chinese)](/docs/Scrum_Guide_Chinese_Simplified_2017.pdf)

Scrum is an iterative and incremental *Agile software development* framework for managing product development. It defines **a flexible, holistic product development strategy where a development team works as a unit to reach a common goal**, challenges assumptions of the *traditional, sequential approach* to product development, and enables teams to self-organize by encouraging physical co-location or close online collaboration of all team members, as well as daily face-to-face communication among all team members and disciplines in the project.

A key principle of scrum is its recognition that during production processes, the customers can change their minds about what they want and need (often called *requirements volatility*), and that unpredicted challenges cannot be easily addressed in a traditional predictive or planned manner. As such, scrum adopts an empirical approach - accepting that the problem cannot be fully understood or defined, focusing instead on maximizing the team's ability to deliver quickly, to respond to emerging requirements and to adapt to evolving technologies and changes in market conditions.

## Roles

There are three core roles in the scrum framework. These core roles are those committed to the project in the scrum process:

* **Product Owner**

    The *product owner* represents the stakeholders and is the **voice of the customer**, who is accountable for ensuring that the team delivers value to the business. The *product owner* writes (or has the team write) customer-centric items (typically user stories), ranks and prioritizes them, and adds them to the **product backlog**. Scrum teams should have one *product owner*, this role should not be combined with that of the *scrum master*. The *product owner* spends most of the time on the business side of the project, and should never interfere or interact with team members on the technical aspects of the development task. This role is equivalent to the customer representative role in some other agile frameworks.

* **Development Team**

    The *development team* is responsible for delivering Potentially Shippable Increments (PSIs) of product at the end of each *sprint* (the sprint goal). A team is made up of **3 - 9 individuals** who do the actual work (analyse, design, develop, test, technical communication, document, etc.). Development teams are *cross-functional*, with all of the skills as a team necessary to create a product increment. The *development team* in scrum is *self-organizing*, even though there may be some level of interface with Project Management Offices (PMOs).

* **Scrum Master**

    Scrum is facilitated by a *scrum master*, who is accountable for removing impediments to the ability of the team to deliver the product goals and deliverables. The *scrum master* is not a traditional team lead or project manager, but acts as a buffer between the team and any distracting influences. The *scrum master* ensures that the scrum process is used as intended. The *scrum master* helps ensure the team follows the agreed scrum processes, often facilitates key sessions, and encourages the team to improve. The role has also been referred to as a *team facilitator* or *servant-leader* to reinforce these dual perspectives.

    The core responsibilities of a scrum master include (but are not limited to):

    * Helping the *product owner* maintain the *product backlog* in a way that ensures the needed work is well understood so the team can continually make forward progress
    * Helping the team to determine the *definition of done* for the product, with input from key stakeholders
    * Coaching the team, within the scrum principles, in order to deliver high-quality features for its product
    * Promoting self-organization within the team
    * Helping the scrum team to avoid or remove impediments to its progress, whether internal or external to the team
    * Facilitating team events to ensure regular progress
    * Educating key stakeholders in the product on scrum principles
    <p/>

    One of the ways the *scrum master* role differs from a *project manager* is that the latter may have people management responsibilities and the *scrum master* does not. Scrum does not formally recognise the role of *project manager*, as traditional command and control tendencies would cause difficulties.

	[What is a scrum master?](/docs/What_is_a_scrum_master.pdf)

## Workflow

A *sprint* (or *iteration*) is the basic unit of development in scrum. The *sprint* is a timeboxed effort; that is, it is restricted to a specific duration. The duration is fixed in advance for each sprint and is normally *between one week and one month*, with two weeks being the most common.

Each sprint starts with a *sprint planning event* that aims to define a *sprint backlog*, identify the work for the sprint, and make an estimated commitment for the sprint goal. Each sprint ends with a *sprint review* and *sprint retrospective*, that reviews progress to show to stakeholders and identify lessons and improvements for the next sprints.

Scrum emphasizes working product at the end of the sprint that is really done. In the case of software, this likely includes that the software has been integrated, fully tested, end-user documented, and is potentially shippable.

![scrum_process](/assets/scrum_process.jpg)
![scrum_in_a_nutshell](/assets/scrum_in_a_nutshell.png)

* **Sprint Planning Meeting**

    At the beginning of a sprint, the team holds a *sprint planning event* that:

    * Communicates the scope of work likely during that sprint
    * Selects *product backlog* items that likely can be done
    * Prepares the *sprint backlog* that details the work needed to finish the selected *product backlog items*, with the entire team
    * Sets a four-hour time planning event limit for a two-week sprint:
        * During the first half, the whole team (*development team*, *scrum master*, and *product owner*) agree what *product backlog items* to consider for that sprint
        * During the second half, the *development team* decomposes the work (tasks) required to deliver those backlog items, resulting in the *sprint backlog*
    <p/>

    Once the *development team* prepares the *sprint backlog*, they commit (usually by voting) to deliver tasks within the sprint.

* **Daily Scrum Meeting**

    Each day during a sprint, the team holds a *daily scrum* (or *stand-up*) with specific guidelines:

    * All members of the *development team* come prepared. The daily scrum...
        * ...starts precisely on time even if some development team members are missing
        * ...should happen at the same time and place every day
        * ...is limited (timeboxed) to *fifteen minutes*
    * Anyone is welcome, though normally only scrum team roles contribute.
    * During the *daily scrum*, each team-member answers three questions:
        * What did I do yesterday that helped the development team meet the sprint goal?
        * What will I do today to help the development team meet the sprint goal?
        * Do I see any impediment that prevents me or the development team from meeting the sprint goal?
    <p/>

    Any impediment (stumbling block, risk or issue) identified in the *daily scrum* should be captured by the *scrum master* and displayed on the team's scrum board, with an agreed person designated to working toward a resolution (outside of the daily scrum). No detailed discussions should happen during the daily scrum.

* **Review and Retrospective Meeting**

    At the end of a sprint, the team holds two events: the *sprint review* and the *sprint retrospective*.

    At the ***sprint review***, the team:

    * Reviews the work that was completed and the planned work that was not completed
    * Presents the completed work to the stakeholders (a.k.a. the demo)
    <p/>

    Guidelines for ***sprint reviews***:

    * Incomplete work cannot be demonstrated
    * The recommended duration is two hours for a two-week sprint
    <p/>

    At the ***sprint retrospective***, the team:

    * Reflects on the past sprint
    * Identifies and agrees on continuous process improvement actions
    <p/>

    Guidelines for ***sprint retrospectives***:

    * Two main questions are asked in the *sprint retrospective*:
        * What went well during the sprint?
        * What could be improved in the next sprint?
    * The recommended duration is one-and-a-half hours for a two-week sprint
    * This event is facilitated by the *scrum master*
    <p/>

# SAFe

The [Scaled Agile Framework (SAFe)](http://www.scaledagileframework.com) is a freely revealed knowledge base of proven, integrated patterns for enterprise-scale Lean-Agile development. It is scalable and modular, allowing each organization to apply it in a way that provides better business outcomes and happier, more engaged employees.

SAFe synchronizes alignment, collaboration, and delivery for large numbers of Agile teams. It supports both software and systems development, from the modest scale of well under 100 practitioners to the largest software solutions and complex cyber-physical systems, systems that require thousands of people to create and maintain. SAFe was developed in the field, based on helping customers solve their most challenging scaling problems. It leverages three primary bodies of knowledge: Agile development, Lean product development, and systems thinking.

![SAFe-4.0-3-level](/assets/SAFe-4.0-3-level.png)

![SAFe-4.0-4-level](/assets/SAFe-4.0-4-level.png)

# References

* [Agile Alliance](https://www.agilealliance.org/)
* [Agile Software Development wikipedia](https://en.wikipedia.org/wiki/Agile_software_development)
* [Thinking in Agile](/docs/Thinking_in_Agile.pdf)

* [Scrum wikipedia](http://en.wikipedia.org/wiki/Scrum_(software_development))
* [Scrum](https://www.scrum.org/)
* [Scrum Cheat Sheet](/docs/Scrum_Cheat_Sheet.pdf)

* [SAFe Scaled Agile](http://www.scaledagileframework.com/)
* [SAFe Implementation Roadmap](/docs/SAFe_Implementation_Roadmap.pdf)


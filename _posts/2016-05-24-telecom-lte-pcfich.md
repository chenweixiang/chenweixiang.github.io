---
layout: post
title: "LTE: Physical Control Format Indicator CHannel (PCFICH)"
tag: Telecommunication
toc: true
---

This article introduces the Physical Control Format Indicator CHannel (PCFICH).

<!--more-->

The physical control format indicator channel (PCFICH) carries information about the number of OFDM symbols used for transmission of PDCCHs in a subframe. The set of OFDM symbols possible to use for PDCCH in a subframe is given by **TS 36.211 Table 6.7-1**.

The following figure shows the process of CFI:

![R8_TS36.211_S6.7_PCFICH](/assets/R8_TS36.211_S6.7_PCFICH.png)

# How to determine CFI value

Refer to **TS 36.212 S5.3.4** and **TS 36.211 Table 6.7-1**.

# Channel Coding

Refer to **TS 36.212 S5.3.4**.

# Scrambling

Refer to **TS 36.211 S6.7.1**

# Modulation

Refer to **TS 36.211 S6.7.2**

# Layer Mapping and Precoding

Refer to **TS 36.211 S6.7.3**

# Mapping to REs

According to **TS 36.211 S6.7.4**, the CFI is mapped to the four resource-element groups in the **first OFDM symbol** in a downlink subframe with the representative resource-element.

Refer to the following sheets in *R8_TS36.XXX_LTE_PHY_Parameters_v2.xlsx*:

* *36.211 S6.7.4 PCFICH REs*
* *LTE-FDD, DL, NCP, 1 AP, All BW*
* *LTE-FDD, DL, NCP, 2 AP, All BW*
* *LTE-FDD, DL, NCP, 4 AP, All BW*
* *LTE-FDD, DL, NCP, 4 AP, 1.4MHz*
* *LTE-FDD, DL, NCP, 4 AP, 3MHz*
* *LTE-FDD, DL, NCP, 4 AP, 5MHz*
* *LTE-FDD, DL, NCP, 4 AP, 15MHz*
* *LTE-FDD, DL, NCP, 4 AP, 20MHz*
* *LTE-FDD, DL, ECP, 1 AP, All BW*
* *LTE-FDD, DL, ECP, 2 AP, All BW*
* *LTE-FDD, DL, ECP, 4 AP, All BW*
* *LTE-TDD, DL, NCP, 1 AP, All BW*
* *LTE-TDD, DL, NCP, 2 AP, All BW*
* *LTE-TDD, DL, NCP, 4 AP, All BW*
* *LTE-TDD, DL, ECP, 1 AP, All BW*
* *LTE-TDD, DL, ECP, 2 AP, All BW*
* *LTE-TDD, DL, ECP, 4 AP, All BW*

# References

**3GPP Specs**

TS 36.212 S5.3.4
TS 36.211 S6.7

**ShareTechnote**

[http://www.sharetechnote.com/](http://www.sharetechnote.com/)
[http://www.sharetechnote.com/html/Handbook_LTE_CFI.html](http://www.sharetechnote.com/html/Handbook_LTE_CFI.html)
[http://www.sharetechnote.com/html/Handbook_LTE_PCFICH.html](http://www.sharetechnote.com/html/Handbook_LTE_PCFICH.html)
[http://www.sharetechnote.com/html/lte_toolbox/Matlab_LteToolbox_PCFICH.html](http://www.sharetechnote.com/html/lte_toolbox/Matlab_LteToolbox_PCFICH.html)

**3GLTEInfo**

[http://www.3glteinfo.com/](http://www.3glteinfo.com/)

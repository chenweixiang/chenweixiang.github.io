---
layout: post
title: "LTE: Physical Hybrid ARQ Indicator CHannel (PHICH)"
tag: Telecom
toc: true
---

This article introduces the Physical Hybrid ARQ Indicator CHannel (PHICH).

<!--more-->

# PHICH Groups and Orthogonal Sequences

The PHICH carries the hybrid-ARQ ACK/NAK. Multiple PHICHs mapped to the same set of resource elements constitute a **PHICH group**, where PHICHs within the same PHICH group are separated through different **orthogonal sequences**.

![R8_TS36.211_S6.9_PHICH](/assets/R8_TS36.211_S6.9_PHICH.png)

A PHICH resource is identified by the index pair:

$$(n^{group}_{PHICH}, n^{seq}_{PHICH})$$

where,

* $$n^{group}_{PHICH}$$ and $$n^{seq}_{PHICH}$$ are given by **TS 36.213 S9.1.2**;
* $$n^{group}_{PHICH}$$ is the PHICH group number, $$n^{group}_{PHICH} \in [0, N^{group}_{PHICH}-1]$$, where $$N^{group}_{PHICH}$$ is calculated in **TS 36.211 S6.9**;
* $$n^{seq}_{PHICH}$$ is the orthogonal sequence index within the group, refer to **TS 36.211 Table 6.9.1-2**.

# Channel Coding

Refer to **TS 36.212 S5.3.5**.

# Modulation

Modulation scheme for PHICH is **BPSK**, refer to **TS 36.211 S6.9.1**.

# Resource Group Alignment, Layer Mapping and Precoding

Refer to **TS 36.211 S6.9.2**.

# Mapping to REs

Refer to the following sheets in **R8_TS36.XXX_LTE_PHY_Parameters_v2.xlsx**:

* LTE-FDD, DL, NCP, 1 AP, All BW
* LTE-FDD, DL, NCP, 2 AP, All BW
* LTE-FDD, DL, NCP, 4 AP, All BW
* LTE-FDD, DL, NCP, 4 AP, 1.4MHz
* LTE-FDD, DL, NCP, 4 AP, 3MHz
* LTE-FDD, DL, NCP, 4 AP, 5MHz
* LTE-FDD, DL, NCP, 4 AP, 15MHz
* LTE-FDD, DL, NCP, 4 AP, 20MHz
* LTE-FDD, DL, ECP, 1 AP, All BW
* LTE-FDD, DL, ECP, 2 AP, All BW
* LTE-FDD, DL, ECP, 4 AP, All BW
* LTE-TDD, DL, NCP, 1 AP, All BW
* LTE-TDD, DL, NCP, 2 AP, All BW
* LTE-TDD, DL, NCP, 4 AP, All BW
* LTE-TDD, DL, ECP, 1 AP, All BW
* LTE-TDD, DL, ECP, 2 AP, All BW
* LTE-TDD, DL, ECP, 4 AP, All BW

# References

* TS 36.213 E-UTRA - Physical layer procedures, section 9.1.2
* TS 36.212 E-UTRA - Multiplexing and channel coding, section 5.3.5
* TS 36.211 E-UTRA - Physical Channels and Modulation, section 6.9
* [ShareTechnote](http://www.sharetechnote.com/)
* [LTE Dictionary on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE.html)
* [PHICH/PHICH Group on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_PHICH_PHICHGroup.html)
* [MatLab Toolbox for PHICH on ShareTechnote](http://www.sharetechnote.com/html/lte_toolbox/Matlab_LteToolbox_PHICH.html)
* [3GLTEinfo](http://www.3glteinfo.com/)

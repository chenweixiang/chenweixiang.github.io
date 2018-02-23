---
layout: post
title: "LTE: PSS, SSS and PBCH"
tag: Telecom
toc: true
---

This article introduces the Physical-layer Cell Identity (PCI), Primary Synchronization Signal (PSS), Secondary Synchronization Signal (SSS) and Physical Broadcast Channel (PBCH).

<!--more-->

# Physical-layer Cell Identity (PCI)

There are **504** unique physical-layer cell identities. A *physical-layer cell identity* is defined by:

$$N^{cell}_{ID} = 3N^{(1)}_{ID} + N^{(2)}_{ID}$$

where,

* $$N^{(1)}_{ID} \in [0, 167]$$ is *physical-layer cell-identity group* and transmitted in Secondary Synchronization Signal (SSS);
* $$N^{(2)}_{ID} \in [0, 2]$$ is *physical-layer identity* within the *physical-layer cell-identity group* and transmitted in Primary Synchronization Signal (PSS).

The *physical-layer cell identity* is only used in physical layer, which is different with the *cell identity* transmitted in SIB1, which is used to unambiguously identify a cell within a PLMN.

```
SystemInformationBlockType1
-> cellAccessRelatedInfo
   -> cellIdentity
```

# Primary Synchronization Signal (PSS)

## Generation of PSS Sequence

According to **TS 36.211 S6.11.1.1**, the sequence used for PSS is generated from a frequency-domain *Zadoff-Chu sequence* according to

$$d_u(n) = \begin{cases} e^{ -j \frac { {\pi} un(n+1)} {63} } & \text {n=0,1,..30} \\ e^{ -j \frac { {\pi} u(n+1)(n+2)} {63} } & \text {n=31,32,..61} \end{cases}$$

where,

* the Zadoff-Chu root sequence index ***u*** is given by **TS 36.211 Table 6.11.1.1-1** according to *physical-layer identity* $$N^{(2)}_{ID}$$.

## Mapping to REs

The sequence $$d(n)$$ shall be mapped to the resource elements according to

$$a_{k,l} = d(n), n = 0,1,..61$$

where,

* frequency-domain index is $$k = n - 31 + \frac { N^{DL}_{RB} N^{RB}_{sc} } {2}$$
* time-domain index *l* is
    * for frame structure type 1, the **last OFDM symbol** in **slots 0 and 10**;
    * for frame structure type 2, the **third OFDM symbol** in **subframes 1 and 6**.
<p/>

The following figure shows the PSS mapped resource elements in time-domain and frequency-domain respectively:

![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p1](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p1.png)

![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p2](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p2.png)

Note that the PSS sequences in every radio frame are the same, so the UE just can determine the slot timing when synchronization to eNB.

# Secondary Synchronization Signal (SSS)

Refer to [SSS Detection Method for Initial Cell Search in 3GPP LTE FDD/TDD Dual Mode Receiver](/docs/SSS_Detection_Method_for_Initial_Cell_Search_in_3GPP_LTE_FDD-TDD_Dual_Mode_Receiver.pdf)

## Generation of SSS Sequence

According to **TS 36.211 S6.11.2.1**, the sequence used for SSS is generated as shown in the following figure:

![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p4](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p4.png)

## Mapping to REs

The sequence $$d(n)$$ shall be mapped to the resource elements according to

$$a_{k,l} = d(n), n = 0,1,..61$$

where,

* frequency-domain index is $$k = n - 31 + \frac { N^{DL}_{RB} N^{RB}_{sc} } {2}$$
* time-domain index is $$l = \begin{cases} N^{DL}_{symb}-2, & \text {in slots 0 and 10 for frame structure type1} \\ N^{DL}_{symb}-1, & \text {in slots 1 and 11 for frame structure type 2} \end{cases}$$

The following figure shows the SSS mapped resource elements in time-domain and frequency-domain respectively:

![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p1](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p1.png)
![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p3](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p3.png)

Note that the SSS sequences in subframe #0 and #5 are different, so the UE can determine the frame timing when synchronization to eNB.

# Physical Broadcast Channel (PBCH)

The downlink Physical Broadcast Channel (PBCH) is used to transmit the Master Information Block (MIB) from logical channel BCH.

![R8_TS36.211_S6.6_PBCH](/assets/R8_TS36.211_S6.6_PBCH.png)

## MIB from RRC

According to **TS 36.331 S6.2.2**, the MIB contains the following **24 bits** system information:

```
MasterInformationBlock ::=  SEQUENCE {
    dl-Bandwidth        ENUMERATED {n6, n15, n25, n50, n75, n100},  // 3 bits
    phich-Config        PHICH-Config,                               // 3 bits
    systemFrameNumber   BIT STRING (SIZE (8)),                      // 8 bits
    spare               BIT STRING (SIZE (10))                      // 10 bits
}

PHICH-Config ::= SEQUENCE {
    phich-Duration      ENUMERATED {normal, extended},
    phich-Resource      ENUMERATED {oneSixth, half, one, two}
}
```

**Q: Why is it necessary to have $$N_g$$ in the MIB? Why does not include it in the MIB?**

A: The reason that the UE needs to know the PHICH configuration at the very beginning of the system acquisition process is because of the "chicken-and-egg" problem. On one hand, the UE needs to decode PDCCH to know where to find SIB on PDSCH. On the other hand, PDCCH and PHICH and PCFICH share the resources in the control region of a subframe and the set of the available resources for PDCCH depends on the PHICH configuration (PCFICH resources are fixed and known).

**Q: The System Frame Number (SFN) in LTE has 10 bit length, but why is it only 8 bits in *MIB->systemFrameNumber*?**

A: In LTE, the SFN has 10 bit length, and the MSB 8 bits are transmitted in *MIB->systemFrameNumber*. The LSB 2 bits are blind-detected by UE according to the position of radio frame in 40 ms PBCH window, that's, the LSB 2 bits are 00, 01, 02, 03 for the radio frame corresponding to the first, second, third and fourth radio frame in 40 ms PBCH window, respectively. The blind-detected is based on the scrambling sequence $$c(i)$$ in **TS 36.211 S6.6.1**.

## BCCH Process in RLC

A TM RLC entity can be configured to deliver/receive RLC PDUs through the BCCH logical channel. Refer to **TS 36.322 S4.2.1.1.1**.

## BCH Process in MAC

Refer to **TS 36.321 S4.2.1**.

## PBCH Process in PHY

According to **TS 36.212 S5.3.1**, the following steps are processed in PHY about the PBCH:

* **Add CRC to the transport block**

    **16 bits** CRC is appended to transport block, so the output of this step is **40 bits** sequence.

    Note that the number of antenna ports is transmitted in CRC part of BCH transport block, refer to **TS 36.212 Table 5.3.1.1-1**. That's, UE can blind-detect the number of antenna ports by decoding BCH transport block.

* **Channel coding**

    The channel coding scheme is **tail biting convolutional coding** with **1/3 coding rate**, so the output of this step is **120 bits** sequence.

* **Rate matching**

    According to **TS 36.211 S6.6.1**, the number of bits transmitted on the physical broadcast channel is **1920** for normal cyclic prefix (NCP) and **1728** for extended cyclic prefix (ECP), so the output of this step is **1920 and 1728 bits** sequence for NCP and ECP respectively.

* **Scrambling**

    According to **TS 36.211 S6.6.1**, the scrambling sequence shall be initialised with $$c_{init} = N^{cell}_ID$$ in each radio frame fulfilling $$n_f % 4 == 0$$. That's why UE can blind-detect the LSB 2 bits of system frame number. Then, UE gets the system frame number by combining it with the MSB 8 bits from *MIB->systemFrameNumber*.

* **Modulation**

    **QPSK**. The output of this step is **960 bits** sequence for NCP, and **864 bits** sequence for ECP.

* **Layer Mapping and Precoding**

    Refer to **TS 36.211 S6.6.3**.

* **Mapping to REs**

    The block of complex-valued symbols for each antenna port is transmitted during **4 consecutive radio frames** starting in each radio frame fulfilling $$n_f mod 4 == 0$$. That's why it takes 4 radio frames to read MIB.

    The following figure shows the PBCH mapped resource elements in time-domain and frequency-domain respectively:

    ![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p1](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p1.png)
    ![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p5](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p5.png)

# Synchronisation Procedure

The following figure shows the synchronisation procedure when UE try to access to LTE:

![R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p6](/assets/R8_TS36.211_S6.11_PSS_SSS_S6.6_PBCH_v2_p6.png)

* **PSS detection**

    UE gets the following information when detection PSS:

    * Synchronisation to slot timing
    * Physical-layer identity $$N^{(2)}_{ID}$$
    <p/>

* **SSS detection**

    UE gets the following information when detection SSS:

    * Synchronisation to radio frame timing.
    * Physical-layer cell-identity group $$N^{(1)}_{ID}$$. Then, UE gets the physical-layer cell identity by the formula in section [Physical-layer Cell Identity (PCI)](#physical-layer-cell-identity-pci).
    * Cyclic prefix length and system type FDD/TDD according to the position between PSS and SSS.
    <p/>

* **PBCH decoding**

    UE gets the following information when detection SSS:

    * Number of antenna ports according to CRC of MIB transport block
    * System information contained in MIB, refer to [MIB from RRC](#mib-from-rrc).

# References

* TS 36.211 E-UTRA - Physical Channels and Modulation
* [ShareTechnote](http://www.sharetechnote.com/)
* [PBCH (Physical Broadcast Channel) on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_PBCH.html)
* [PSS (Primary Synchronization Channel) on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_PSS.html)
* [SSS (Secondary Synchronization Channel) on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_SSS.html)
* [3GLTEinfo](http://www.3glteinfo.com/)
* [SSS Detection Method for Initial Cell Search in 3GPP LTE FDD/TDD Dual Mode Receiver](/docs/SSS_Detection_Method_for_Initial_Cell_Search_in_3GPP_LTE_FDD-TDD_Dual_Mode_Receiver.pdf)

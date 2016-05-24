---
layout: post
title: "LTE: Downlink Reference Signals"
tag: Telecommunication
toc: true
---

This article introduce the Reference Signals on downlink.

<!--more-->

There are three kind of reference signals on downlink:

* [Cell-specific Reference Signal](#cell-specific-reference-signal)
* [MBSFN Reference Signal](#mbsfn-reference-signal)
* [UE-specific Reference Signal](#ue-specific-reference-signal)

# Cell-specific Reference Signal

Cell-specific reference signals shall be transmitted in all downlink subframes in a cell supporting non-MBSFN transmission. In case the subframe is used for transmission with MBSFN, only the first two OFDM symbols in a subframe can be used for transmission of cell-specific reference symbols.

Cell-specific reference signals are transmitted on one or several of antenna ports 0 to 3.

Cell-specific reference signals are defined for $$\delta f = 15 kHz$$ only.

## Sequence Generation

Refer to **TS 36.211 S6.10.1.1**.

## Mapping to REs

In time domain, the location of cell-specific reference signals is fixed, that's on symbol 0 and $$N^{DL}_{symb}-3$$ for antenna ports 0 and 1, symbol 1 for antenna ports 2 and 3.

In frequency domain, the location of cell-specific reference signals is distributed accross the system bandwidth and related to physical-layer cell identity $$N^{cell}_{ID}$$.

The following figure shows the cell-specific reference signals of LTE-FDD with 3MHz system bandwidth, normal CP and antenna port 0:
![R8_LTE-FDD_DL_Cell_Specific_RS_3MHz_NCP_1AP](/assets/R8_LTE-FDD_DL_Cell_Specific_RS_3MHz_NCP_1AP.png)

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

# MBSFN Reference Signal

MBSFN reference signals shall only be transmitted in subframes allocated for MBSFN transmissions. MBSFN reference signals are transmitted on antenna port 4.

MBSFN reference signals are defined for extended cyclic prefix only.

## Sequence Generation

Refer to **TS 36.211 S6.10.2.1**.

## Mapping to REs

Refer to **TS 36.211 S6.10.2.2**.

# UE-specific Reference Signal

## RRC Configurations

The following configuration from TS 36.331 points to one of Transmission modes defined in TS 36.213 S7.1.

```
AntennaInfoDedicated
-> transmissionMode
```

The following configuration from TS 36.331 defines whether the UE supports PDSCH transmission mode 7 for FDD, refer to TS 36.306 S4.3.4.2.

```
UE-EUTRA-Capability
-> phyLayerParameters
   -> ue-SpecificRefSigsSupported
```

## Sequence Generation

Refer to **TS 36.211 S6.10.3.1**.

## Mapping to REs

Refer to **TS 36.211 S6.10.3.2**.

# References

**3GPP Specs**

TS 36.211 S6.10

**ShareTechnote**

[http://www.sharetechnote.com/](http://www.sharetechnote.com/)
[http://www.sharetechnote.com/html/Handbook_LTE_Reference_Signal_Downlink.html](http://www.sharetechnote.com/html/Handbook_LTE_Reference_Signal_Downlink.html)
[http://www.sharetechnote.com/html/FrameStructure_DL.html#RS](http://www.sharetechnote.com/html/FrameStructure_DL.html#RS)
[http://www.sharetechnote.com/html/lte_toolbox/Matlab_LteToolbox_CellRS.html](http://www.sharetechnote.com/html/lte_toolbox/Matlab_LteToolbox_CellRS.html)

**3GLTEInfo**

[http://www.3glteinfo.com/](http://www.3glteinfo.com/)

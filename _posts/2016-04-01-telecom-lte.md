---
layout: post
title: "Telecom: LTE/LTE-Advanced"
tags: [Telecommunication]
toc: true
---

This article introduce the LTE/LTE-Advanced defined by 3GPP.

<!--more-->

# History

Although marketed as a 4G wireless service, **LTE** (as specified in the 3GPP Release 8 and 9 document series) does not satisfy the technical requirements the 3GPP consortium has adopted for its new **LTE-Advanced** standard. The requirements were originally set forth by the ITU-R organization in its **IMT Advanced** specification. However, due to marketing pressures and the significant advancements that WiMAX, Evolved High Speed Packet Access (HSPA+) and LTE bring to the original 3G technologies, ITU later decided that LTE together with the aforementioned technologies can be called 4G technologies. The LTE Advanced standard formally satisfies the ITU-R requirements to be considered IMT-Advanced. To differentiate LTE Advanced and WiMAX-Advanced from current 4G technologies, ITU has defined them as **True 4G**.

# Standards

ITU Recommendations related to LTE/LTE-Advanced are introduced in <a href="{{ site.base-url }}/2016/03/13/telecom-itu-recommendations.html#imt-advanced-4g">IMT-Advanced (4G)</a>.

LTE/LTE-Advanced related Technical Specifications (TS) and Technical Reports (TR) are:

* **TD RP-040461 Proposed Study Item on Evolved UTRA and UTRAN** => 发起LTE可行性研究项目的决议 (2004.12)
* **REV-090022 3GPP IMT-Advanced Evaluation Workshop Other considerations**
* **2009_10_3GPP_IMT Proposal for Candidate Radio Interface Technologies for IMT-Advanced Based on LTE Release 10 and Beyond (LTE‐Advanced)**
* **TR 25.913-800 Requirements for E-UTRA and E-UTRAN** => LTE系统需求报告
* **TR 25.913-900 Requirements for Evolved UTRA (E-UTRA) and Evolved UTRAN (E-UTRAN)** => LTE系统需求报告
* **TR 36.913-801 Requirements for further advancements for E-UTRA (LTE-Advanced)** => LTE-Advanced系统需求报告
* **TR 36.913-a00 Requirements for further advancements for E-UTRA (LTE-Advanced)** => LTE-Advanced系统需求报告
* **TR 25.912-800 Feasibility study for evolved UTRA and UTRAN** => LTE可行性研究
* **TR 36.912-a00 Feasibility study for Further Advancements for E-UTRA (LTE-Advanced)** => LTE-Advanced可行性研究
* **TR 25.813-710 E-UTRA and E-UTRAN - Radio interface protocol aspects** => LTE无线接口协议
* **TR 25.814-710 Physical layer aspects for E-UTRA** => LTE物理层
* **TR 36.814-900 Further advancements for E-UTRA physical layer aspects** => LTE-Advanced物理层
* **TR 36.815-910 Further advancements for E-UTRA - LTE-Advanced feasibility studies in RAN WG4**
* **TS 22.278-8a0 Service requirements for the Evolved Packet System (EPS)** => EPS需求报告
* **TS 36.300-8c0 E-UTRA Overall description – Stage 2** => E-UTRA整体描述

Specifications: **TS 36.xxx**

# Requirements

The objective of Evolved UTRA and UTRAN is to develop a framework for the evolution of the 3GPP radio-access technology towards a **high-data-rate**, **low-latency** and **packet-optimized** radio-access technology.

The LTE/LTE-Advanced requirements are defined in **TR 25.913-800 Requirements for E-UTRA and E-UTRAN**:

* **Peak data rate**

    **Configuration**: 1 transmit antenna and 2 receive antennas at UE

    **Downlink**: instantaneous downlink peak data rate of **100Mb/s** within a **20 MHz** downlink spectrum allocation (5 bps/Hz)

    **Uplink**: instantaneous uplink peak data rate of **50Mb/s** (2.5 bps/Hz) within a **20MHz** uplink spectrum allocation.

* **C-plane latency**

    Transition time (excluding downlink paging delay and NAS signalling delay) of less than **100 ms** from a camped-state (such as Release 6 Idle Mode) to an active state (such as Release 6 CELL_DCH).

    Transition time (excluding DRX interval) of less than **50 ms** between a dormant state (such as Release 6 CELL_PCH) and an active state (such as Release 6 CELL_DCH).

* **C-plane capacity**

    At least **200 users per cell** should be supported in the active state for spectrum allocations up to **5 MHz**, and at least **400 users** for higher spectrum allocation.

* **U-plane latency**

    Less than **5 ms** in unload condition (i.e. single user with single data stream) for small IP packet.

* **User throughput**

    **Downlink**: User throughput per MHz, 2 to 3 times Release 6 HSDPA. Averaged user throughput per MHz, 3 to 4 times Release 6 HSDPA.

    **Uplink**: User throughput per MHz, 2 to 3 times Release 6 Enhanced Uplink. Averaged user throughput per MHz, 2 to 3 times Release 6 Enhanced Uplink.

* **Spectrum efficiency**

    **Downlink**: In a loaded network, target for spectrum efficiency (bits/sec/Hz/site), 3 to 4 times Release 6 HSDPA.

    **Uplink**: In a loaded network, target for spectrum efficiency (bits/sec/Hz/site), 2 to 3 times Release 6 Enhanced Uplink.

* **Mobility**

    E-UTRAN should be optimized for low mobile speed from **0 to 15 km/h**. Higher mobile speed between **15 and 120 km/h** should be supported with high performance.

    Mobility across the cellular network shall be maintained at speeds from **120 km/h to 350 km/h** (or even up to 500 km/h depending on the frequency band).

* **Coverage**

    User throughput, spectrum efficiency and mobility targets above should be met for 5 km cells, and with a slight degradation for 30 km cells. Cells range up to 100 km should not be precluded.

* **Further Enhanced MBMS**

    E-UTRA broadcast transmission should use the same fundamental modulation, coding and multiple access whether it is deployed on dedicated carrier or a carrier shared with unicast.

* **Deployment Scenarios**

    E-UTRAN shall support the following two deployment scenarios at least:

    * Standalone deployment scenario
    * Integrating with existing UTRAN and/or GERAN deployment scenario
    <p/>

* **Spectrum flexibility**

    E-UTRA shall operate in spectrum allocations of different sizes, including 1.25 MHz, 1.6MHz, 2.5 MHz, 5 MHz, 10 MHz, 15 MHz and 20 MHz in both the uplink and downlink. Operation in paired and unpaired spectrum shall be supported.

    The system shall be able to support (same and different) content delivery over an aggregation of resources including Radio Band Resources (as well as power, adaptive scheduling, etc) in the same and different bands, in both uplink and downlink and in both adjacent and non-adjacent channel arrangements.

* **Spectrum deployment**

    E-UTRA is required to cope with following scenarios:

    * Co-existence in the same geographical area and co-location with GERAN/UTRAN on adjacent channels.
    * Co-existence in the same geographical area and co-location between operators on adjacent channels.
    * Co-existence on overlapping and/or adjacent spectrum at country borders.
    * E-UTRA shall be possible to operate standalone, i.e. there is no need for any other carrier to be available.
    * All frequency bands should be allowed following release independent frequency band principles.
    <p/>

* **Co-existence and interworking with 3GPP RAT**

    The following requirements are applicable to inter-working between E-UTRA and other 3GPP systems:

    * E-UTRAN Terminals supporting also UTRAN and/or GERAN operation should be able to support measurement of, and handover from and to, both 3GPP UTRA and 3GPP GERAN systems correspondingly with acceptable impact on terminal complexity and network performance.
    * E-UTRAN is required to efficiently support inter-RAT measurements with acceptable impact on terminal complexity and network performance, by e.g. providing UE's with measurement opportunities through downlink and uplink scheduling.
    * The interruption time during a handover of real-time services between E-UTRAN and UTRAN is less than 300 msec.
    * The interruption time during a handover of non real-time services between E-UTRAN and UTRAN should be less than 500 msec.
    * The interruption time during a handover of real-time services between E-UTRAN and GERAN is less than 300 msec.
    * The interruption time during a handover of non real-time services between E-UTRAN and GERAN should be less than 500 msec.
    * Non-active terminals (such as one being in Release 6 idle mode or CELL_PCH) which support UTRAN and/or GERAN in addition to E-UTRAN shall not need to monitor paging messages only from one of GERAN, UTRA or E-UTRA.
    <p/>

* **Requirements for E-UTRAN architecture and migration**

    * A single E-UTRAN architecture should be agreed.
    * The E-UTRAN architecture shall be packet based, although provision should be made to support systems supporting real-time and conversational class traffic.
    * E-UTRAN architecture shall minimize the presence of *single points of failure* where possible without additional cost for backhaul.
    * E-UTRAN architecture shall simplify and minimize the introduced number of interfaces where possible.
    * Radio Network Layer (RNL) and Transport Network Layer (TNL) interaction should not be precluded if in the interest of improved system performance.
    * E-UTRAN architecture shall support an end-to-end QoS. The Transport Network Layer (TNL) shall provide the appropriate QoS requested by the Radio Network Layer (RNL).
    * QoS mechanism(s) shall take into account the various types of traffic that exists to provide efficient bandwidth utilization: *Control Plane* traffic, *User Plane* traffic, O&M traffic etc.
    * The E-UTRAN shall be designed in such a way to minimize the delay variation (jitter) for e.g. TCP/IP for packet communication.
    <p/>

* **Radio Resource Management requirements**

    * Enhanced support for end to end QoS
    * Efficient support for transmission of higher layers
    * Support of load sharing and policy management across different Radio Access Technologies
    <p/>

* **Complexity requirements for overall system**

    * Minimize the number of options.
    * No redundant mandatory features.
    * Reduce the number of necessary test cases, e.g. Reduce the number of states of protocols, minimize the number of procedures, appropriate parameter range and granularity.
    <p/>

* **Complexity requirements for UE**

    * UE complexity in terms of supporting multi-RAT (GERAN/UTRA/E-UTRA) should be considered when considering the complexity of E-UTRA features.
    * The mandatory features shall be kept to the minimum.
    * There shall be no redundant or duplicate specifications of mandatory features, or for accomplishing the same task.
    * The number of options shall be minimized. Sets of options shall be realizable in terms of separate distinct UE *types/capabilities*. Different UE *types/capabilities* shall be used to capture different complexity vs. performance trade-offs, e.g. for the impact of multiple antennas.
    * The number of necessary test cases shall be minimizied so it is feasible to complete the development of the test cases in a reasonable timeframe after the Core Specifications are completed. No unnecessary test cases shall be developed.
    <p/>

* **Cost-related requirements**

    * Backhaul communication protocols should be optimized.
    * The E-UTRAN architecture should reduce the cost of future network deployment whilst enabling the usage of existing site locations.
    * All the interfaces specified shall be open for multi-vendor equipment interoperability.
    * UE complexity and power consumption shall be minimized/optimized. Complicated UTRAN architecture and unnecessary interfaces should be avoided.
    * More efficient and easy to use OAM&P.
    <p/>

* **Service-related requirements**

    The E-UTRA should efficiently support various types of service. These must include currently available services like web-browsing, FTP, video-streaming or VoIP, and more advanced services (e.g. real-time video or push-to-x) in the PS-domain.

    VoIP should be supported with at least as good radio, backhaul efficiency and latency as voice traffic over the UMTS CS networks.

# Network Architecture

According to [LTE Network Architecture](http://www.tutorialspoint.com/lte/lte_network_architecture.htm) and **Figure 4.7.2-1** in **TS 36.300**, the high-level network architecture of LTE is comprised of following three main components:

* [User Equipment (UE)](#user-equipment-ue)
* [Evolved UMTS Terrestrial Radio Access Network (E-UTRAN)](#evolved-umts-radio-access-network-e-utran)
* [Evolved Packet Core (EPC)](#evolved-packet-core-epc)

![LTE Architecture](/assets/lte_architecture.jpg)

![E-UTRAN](/assets/lte_e_utran.jpg)

![EPC](/assets/lte_epc.jpg)

# Protocol Architecture

The following figure from **Figure 13.1-1** of **TS 36.300-8c0** shows the EPS Bearer Service Architecture:

![R8_EPS_Bearer_Service_Architecture](/assets/R8_EPS_Bearer_Service_Architecture.png)

According to [LTE Radio Protocol Architecture](http://www.tutorialspoint.com/lte/lte_radio_protocol_architecture.htm), **Figure 4.3.1-1**, **Figure 4.3.2-1**, **Figure 4.6.3.1-1** and **Figure 4.6.3.2-1** of **TS 36.300-8c0**, the protocol architecture on **User-plane** is shown in the following figure:

![lte_user_plane](/assets/lte_user_plane.jpg)

![R8_Interfaces_User_Plane](/assets/R8_Interfaces_User_Plane.png)

The protocol architecture on **Control-plane** is shown in the following figure:

![lte_control_plane](/assets/lte_control_plane.jpg)

![R8_Interfaces_Control_Plane](/assets/R8_Interfaces_Control_Plane.png)

The Radio protocl architecture is shown in the following figure:

![lte_protocol_layers](/assets/lte_protocol_layers.jpg)

# Channel Mapping

The following figure shows the channel mapping between **logical channels**, **transport channels** and **physical channels**:

![Channel_Mapping_R10_LTE-Advanced](/assets/Channel_Mapping_R10_LTE-Advanced.png)

Each **logical channel** type is defined by ***what*** type of information is transferred.

# User Equipment (UE)

The internal architecture of the user equipment (UE) for LTE is identical to the one used by UMTS and GSM which is actually a **Mobile Equipment** (**ME**). The mobile equipment comprised of the following important modules:

* **Mobile Termination** (**MT**): This handles all the communication functions.
* **Terminal Equipment** (**TE**): This terminates the data streams.
* **Universal Integrated Circuit Card** (**UICC**) : This is also known as the SIM card for LTE equipment. It runs an application known as the **Universal Subscriber Identity Module** (**USIM**). A USIM stores user-specific data very similar to 3G SIM card. This keeps information about the user's phone number, home network identity and security keys etc.

UE related specifications include:

* TS 36.101-a70 UE radio transmission and reception
* TS 36.304-a80 UE procedures in idle mode
* TS 36.305-a50 Stage 2 functional specification of User Equipment (UE) positioning in E-UTRAN

# Evolved UMTS Radio Access Network (E-UTRAN)

## E-UTRAN Overview

* TS 36.401-880 E-UTRAN Architecture description
* TS 36.300-8c0 E-UTRA and E-UTRAN Overall description - Stage 2
* TS 36.302-820 E-UTRA - Services provided by the physical layer

## Radio Interface (Uu)

### Radio Resource Control (RRC)

* **TS 36.331-8f0 E-UTRA - RRC Protocol specification**

### Packet Data Convergence Protocol (PDCP)

* **TS 36.323-860 E-UTRA - Packet Data Convergence Protocol (PDCP) specification**
* **TS 36.314-830 E-UTRA - Layer 2 Measurements**

#### PDCP Services

PDCP provides its services to the **RRC** and **user plane** upper layers at the UE or to the relay at the evolved Node B (eNB). The following services are provided by PDCP to upper layers:

* transfer of user plane data;
* transfer of control plane data;
* header compression (U-plane only) using ROHC protocol;
* integrity protection (C-plane only);
* ciphering (U-plane and C-plane).

The maximum supported size of a PDCP SDU is **8188 octets**.

#### PDCP Functions

#### PDCP Procedures

The following figure from **Figure 4.2.1.1** of **TS 36.323-860** shows the structure view of PDCP layer:

![R8_structure_view_of_PDCP](/assets/R8_structure_view_of_PDCP.png)

The following figure from **Figure 4.2.2.1** of **TS 36.323-860** shows the functional view of PDCP layer:

![R8_functional_view_of_PDCP](/assets/R8_functional_view_of_PDCP.png)

#### ROHC Resources

* [ROHC - Robust Header Compression](http://rohc.sourceforge.net/): a free implementation of **ROHC** (Robust Header Compression) defined in **RFC 3095**

### Radio Link Control (RLC)

* **TS 36.322-880 E-UTRA - RLC protocol specification**
* **TS 36.314-830 E-UTRA - Layer 2 Measurements**

#### RLC Services

The following services are provided by RLC to upper layer (i.e. RRC or PDCP):

* Transparent Mode (TM) data transfer;
* Unacknowledged Mode (UM) data transfer;
* Acknowledged Mode (AM) data transfer, including indication of successful delivery of upper layers PDUs.

#### RLC Functions

#### RLC Procedures

The following figure from **Figure 4.2.1.1.1-1** of **TS 36.322-880** shows the model of two transparent mode (TM) peer entities:

![Model_of_two_transparent_mode_peer_entities](/assets/R8_Model_of_two_transparent_mode_peer_entities.png)

The following figure from **Figure 4.2.1.2.1-1** of **TS 36.322-880** shows the model of two unacknowledged mode (UM) peer entities:

![R8_Model_of_two_unacknowledged_mode_peer_entities](/assets/R8_Model_of_two_unacknowledged_mode_peer_entities.png)

The following figure from **Figure 4.2.1.3.1-1** of **TS 36.322-880** shows the model of two acknowledged mode (AM) peer entities:

![R8_Model_of_an_acknowledged_mode_entities](/assets/R8_Model_of_an_acknowledged_mode_entities.png)

### Medium Access Control (MAC)

* **TS 36.321-8a0 E-UTRA - MAC protocol specification**
* **TS 36.314-830 E-UTRA - Layer 2 Measurements**

#### MAC Services

According to section **4.3.1** of **TS 36.321-8a0**, the following two kind of services are provided by MAC sublayer to upper layers:

* Data transfer
* Radio resource allocation

#### MAC Functions

According to section **4.4** of **TS 36.321-8a0**, the following functions are supported by MAC sublayer:

* mapping between logical channels and transport channels, refer to [Channel Mapping](#channel-mapping);
* multiplexing of MAC SDUs from one or different logical channels onto transport blocks (TB) to be delivered to the physical layer on transport channels;
* demultiplexing of MAC SDUs from one or different logical channels from transport blocks (TB) delivered from the physical layer on transport channels;
* scheduling information reporting;
* error correction through HARQ;
* priority handling between UEs by means of dynamic scheduling;
* priority handling between logical channels of one UE;
* Logical Channel prioritisation;
* transport format selection.

#### MAC Procedures

Refer to section **5** of **TS 36.321-8a0**.

### Physical Layer (L1)

* **TS 36.201-830 E-UTRA - LTE Physical Layer General Description**
* **TS 36.211-890 E-UTRA - Physical Channels and Modulation**
* **TS 36.212-880 E-UTRA - Multiplexing and channel coding**
* **TS 36.213-880 E-UTRA - Physical layer procedures**
* **TS 36.214-870 E-UTRA - Physical layer Measurements**

The following figure from **Figure 2** of **TS 36.201-830** shows the relation between the physical layer specifications:

![R8_Relation_between_Physical_Layer_specifications](/assets/R8_Relation_between_Physical_Layer_specifications.png)

#### L1 Services

According to section **4.1.2** of **TS 36.201-830**, the physical layer offers **data transport services to higher layers**. The access to these services is through the use of a transport channel via the MAC sub-layer.

#### L1 Functions

According to section **4.1.2** of **TS 36.201-830**, the physical layer is expected to perform the following functions in order to provide the data transport service:

* Error detection on the transport channel and indication to higher layers
* FEC encoding/decoding of the transport channel
* Hybrid ARQ soft-combining
* Rate matching of the coded transport channel to physical channels
* Mapping of the coded transport channel onto physical channels
* Power weighting of physical channels
* Modulation and demodulation of physical channels
* Frequency and time synchronisation
* Radio characteristics measurements and indication to higher layers
* Multiple Input Multiple Output (MIMO) antenna processing
* Transmit Diversity (TX diversity)
* Beamforming
* RF processing. (Note: RF processing aspects are specified in the TS 36.100 series)

#### L1 Procedures

According to section **4.2.4** of **TS 36.201-830**, there are several Physical layer procedures involved with LTE operation. Such procedures covered by the physical layer are:

* Cell search
* Power control
* Uplink synchronisation and Uplink timing control
* Random access related procedures
* HARQ related procedures

## S1 Interface

The S1 interfaces related specifications are:

* TS 36.410-830 E-UTRAN - S1 general aspects and principles
* TS 36.411-810 E-UTRAN - S1 layer 1
* TS 36.412-860 E-UTRAN - S1 signaling transport
* TS 36.413-8a0 E-UTRAN - S1 Application Protocol (S1AP)
* TS 36.414-840 E-UTRAN - S1 data transport

The S1 interface connects the Evolved NodeB (eNB) component of the E-UTRAN to the Core Network of the SAE system, refer to [Network Architecture](#network-architecture), [Protocol Architecture](#protocol-architecture) and the following figure:

![TS36.410-830-F1-S1-Interface-architecture](/assets/TS36.410-830-F1-S1-Interface-architecture.png)

From the S1 perspective, the E-UTRAN access point is an eNB, and the EPC access point is either the control plane MME logical node or the user plane S-GW logical node. Two types of S1 interfaces are thus defined at the boundary depending on the EPC access point: **S1-MME** towards an MME and **S1-U** towards an S-GW.

The S1 is a **logical interface**. The S1 is a **point-to-point** interface between an eNB within the E-UTRAN and an MME in the EPC. A point-to-point logical interface should be feasible even in the absence of a physical direct connection between the eNB and MME.

## X2 Interface

The X2 interfaces related specifications are:

* TS 36.420-810 E-UTRAN - X2 general aspects and principles
* TS 36.421-800 E-UTRAN - X2 layer 1
* TS 36.422-860 E-UTRAN - X2 signaling transport
* TS 36.423-890 E-UTRAN - X2 application protocol (X2AP)
* TS 36.424-850 E-UTRAN - X2 data transport

The S1 interface connects two E-UTRAN NodeB (eNB) components within the E-UTRAN architecture, refer to [Network Architecture](#network-architecture), [Protocol Architecture](#protocol-architecture).

The X2 is a point-to-point interface between two eNBs within the E-UTRAN. A point-to-point logical interface should be feasible even in the absence of a physical direct connection between the two eNBs.

# Evolved Packet Core (EPC)

## S10 Interface

## S11 Interface

## S5/S8 Interface

## S6a Interface

## SGi Interface

# Technical Details

# Procedures

* TS 36.304 - Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode

# References

* [ShareTechnote](http://www.sharetechnote.com/)
* [LTE Dictionary on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE.html)
* [LTE Full Stack on ShareTechnote](http://www.sharetechnote.com/html/FullStack_LTE.html)
* [LTE PDCP Layer on ShareTechnote](http://www.sharetechnote.com/html/PDCP_LTE.html)
* [LTE RLC Layer on ShareTechnote](http://www.sharetechnote.com/html/RLC_LTE.html)
* [LTE MAC Layer on ShareTechnote](http://www.sharetechnote.com/html/MAC_LTE.html)
* [LTE PHY Processing on ShareTechnote](http://www.sharetechnote.com/html/PhyProcessing_LTE.html)
* [LTE Quick Reference on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_PhySequence.html)
* [LTE Basic Procedure on ShareTechnote](http://www.sharetechnote.com/html/BasicProcedure_LTE_PHY_Process.html)
* [3GLTEinfo](http://www.3glteinfo.com/)

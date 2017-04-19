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

The **logical channel** is defined by ***what*** type of information is transferred. The **transport channel** is characterized by ***how*** the information is transferred over the radio interface.

According to **TS 36.300**, the following figure shows the channel mapping between **logical channels**, **transport channels** and **physical channels**:

![Channel_Mapping_R10_LTE-Advanced](/assets/Channel_Mapping_R10_LTE-Advanced.png)

![Channel_Mapping_R8_TS36.212_S4](/assets/Channel_Mapping_R8_TS36.212_S4.png)

# Frame Structure

According to section 4 of **TS 36.211**, there are two types of frame structure in LTE:

* The frame structure type 1 is applicable to both full duplex and half duplex FDD-LTE.
* The frame structure type 2 is applicable to TDD-LTE.

![R8_TS36.211_S4_Frame_Type](/assets/R8_TS36.211_S4_Frame_Type.png)

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

The following specifications are related to E-UTRAN overview:

* TS 36.401-880 E-UTRAN Architecture description
* TS 36.300-8c0 E-UTRA and E-UTRAN Overall description - Stage 2
* TS 36.302-820 E-UTRA - Services provided by the physical layer

According to **TS 23.401 S4.4.1**, in addition to the E-UTRAN functions described in **TS 36.300**, E-UTRAN functions include:

* Header compression and user plane ciphering;
* MME selection when no routing to an MME can be determined from the information provided by the UE;
* UL bearer level rate enforcement based on UE-AMBR (Aggregate Maximum Bit Rate) and MBR (Maximum Bit Rate) via means of uplink scheduling (e.g. by limiting the amount of UL resources granted per UE over time);
* DL bearer level rate enforcement based on UE-AMBR (Aggregate Maximum Bit Rate);
* UL and DL bearer level admission control;
* Transport level packet marking in the uplink, e.g. setting the DiffServ Code Point, based on the QCI of the associated EPS bearer.

## Radio Interface (Uu)

Refer to [Protocol Architecture](#protocol-architecture) for the User-plane and Control-plane protocol layers of Uu interface.

### Radio Resource Control (RRC)

* **TS 36.331-8f0 E-UTRA - RRC Protocol specification**

### Packet Data Convergence Protocol (PDCP)

* **TS 36.323-860 E-UTRA - Packet Data Convergence Protocol (PDCP) specification**
* TS 36.314-830 E-UTRA - Layer 2 Measurements

#### PDCP Services

PDCP provides its services to the **RRC** and **user plane** upper layers at the UE or to the relay at the evolved Node B (eNB). The following services are provided by PDCP to upper layers:

* transfer of user plane data;
* transfer of control plane data;
* header compression (U-plane only) using [ROHC protocol](#rohc-resources);
* integrity protection (C-plane only);
* ciphering (U-plane and C-plane).

The maximum supported size of a PDCP SDU is **8188 octets**.

#### PDCP Procedures

The following figure from **Figure 4.2.1.1** of **TS 36.323-860** shows the structure view of PDCP layer:

![R8_structure_view_of_PDCP](/assets/R8_structure_view_of_PDCP.png)

The following figure from **Figure 4.2.2.1** of **TS 36.323-860** shows the functional view of PDCP layer:

![R8_functional_view_of_PDCP](/assets/R8_functional_view_of_PDCP.png)

#### PDCP PDU Formats

**Control Plane PDCP PDUs**

**Control Plane PDCP PDUs**

#### ROHC Resources

* [ROHC - Robust Header Compression](http://rohc.sourceforge.net/): a free implementation of **ROHC** (Robust Header Compression) defined in **RFC 3095**

### Radio Link Control (RLC)

* **TS 36.322-880 E-UTRA - RLC protocol specification**
* TS 36.314-830 E-UTRA - Layer 2 Measurements

#### RLC Services

The following services are provided by RLC to upper layer (i.e. RRC or PDCP):

* **Transparent Mode** (**TM**) data transfer;
* **Unacknowledged Mode** (**UM**) data transfer;
* **Acknowledged Mode** (**AM**) data transfer, including indication of successful delivery of upper layers PDUs.

#### RLC Procedures

The following figure from **Figure 4.2.1.1.1-1** of **TS 36.322-880** shows the model of two **transparent mode** (**TM**) peer entities:

![Model_of_two_transparent_mode_peer_entities](/assets/R8_Model_of_two_transparent_mode_peer_entities.png)

The following figure from **Figure 4.2.1.2.1-1** of **TS 36.322-880** shows the model of two **unacknowledged mode** (**UM**) peer entities:

![R8_Model_of_two_unacknowledged_mode_peer_entities](/assets/R8_Model_of_two_unacknowledged_mode_peer_entities.png)

The following figure from **Figure 4.2.1.3.1-1** of **TS 36.322-880** shows the model of two **acknowledged mode** (**AM**) peer entities:

![R8_Model_of_an_acknowledged_mode_entities](/assets/R8_Model_of_an_acknowledged_mode_entities.png)

### Medium Access Control (MAC)

* **TS 36.321-8a0 E-UTRA - MAC protocol specification**
* TS 36.314-830 E-UTRA - Layer 2 Measurements

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
* logical channel prioritisation;
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

The S1 interface connects two E-UTRAN NodeB (eNB) components within the E-UTRAN architecture, refer to [Network Architecture](#network-architecture) and [Protocol Architecture](#protocol-architecture).

The X2 is a point-to-point interface between two eNBs within the E-UTRAN. A point-to-point logical interface should be feasible even in the absence of a physical direct connection between the two eNBs.

# Evolved Packet Core (EPC)

## EPC Entities

### Mobility Management Entity (MME)

According to **TS 23.401 S4.4.2**, MME functions include:

* NAS signalling;
* NAS signalling security;
* Inter CN node signalling for mobility between 3GPP access networks (terminating S3);
* UE Reachability in ECM-IDLE state (including control and execution of paging retransmission);
* Tracking Area list management;
* PDN GW and Serving GW selection;
* MME selection for handovers with MME change;
* SGSN selection for handovers to 2G or 3G 3GPP access networks;
* Roaming (S6a towards home HSS);
* Authentication;
* Authorization;
* Bearer management functions including dedicated bearer establishment;
* Lawful Interception of signalling traffic;
* Warning message transfer function (including selection of appropriate eNodeB);
* UE Reachability procedures.

NOTE: The **S-GW** and the **MME** may be implemented in one physical node or separated physical nodes.

### Serving GW (S-GW)

According to **TS 23.401 S4.4.3.2**, the Serving GW is the gateway which terminates the interface towards E-UTRAN. For each UE associated with the EPS, at a given point of time, there is a single Serving GW. The functions of the Serving GW, for both the GTP-based and the PMIP-based S5/S8, include:

* the local Mobility Anchor point for inter-eNodeB handover;
* sending of one or more "end marker" to the source eNodeB, source SGSN or source RNC immediately after switching the path during inter-eNodeB and inter-RAT handover, especially to assist the reordering function in eNodeB.
* Mobility anchoring for inter-3GPP mobility (terminating S4 and relaying the traffic between 2G/3G system and PDN GW);
* ECM-IDLE mode downlink packet buffering and initiation of network triggered service request procedure;
* Lawful Interception;
* Packet routing and forwarding;
* Transport level packet marking in the uplink and the downlink, e.g. setting the DiffServ Code Point, based on the QCI of the associated EPS bearer;
* Accounting for inter-operator charging. For GTP-based S5/S8, the Serving GW generates accounting data per UE and bearer;
* Interfacing OFCS according to charging principles and through reference points specified in TS 32.240.

Additional Serving GW functions for the PMIP-based S5/S8 are captured in **TS 23.402**. Connectivity to a GGSN is not supported.

NOTE: The **P-GW** and **S-GW** may be implemented in one physical node or separated physical nodes.

### PDN GW (P-GW)

According to **TS 23.401 S4.4.3.3**, the PDN GW is the gateway which terminates the SGi interface towards the PDN. If a UE is accessing multiple PDNs, there may be more than one PDN GW for that UE, however a mix of S5/S8 connectivity and Gn/Gp connectivity is not supported for that UE simultaneously. PDN GW functions include for both the GTP-based and the PMIP-based S5/S8:

* Per-user based packet filtering (by e.g. deep packet inspection);
* Lawful Interception;
* UE IP address allocation;
* Transport level packet marking in the uplink and downlink, e.g. setting the DiffServ Code Point, based on the QCI of the associated EPS bearer;
* Accounting for inter-operator charging;
* UL and DL service level charging as defined in TS 23.203 (e.g. based on SDFs defined by the PCRF, or based on deep packet inspection defined by local policy);
* Interfacing OFCS through according to charging principles and through reference points specified in TS 32.240.
* UL and DL service level gating control as defined in TS 23.203;
* UL and DL service level rate enforcement as defined in TS 23.203 (e.g. by rate policing/shaping per SDF);
* UL and DL rate enforcement based on APN-AMBR (e.g. by rate policing/shaping per aggregate of traffic of all SDFs of the same APN that are associated with Non-GBR QCIs);
* DL rate enforcement based on the accumulated MBRs of the aggregate of SDFs with the same GBR QCI (e.g. by rate policing/shaping);
* DHCPv4 (server and client) and DHCPv6 (client and server) functions;
* The network does not support PPP bearer type in this version of the specification. Pre-Release 8 PPP functionality of a GGSN may be implemented in the PDN GW;
* packet screening.

Additionally the PDN GW includes the following functions for the GTP-based S5/S8:

* UL and DL bearer binding as defined in TS 23.203;
* UL bearer binding verification as defined in TS 23.203;
* Functionality as defined in RFC 4861;
* Accounting per UE and bearer.

The P-GW provides PDN connectivity to both GERAN/UTRAN only UEs and E-UTRAN capable UEs using any of E-UTRAN, GERAN or UTRAN. The P-GW provides PDN connectivity to E-UTRAN capable UEs using E-UTRAN only over the S5/S8 interface.

NOTE: The **P-GW** and **S-GW** may be implemented in one physical node or separated physical nodes.

## Interfaces

### S10 Interface

### S11 Interface

### S5/S8 Interface

### S6a Interface

### SGi Interface

# Technical Components of LTE-Advanced

The followings are the technical components to implement LTE-Advanced:

![LTE_Advanced_Technical_Component_01](/assets/LTE_Advanced_Technical_Component_01.png)

## Carrier Aggregation (CA)

**3GPP Specifications**

Refer to the [3GPP_Carrier Aggregation for LTE_20141015.zip](ftp://www.3gpp.org/Information/WORK_PLAN/Description_Releases/) on 3GPP FTP site.

Refer to the artical **Carrier Aggregation explained** on [3GPP website](http://www.3gpp.org/technologies/keywords-acronyms/101-carrier-aggregation-explained) or [its local copy on GitHub](/docs/Carrier_Aggregation_explained.pdf) for explainations of carrier aggregation.

Refer to the artical **LTE CA: Carrier Aggregation Tutorial** on [Radio-Electronic.com](http://www.radio-electronics.com/info/cellulartelecomms/lte-long-term-evolution/4g-lte-advanced-carrier-channel-aggregation.php) or [its local copy on GitHub](/docs/What_is_LTE_Carrier_Aggregation.pdf) for the tutorial of carrier aggregation.

And read the following specifications:

* TR 36.808 Evolved Universal Terrestrial Radio Access (E-UTRA); Carrier Aggregation; Base Station (BS) radio transmission and reception
* TR 36.814 Evolved Universal Terrestrial Radio Access (E-UTRA); Further advancements for E-UTRA physical layer aspects
* TR 36.815 Further Advancements for E-UTRA; LTE-Advanced feasibility studies in RAN WG4
* TR 36.823 Evolved Universal Terrestrial Radio Access (E-UTRA); Carrier Aggregation Enhancements; UE and BS radio transmission and reception
* TR 36.912 Feasibility study for Further Advancements for E-UTRA (LTE-Advanced)
* TR 36.913 Requirements for further advancements for Evolved Universal Terrestrial Radio Access (E-UTRA) (LTE-Advanced)
* TS 36.101 Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio transmission and reception
  * TS 36.101-e30 Section 5.6A: Channel bandwidth for CA
  * TS 36.101-e30 Table 5.6A-1: CA bandwidth classes and corresponding nominal guard bands
  * TS 36.101-e30 Section 5.7.1A: Channel spacing for CA
  * TS 36.101-e30 Section 5.7.2A: Channel raster for CA
  * TS 36.101-e30 Section 5.7.4A: TX–RX frequency separation for CA
* TS 36.211 Evolved Universal Terrestrial Radio Access (E-UTRA); Physical channels and modulation
* TS 36.212 Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding
* TS 36.213 Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures
* TS 36.300 Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2

**Initial Motivation for Carrier Aggregation**

Does this mean that they already feel the current 20 Mhz LTE bandwidth is not enough? As far as I know, it is not because of this. Even though the current LTE supports 20 Mhz BW in maximum, there are only a few network operators who is certified for such a wide bandwidth. The most common bandwidth that network operators has for LTE is 10 Mhz, which means they are not fully utilizing the LTE capability in terms of bandwidth. This is not because of technical restriction, it is purely because of licensing issues for the allocated bandwidth.

Even though there is not many Network Operators who has 20 Mhz BW, there are some network operators who has license multiple band (e.g, two separated 10 Mhz BW and two or more 5 Mhz BW). These network operators wants to combine those multiple bands to achieve wide BW (in most case 20 Mhz BW) LTE. It is the initial motivation for LTE Advanced for now.

**What is Carrier Aggregation?**

Carrier Aggregation is a special form of LTE technology that enables UE and Network to use more than one carrier frequencies. Actually this is not a new concept in LTE. You might have used/heard Dual Carrier in WCDMA HSDPA (HSDPA DC) or similar mode in WiFi (I forgot the terminology in WiFi).

**How can I know which band combination of bands a UE support in terms of Carrier Aggregation?**

It is also supposed to be reported to network by the UE via UE Capability Information message. Followings are some of the possible IEs a UE may use depending on its release status, refer to TS 36.331:

```
RF-Parameters-v1020 ::= SEQUENCE {
    supportedBandCombination-r10    SupportedBandCombination-r10
}

RF-Parameters-v1090 ::= SEQUENCE {
    supportedBandCombination-v1090  SupportedBandCombination-v1090  OPTIONAL
}

RF-Parameters-v1130 ::= SEQUENCE {
    supportedBandCombination-v1130  SupportedBandCombination-v1130  OPTIONAL
}
```

Refer to the following tables for all the possible (allowed) band combination of inter-band and intra-band CA case:

* TS 36.101-e30 Table 5.6A-1: CA bandwidth classes and corresponding nominal guard bands
* TS 36.101-e30 Table 5.6A.1-1: E-UTRA CA configurations and bandwidth combination sets defined for intra-band contiguous CA
* TS 36.101-e30 Table 5.6A.1-2: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (two bands)
* TS 36.101-e30 Table 5.6A.1-2a: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (three bands)
* TS 36.101-e30 Table 5.6A.1-2b: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (four bands)
* TS 36.101-e30 Table 5.6A.1-2c: E-UTRA CA configurations and bandwidth combination sets defined for inter-band CA (five bands)
* TS 36.101-e30 Table 5.6A.1-3: E-UTRA CA configurations and bandwidth combination sets defined for non-contiguous intra-band CA (with two sub-blocks)

## Enhanced UL Transmission (Clustered SC-FDMA)

## Enhanced MIMO

## Relay Node

One of the key modification of LTE advanced is **Relay Node** to improve data communication especially on cell boundary and increase cell coverage.

![LTE_Advanced_R10_Network_Overview](/assets/LTE_Advanced_R10_Network_Overview.png)

The following table from [NTT DoCoMo technical report](/docs/Relay_Technology_in_LTE-Advanced_DoCoMo_Report_Vol12_2_029en.pdf):

![DoCoMo Technology Report vol 12-2](/assets/LTE_Advanced_RN_DoCoMoTechnote.png)

## LTE CoMP (Coordinated Multi Point transmission)

# Procedures

* TS 36.304 - Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode

# References

* [ShareTechnote](http://www.sharetechnote.com/)
* [ShareTechnote Index](http://www.sharetechnote.com/html)
* [LTE Dictionary on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE.html)
* [LTE Full Stack on ShareTechnote](http://www.sharetechnote.com/html/FullStack_LTE.html)
* [LTE PDCP Layer on ShareTechnote](http://www.sharetechnote.com/html/PDCP_LTE.html)
* [LTE RLC Layer on ShareTechnote](http://www.sharetechnote.com/html/RLC_LTE.html)
* [LTE MAC Layer on ShareTechnote](http://www.sharetechnote.com/html/MAC_LTE.html)
* [LTE PHY Processing on ShareTechnote](http://www.sharetechnote.com/html/PhyProcessing_LTE.html)
* [LTE Quick Reference on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_PhySequence.html)
* [LTE Basic Procedure on ShareTechnote](http://www.sharetechnote.com/html/BasicProcedure_LTE_PHY_Process.html)
* [Typical Packet Call Processing on ShareTechnote](http://www.sharetechnote.com/html/BasicCallFlow_LTE_ChannelMap.html)
* [LTE Network Architecture on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_NetworkArchitecture.html)
* [LTE SAE on ShareTechnote](http://www.sharetechnote.com/html/Handbook_LTE_SAE.html)
* [3GLTEinfo](http://www.3glteinfo.com/)
* [LTE Network Architecture](/docs/LTE_Network_Architecture_StraWhitePaper.pdf)

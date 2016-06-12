---
layout: post
title: "LTE: System Requirements"
tag: Telecommunication
toc: true
---

This article introduce the system requirements of LTE / LTE-Advanced network.

<!--more-->

# History

Although marketed as a 4G wireless service, **LTE** (as specified in the 3GPP Release 8 and 9 document series) does not satisfy the technical requirements the 3GPP consortium has adopted for its new **LTE-Advanced** standard. The requirements were originally set forth by the ITU-R organization in its **IMT Advanced** specification. However, due to marketing pressures and the significant advancements that WiMAX, Evolved High Speed Packet Access (HSPA+) and LTE bring to the original 3G technologies, ITU later decided that LTE together with the aforementioned technologies can be called 4G technologies. The LTE Advanced standard formally satisfies the ITU-R requirements to be considered IMT-Advanced. To differentiate LTE Advanced and WiMAX-Advanced from current 4G technologies, ITU has defined them as **True 4G**.

# Standards

ITU Recommendations related to LTE/LTE-Advanced are introduced in the section <a href="{{ site.base-url }}/2016/03/13/telecom-itu-recommendations.html">IMT-Advanced (4G)</a>.

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

3GPP specifications: **TS 36.XXX**

# Requirements

The objective of Evolved UTRA and UTRAN is to develop a framework for the evolution of the 3GPP radio-access technology towards a **high-data-rate**, **low-latency** and **packet-optimized** radio-access technology.

The LTE/LTE-Advanced requirements are defined in **TR 25.913-800 Requirements for E-UTRA and E-UTRAN**:

* **Peak data rate**

    ***Configuration***: 1 transmit antenna and 2 receive antennas at UE
    ***Downlink***: instantaneous downlink peak data rate of **100Mb/s** within a **20 MHz** downlink spectrum allocation (5 bps/Hz)
    ***Uplink***: instantaneous uplink peak data rate of **50Mb/s** (2.5 bps/Hz) within a **20MHz** uplink spectrum allocation.

* **C-plane latency**

    Transition time (excluding downlink paging delay and NAS signalling delay) of less than **100 ms** from a camped-state (such as Release 6 Idle Mode) to an active state (such as Release 6 CELL_DCH).

    Transition time (excluding DRX interval) of less than **50 ms** between a dormant state (such as Release 6 CELL_PCH) and an active state (such as Release 6 CELL_DCH).

* **C-plane capacity**

    At least **200 users per cell** should be supported in the active state for spectrum allocations up to **5 MHz**, and at least **400 users** for higher spectrum allocation.

* **U-plane latency**

    Less than **5 ms** in unload condition (i.e. single user with single data stream) for small IP packet.

* **User throughput**

    ***Downlink***: User throughput per MHz, 2 to 3 times Release 6 HSDPA. Averaged user throughput per MHz, 3 to 4 times Release 6 HSDPA.
    ***Uplink***: User throughput per MHz, 2 to 3 times Release 6 Enhanced Uplink. Averaged user throughput per MHz, 2 to 3 times Release 6 Enhanced Uplink.

* **Spectrum efficiency**

    ***Downlink***: In a loaded network, target for spectrum efficiency (bits/sec/Hz/site), 3 to 4 times Release 6 HSDPA.
    ***Uplink***: In a loaded network, target for spectrum efficiency (bits/sec/Hz/site), 2 to 3 times Release 6 Enhanced Uplink.

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

# References

* TR 25.913-800: Requirements for E-UTRA and E-UTRAN
* [http://www.sharetechnote.com/](http://www.sharetechnote.com/)
* [http://www.sharetechnote.com/html](http://www.sharetechnote.com/html)
* [http://www.3glteinfo.com/](http://www.3glteinfo.com/)

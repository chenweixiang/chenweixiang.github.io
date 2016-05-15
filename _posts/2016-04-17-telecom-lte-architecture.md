---
layout: post
title: "LTE: Network Architecture"
tag: Telecommunication
toc: true
---

This article introduce the network and protocol architectures of LTE/LTE-Advanced network.

<!--more-->

# Network Architecture

According to [LTE Network Architecture](http://www.tutorialspoint.com/lte/lte_network_architecture.htm) and **Figure 4.7.2-1** in **TS 36.300-8c0**, the high-level network architecture of LTE is comprised of the following three main components:

* User Equipment (UE)
* Evolved UMTS Terrestrial Radio Access Network (E-UTRAN)
* Evolved Packet Core (EPC)

![LTE Architecture](/assets/lte_architecture.jpg)
![E-UTRAN](/assets/lte_e_utran.jpg)
![EPC](/assets/lte_epc.jpg)

More EPC architectures can be found in **TS 23.401**.

## E-URTAN

According to **TS 23.401 S4.4.1**, in addition to the E-UTRAN functions described in **TS 36.300**, E-UTRAN functions include:

* Header compression and user plane ciphering;
* MME selection when no routing to an MME can be determined from the information provided by the UE;
* UL bearer level rate enforcement based on UE-AMBR and MBR via means of uplink scheduling (e.g. by limiting the amount of UL resources granted per UE over time);
* DL bearer level rate enforcement based on UE-AMBR;
* UL and DL bearer level admission control;
* Transport level packet marking in the uplink, e.g. setting the DiffServ Code Point, based on the QCI of the associated EPS bearer.

## Mobility Management Entity (MME)

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

## Serving GW (S-GW)

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

Additional Serving GW functions for the PMIP-based S5/S8 are captured in TS 23.402. Connectivity to a GGSN is not supported.

NOTE: The **P-GW** and **S-GW** may be implemented in one physical node or separated physical nodes.

## PDN GW (P-GW)

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

# References

**3GPP Specs**

TS 36.300-8c0

**ShareTechnote**

[http://www.sharetechnote.com/](http://www.sharetechnote.com/)

[http://www.sharetechnote.com/html/Handbook_LTE_NetworkArchitecture.html](http://www.sharetechnote.com/html/Handbook_LTE_NetworkArchitecture.html)

[http://www.sharetechnote.com/html/Handbook_LTE_SAE.html](http://www.sharetechnote.com/html/Handbook_LTE_SAE.html)

**3GLTEInfo**

[http://www.3glteinfo.com/](http://www.3glteinfo.com/)

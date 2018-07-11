---
layout: post
title: "Telecom: 3GPP Introduction"
tag: Telecom
toc: true
---

This article introduce the 3GPP and its specifications related to Telecommunication.

<!--more-->

# 3GPP Overview

The [3rd Generation Partnership Project (3GPP)](http://www.3gpp.org/) is a collaboration between groups of telecommunications associations, known as the Organizational Partners. The initial scope of 3GPP was to make a globally applicable third-generation (3G) mobile phone system specification based on evolved Global System for Mobile Communications (GSM) specifications within the scope of the International Mobile Telecommunications-2000 (IMT-2000) project of the International Telecommunication Union (ITU). The scope was later enlarged to include the development and maintenance of:

* **GSM** and related 2G and 2.5G standards including GPRS and EDGE
* **UMTS** and related 3G standards including HSPA
* **LTE** and related 4G standards
* An evolved IP Multimedia Subsystem (**IMS**) developed in an access independent manner

3GPP standardization encompasses **Radio**, **Core Network** and **Service** architecture. The project was established in **December 1998** and should not be confused with 3rd Generation Partnership Project 2 (3GPP2), which specifies standards for another 3G technology based on IS-95 (CDMA), commonly known as CDMA2000. The 3GPP support team (also known as the "Mobile Competence Centre") is located at the European Telecommunications Standards Institute (ETSI) headquarters in Sophia-Antipolis (France).

## 3GPP Partners

The seven **3GPP Organizational Partners** are from Asia, Europe and North America. Their aim is to determine the general policy and strategy of 3GPP and perform the following tasks:

* The approval and maintenance of the 3GPP scope;
* The maintenance of the Partnership Project Description;
* Take the decision to create or cease a Technical Specification Groups (TSGs), and approve their scope and terms of reference;
* The approval of Organizational Partner funding requirements;
* The allocation of human and financial resources provided by the Organizational Partners to the Project Co-ordination Group;
* Act as a body of appeal on procedural matters referred to them.

Together with the **Market Representation Partners** (**MRPs**) perform the following tasks:

* The maintenance of the Partnership Project Agreement;
* The approval of applications for 3GPP partnership;
* Take the decision against a possible dissolution of 3GPP.

| Organization | Base Region |
| :----------- | :---------: |
| Association of Radio Industries and Businesses (ARIB) | Japan |
| Alliance for Telecommunications Industry Solutions (ATIS) | USA |
| China Communications Standards Association (CCSA) | China |
| European Telecommunications Standards Institute (ETSI) | Europe |
| Telecommunications Technology Association (TTA) | Korea |
| Telecommunication Technology Committee (TTC) | Japan |
| Telecommunications Standards Development Society India (TSDSI) | India |

<p/>

The **3GPP Organizational Partners** can invite a **Market Representation Partner** (**MRPs**) to take part in 3GPP, which:

* Has the ability to offer market advice to 3GPP and to bring into 3GPP a consensus view of market requirements (e.g., services, features and functionality) falling within the 3GPP scope;
* Does not have the capability and authority to define, publish and set standards within the 3GPP scope, nationally or regionally;
* Has committed itself to all or part of the 3GPP scope;
* Has signed the Partnership Project Agreement.

As of November 2013 the **Market Representation Partners** (**MRPs**) are:

* [IMS Forum](http://www.imsforum.org/)
* [TD-Forum](http://www.tdscdma-forum.org/)
* [Global mobile Suppliers Association (GSA)](http://www.gsacom.com/)
* [GSM Association](http://www.gsmworld.com/)
* [IPV6 Forum](http://www.ipv6forum.com/)
* [UMTS Forum](http://www.umts-forum.org/)
* [4G Americas](http://www.4gamericas.org/)
* [TD SCDMA Industry Alliance](http://www.tdscdma-alliance.org/)
* [InfoCommunication Union](http://www.icu.org.ru/)
* [Small Cell Forum (formerly Femto Forum)](http://www.smallcellforum.org/)
* [CDMA Development Group](http://www.cdg.org/)
* [Cellular Operators Association of India (COAI)](http://www.coai.com/)
* [Next Generation Mobile Networks (NGMN)](http://www.ngmn.org/)
* [TETRA and Critical Communications Association (TCCA)](http://www.tandcca.com/)

## Specification Groups

The 3GPP specification work is done in Technical Specification Groups (**TSGs**) and Working Groups (**WGs**). There are four **TSGs**, each of which consists of multiple **WGs**:

### GERAN (GSM/EDGE Radio Access Network)

GERAN specifies the **GSM radio technology**, including **GPRS** and **EDGE**. It is composed of the following working groups, refer to [TSG GERAN](http://www.3gpp.org/specifications-groups/tsg-geran):

|  Working_Groups | Shorthand | Scope | Specifications |
| :-------------: | :-------: | :---- | :------------: |
| GERAN WG1 | GERAN1 | Radio Aspects | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--G1.htm) |
| GERAN WG2 | GERAN2 | Protocol Aspects | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--G2.htm) |
| GERAN WG3 | GERAN3 | Terminal Testing | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--G3new.htm) |

<p/>

### RAN (Radio Access Network)

RAN specifies the **UTRAN and the E-UTRAN**. It is composed of the following working groups, refer to [TSG RAN](http://www.3gpp.org/specifications-groups/ran-plenary):

|  Working_Groups | Shorthand | Scope | Specifications |
| :-------------: | :-------: | :---- | :------------: |
| RAN WG1 | RAN1 | Radio Layer 1 specification | [List of specs](http://www.3gpp.org/DynaReport/TSG-WG--R1.htm) |
| RAN WG2 | RAN2 | Radio Layer 2 and Radio Layer 3 RR specification | [List of specs](http://www.3gpp.org/DynaReport/TSG-WG--R2.htm) |
| RAN WG3 | RAN3 | Iub Iur and Iu specification - UTRAN O&M requirements | [List of specs](http://www.3gpp.org/DynaReport/TSG-WG--R3.htm) |
| RAN WG4 | RAN4 | Radio performance and protocol aspects (system) - RF parameters and BS conformance | [List of specs](http://www.3gpp.org/DynaReport/TSG-WG--R4.htm) |
| RAN WG5 | RAN5 | Mobile terminal conformance testing | [List of specs](http://www.3gpp.org/DynaReport/TSG-WG--R5.htm) |
| RAN WG6 | RAN6 | Legacy RAN radio and protocol | [List of specs](http://www.3gpp.org/DynaReport/TSG-WG--R6.htm) |

<p/>

RAN protocol stacks vs Working groups:

![3GPP_TSG_RAN_WGs_vs_Protocol_Stacks](/assets/3GPP_TSG_RAN_WGs_vs_Protocol_Stacks.png)

### SA (Service and System Aspects)

SA specifies the service requirements and the overall architecture of the 3GPP system. It is also responsible for the coordination of the project. SA is composed of the following working groups, refer to [TSG SA](http://www.3gpp.org/specifications-groups/sa-plenary):

|  Working_Groups | Shorthand | Scope | Specifications |
| :-------------: | :-------: | :---- | :------------: |
| SA WG1 | SA1 | Services | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--S1.htm) |
| SA WG2 | SA2 | Architecture | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--S2.htm) |
| SA WG3 | SA3 | Security | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--S3.htm) |
| SA WG4 | SA4 | Codec | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--S4.htm) |
| SA WG5 | SA5 | Telecom Management | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--S5.htm) |
| SA WG6 | SA6 | Mission-critical applications | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--S6.htm) |

<p/>

### CT (Core Network and Terminals)

CT specifies the core network and terminal parts of 3GPP. It includes the core network - terminal layer 3 protocols. It is composed of the following working groups, refer to [TSG CT](http://www.3gpp.org/specifications-groups/ct):

|  Working_Groups | Shorthand | Scope | Specifications |
| :-------------: | :-------: | :---- | :------------: |
| CT WG1 | CT1 | MM/CC/SM (lu) | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--C1.htm) |
| CT WG2 | CT2 | closed	| |
| CT WG3 | CT3 | Interworking with external networks | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--C3.htm) |
| CT WG4 | CT4 | MAP/GTP / BCH/SS | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--C4.htm) |
| CT WG5 | CT5 | OSA (Now transferred to [OMA](http://www.openmobilealliance.org/)) | |
| CT WG6 | CT6 | Smart Card Application Aspects | [List of specs](http://www.3gpp.org/ftp/Specs/html-info/TSG-WG--C6.htm) |

<p/>

The 3GPP structure also includes a **Project Coordination Group** (**PCG**), which is the highest decision-making body. Its missions include the management of overall timeframe and work progress.

## Standardization Process

3GPP standardization work is contribution-driven. Companies (individual members) participate through their membership to a 3GPP Organizational Partner. As of April 2011, 3GPP is composed of more than 370 individual members.

Specification work is done at **WG** and at **TSG** level:

* the **3GPP WGs** hold several meetings a year. They prepare and discuss change requests against 3GPP specifications. A change request accepted at WG level is called "agreed".
* the **3GPP TSGs** hold plenary meetings quarterly. The TSGs can "approve" the change requests that were agreed at WG level. Some specifications are under the direct responsibility of TSGs and therefore, change requests can also be handled at TSG level. The approved change requests are subsequently incorporated in 3GPP specifications.

3GPP follows a three-stage methodology as defined in **ITU-T Recommendation I.130**:

* **stage 1 specifications** define the service requirements from the user point of view.
* **stage 2 specifications** define an architecture to support the service requirements.
* **stage 3 specifications** define an implementation of the architecture by specifying protocols in details.

Test specifications are sometimes defined as **stage 4**, as they follow **stage 3**.

Specifications are grouped into releases. A release consists of a set of internally consistent set of features and specifications.

Timeframes are defined for each release by specifying freezing dates. Once a release is frozen, only essential corrections are allowed (i.e. addition and modifications of functions are forbidden). Freezing dates are defined for each stage.

The 3GPP specifications are transposed into deliverables by the Organizational Partners.

# 3GPP Standards

3GPP standards are structured as [Releases](http://www.3gpp.org/specifications/releases). Discussion of 3GPP thus frequently refers to the functionality in one release or another.

## 3GPP Releases Evolution

![3GPP Evolution](/assets/3GPP_Evolution.png)

![3GPP_ongoing_releases](/assets/3GPP_ongoing_releases.JPG)

![Rel15_5G_NR_timeline](/assets/Rel15_5G_NR_timeline.jpg)

## Releases

The following table is from [3GPP wikipedia page](https://en.wikipedia.org/wiki/3GPP). For detail features of each release, refer to [Release Description](http://www.3gpp.org/ftp/Information/WORK_PLAN/Description_Releases/). The table [3GPP Specification Release Version Matrix](http://www.3gpp.org/DynaReport/SpecReleaseMatrix.htm) shows the versions which exist in each Release of the 3GPP specifications. The [3GPP Work Plan](http://www.3gpp.org/specifications/work-plan) and [3GPP Work Programme](http://www.3gpp.org/DynaReport/GanttChart-Level-2.htm) shows the 3GPP work plan.

| [Releases](http://www.3gpp.org/specifications/67-releases) | Released | Description |
| :------- | :------- | :---------- |
| Phase 1 | 1992 | GSM Features. |
| Phase 2 | 1995 | GSM Features, **EFR Codec**. |
| Release 96 | 1997 Q1 | GSM Features, **14.4 kbit/s** User Data Rate. |
| Release 97 | 1998 Q1 | GSM Features, **GPRS**. |
| Release 98 | 1999 Q1 | GSM Features, **AMR**, **EDGE**, **GPRS** for PCS1900. |
| [**Release 99**](http://www.3gpp.org/specifications/releases/77-release-1999) | 2000 Q1 | **Specified the first UMTS 3G networks**, incorporating a CDMA air interface. |
| [Release 4](http://www.3gpp.org/release-4) | 2001 Q2 | Originally called the **Release 2000**, added features including an **all-IP Core Network**, **TD-SCDMA** (UTRA-TDD 1.28 Mchip/s Low Chip Rate (LCR)). |
| [Release 5](http://www.3gpp.org/release-5) | 2002 Q1 | Introduced **IMS**, **HSDPA**, **IPv6** (IP transport in UTRAN). |
| [Release 6](http://www.3gpp.org/release-6) | 2004 Q4 | Integrated operation with **Wireless LAN** networks, adds **HSUPA**, **MBMS** (Multimedia Broadcast and Multicast), enhancements to **IMS** such as Push to Talk over Cellular (**PoC**), **GAN**. |
| [Release 7](http://www.3gpp.org/release-7) | 2007 Q4 | Focuses on decreasing latency, improvements to QoS and real-time applications such as VoIP. This specification also focus on **HSPA+** (High Speed Packet Access Evolution), SIM high-speed protocol and contactless front-end interface (Near Field Communication (NFC) enabling operators to deliver contactless services like Mobile Payments), **EDGE Evolution**. |
| [**Release 8**](http://www.3gpp.org/release-8) | 2008 Q4 | **First LTE release**. All-IP Network (SAE). New **OFDMA**, **FDE** and **MIMO** based radio interface, not backwards compatible with previous CDMA interfaces. **DC-HSDPA** (Dual-Cell HSDPA). **UMTS HNB**. |
| [Release 9](http://www.3gpp.org/release-9) | 2009 Q4 | SAES Enhancements, WiMAX and LTE/UMTS Interoperability. **Dual-Cell HSDPA** (DC-HSDPA) with MIMO, **DC-HSUPA** (Dual-Cell HSUPA). **LTE HeNB**. |
| [**Release 10**](http://www.3gpp.org/release-10) | 2011 Q1 | **LTE Advanced fulfilling IMT-Advanced (4G) requirements**. Backwards compatible with release 8 (LTE). **Multi-Cell HSDPA** (4 carriers). |
| [Release 11](http://www.3gpp.org/release-11) | 2012 Q3 | Advanced IP Interconnection of Services. Service layer interconnection between national operators/carriers as well as third party application providers. Heterogeneous networks (HetNet) improvements, Coordinated Multi-Point operation (CoMP). In-device Co-existence (IDC). |
| [Release 12](http://www.3gpp.org/release-12) | 2015 Q1 | **Enhanced Small Cells** (higher order modulation, dual connectivity, cell discovery, self configuration), **Carrier Aggregation** (2 uplink carriers, 3 downlink carriers, FDD/TDD carrier aggregation), **MIMO** (3D channel modeling, elevation beamforming, massive MIMO), **New and Enhanced Services** (cost and range of MTC, D2D communication, eMBMS enhancements). |
| [Release 13](http://www.3gpp.org/release-13) | 2016 Q1 | LTE in unlicensed, LTE enhancements for Machine-Type Communication. Elevation Beamforming / Full-Dimension MIMO, Indoor positioning. |
| [Release 14](http://www.3gpp.org/release-14) | Planned for June 2017 | Energy Efficiency, Location Services (LCS), Mission Critical Data over LTE, Mission Critical Video over LTE, Flexible Mobile Service Steering (FMSS), Multimedia Broadcast Supplement for Public Warning System (MBSP), enhancement for TV service, massive Internet of Things, Cell Broadcast Service (CBS) |
| [Release 15](http://www.3gpp.org/release-15) | 2018 Q3 | Support for 5G Vehicle-to-x service,IP Multimedia Core Network Subsystem (IMS), Future Railway Mobile Communication System |

<p/>

Each release incorporates hundreds of individual standards documents, each of which may have been through many revisions. Current 3GPP standards incorporate the latest revision of the GSM standards.

The documents are available freely on [3GPP's Web site](http://www.3gpp.org/ftp/specs/latest/). While 3GPP standards can be bewildering to the newcomer, they are remarkably complete and detailed, and provide insight into how the cellular industry works. They cover not only the radio part (Air Interface) and Core Network, but also billing information and speech coding down to source code level. Cryptographic aspects (authentication, confidentiality) are also specified in detail. 3GPP2 offers similar information about its system.

## Specification Numbering

All 3GPP specifications have a specification number consisting of 4 or 5 digits. (e.g. 09.02 or 29.002). The first two digits define the series, followed by 2 further digits for the 01 to 13 series or 3 further digits for the 21 to 55 series.

The full title, specification number and latest version number for every specification can be found in the [3GPP Specification Status Report](http://www.3gpp.org/ftp/Specs/html-info/status-report.htm).

The [3GPP Specification Release Version Matrix](http://www.3gpp.org/ftp/Specs/html-info/SpecReleaseMatrix.htm) shows the versions which exist in each Release of the 3GPP specifications.

The following table is got from [Specification Numbering](http://www.3gpp.org/specifications/79-specification-numbering):

| Subject of specification series | 3G and beyond / GSM (R99 and later) (0) | GSM only (R4 and later) | GSM only (before R4) |
| :------------------------------ | :-------------------------------------: | :---------------------: | :------------------: |
| General information (long defunct) | | | [00 series](http://www.3gpp.org/ftp/Specs/html-info/00-series.htm) |
| Requirements | [21 series](http://www.3gpp.org/ftp/Specs/html-info/21-series.htm) | [41 series](http://www.3gpp.org/ftp/Specs/html-info/41-series.htm) | [01 series](http://www.3gpp.org/ftp/Specs/html-info/01-series.htm) |
| Service aspects (stage 1) | [22 series](http://www.3gpp.org/ftp/Specs/html-info/22-series.htm) | [42 series](http://www.3gpp.org/ftp/Specs/html-info/42-series.htm) | [02 series](http://www.3gpp.org/ftp/Specs/html-info/02-series.htm) |
| Technical realization (stage 2) | [23 series](http://www.3gpp.org/ftp/Specs/html-info/23-series.htm) | [43 series](http://www.3gpp.org/ftp/Specs/html-info/43-series.htm) | [03 series](http://www.3gpp.org/ftp/Specs/html-info/03-series.htm) |
| Signalling protocols (stage 3)<br>- user equipment to network | [24 series](http://www.3gpp.org/ftp/Specs/html-info/24-series.htm) | [44 series](http://www.3gpp.org/ftp/Specs/html-info/44-series.htm) | [04 series](http://www.3gpp.org/ftp/Specs/html-info/04-series.htm) |
| Radio aspects | [25 series](http://www.3gpp.org/ftp/Specs/html-info/25-series.htm) | [45 series](http://www.3gpp.org/ftp/Specs/html-info/45-series.htm) | [05 series](http://www.3gpp.org/ftp/Specs/html-info/05-series.htm) |
| CODECs | [26 series](http://www.3gpp.org/ftp/Specs/html-info/26-series.htm) | [46 series](http://www.3gpp.org/ftp/Specs/html-info/46-series.htm) | [06 series](http://www.3gpp.org/ftp/Specs/html-info/06-series.htm) |
| Data | [27 series](http://www.3gpp.org/ftp/Specs/html-info/27-series.htm) | 47 series (none exists) | [07 series](http://www.3gpp.org/ftp/Specs/html-info/07-series.htm) |
| Signalling protocols (stage 3)<br>- (RSS-CN) and OAM&P and Charging (overflow from 32.- range) | [28 series](http://www.3gpp.org/ftp/Specs/html-info/28-series.htm) | [48 series](http://www.3gpp.org/ftp/Specs/html-info/48-series.htm) | [08 series](http://www.3gpp.org/ftp/Specs/html-info/08-series.htm) |
| Signalling protocols (stage 3)<br>- intra-fixed-network | [29 series](http://www.3gpp.org/ftp/Specs/html-info/29-series.htm) | [49 series](http://www.3gpp.org/ftp/Specs/html-info/49-series.htm) | [09 series](http://www.3gpp.org/ftp/Specs/html-info/09-series.htm) |
| Programme management | [30 series](http://www.3gpp.org/ftp/Specs/html-info/30-series.htm) | [50 series](http://www.3gpp.org/ftp/Specs/html-info/50-series.htm) | [10 series](http://www.3gpp.org/ftp/Specs/html-info/10-series.htm) |
| Subscriber Identity Module (SIM / USIM), IC Cards. Test specs. | [31 series](http://www.3gpp.org/ftp/Specs/html-info/31-series.htm) | [51 series](http://www.3gpp.org/ftp/Specs/html-info/51-series.htm) | [11 series](http://www.3gpp.org/ftp/Specs/html-info/11-series.htm) |
| OAM&P and Charging | [32 series](http://www.3gpp.org/ftp/Specs/html-info/32-series.htm) | [52 series](http://www.3gpp.org/ftp/Specs/html-info/52-series.htm) | [12 series](http://www.3gpp.org/ftp/Specs/html-info/12-series.htm) |
| Access requirements and test specifications | | 13 series (1) | 13 series (1) |
| Security aspects | [33 series](http://www.3gpp.org/ftp/Specs/html-info/33-series.htm) | (2) | (2) |
| UE and (U)SIM test specifications | [34 series](http://www.3gpp.org/ftp/Specs/html-info/34-series.htm) | (2) | [11 series](http://www.3gpp.org/ftp/Specs/html-info/11-series.htm) |
| Security algorithms (3) | [35 series](http://www.3gpp.org/ftp/Specs/html-info/35-series.htm) | [55 series](http://www.3gpp.org/ftp/Specs/html-info/55-series.htm) | (4) |
| LTE (Evolved UTRA), LTE-Advanced, LTE-Advanced Pro radio technology | [**36 series**](http://www.3gpp.org/ftp/Specs/html-info/36-series.htm) | - | - |
| Multiple radio access technology aspects | [37 series](http://www.3gpp.org/ftp/Specs/html-info/37-series.htm) | - | - |
| **Radio technology beyond LTE** | [**38 series**](http://www.3gpp.org/ftp/Specs/html-info/38-series.htm) | - | - |

<p/>

**Note (0)**: 当前仅当第三位数字为零的规范(如TS 23.013)才适用于GSM.

**Note (1)**: The 13 series GSM specifications relate to European-Union-specific regulatory standards. On the closure of ETSI TC SMG, responsibility for these specifications was transferred to ETSI TC MSG (Mobile Specification Group) and they do not appear on the 3GPP file server.

**Note (2)**: The specifications of these aspects are spread throughout several series.

**Note (3)**: Algorithms may be subject to export licensing conditions, see [relevant 3GPP page](http://www.3gpp.org/Confidentiality-Algorithms) and [relevant ETSI pages](http://www.etsi.org/WebSite/OurServices/Algorithms/algorithms.aspx).

**Note (4)**: The original GSM algorithms are not published and are controlled by the [GSM Association](http://www.gsma.com/).

# 3GPP Specs Reading

| Releases | Technology |
| :------: | :--------- |
| R8       | LTE        |
| R10      | LTE-Advanced |
| R15      | 5G New Radio (5GNR) |

<p/>

## RF Performance

3GPP TRs related to RF performance:

* **TR 45.050** - Background for Radio Frequency (RF) requirements
* **TR 25.942** - UTRA RF system scenario
* **TR 36.942** - E-UTRA RF system scenario
* **TR 37.802** - Multi-standard radio Base Station (BS) Radio Frequency (RF) requirements for non-contiguous spectrum deployments
* **TR 37.812** - Radio Frequency (RF) requirements for Multi-band and Multi-standard radio (MB-MSR) Base Station (BS)
* **TR 37.843** - Radio Frequency (RF) requirement background for Active Antenna System (AAS) Base Station (BS) radiated requirements
* **TR 37.900** - Radio Frequency (RF) requirements for Multicarrier and Multiple Radio Access Technology (Multi-RAT) Base Station (BS)

Also refer to document *RF_Performance/RF_Performance_PA2.pptx*.

# References

* [3rd Generation Partnership Project (3GPP)](http://www.3gpp.org/)
* [Demystifying 3GPP](/docs/Demystifying_3GPP.pdf)
* [Understanding 3GPP - starting with the basics](https://www.qualcomm.com/news/onq/2017/08/02/understanding-3gpp-starting-basics) ([local pdf](/docs/Understanding_3GPP.pdf))
* [Top 5 drawbacks of "contribution counting" in 3GPP](https://www.qualcomm.com/news/onq/2017/08/02/top-5-drawbacks-contribution-counting-3gpp-dont-count-it) ([local pdf](/docs/Top_5_drawbacks_of_contribution_counting_in_3GPP.pdf))
* [How to lead the evolution and expansion of the 3GPP ecosystem](https://www.qualcomm.com/news/onq/2017/08/02/how-lead-evolution-and-expansion-3gpp-ecosystem) ([local pdf](/docs/How_to_lead_the_evolution_and_expansion_of_the_3GPP_ecosystem.pdf))

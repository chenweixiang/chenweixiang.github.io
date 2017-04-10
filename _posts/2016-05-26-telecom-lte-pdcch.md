---
layout: post
title: "LTE: Physical Downlink Control CHannel (PDCCH)"
tag: Telecommunication
toc: true
---

This article introduces the Physical Downlink Control CHannel (PDCCH).

<!--more-->

# Flow Diagram of PDCCH

![R8_TS36.211_S6.8_PDCCH](/assets/R8_TS36.211_S6.8_PDCCH.png)

# Downlink Control Information (DCI)

Refer to **TS 36.212 S5.3.3.1**.

A DCI transports downlink or uplink scheduling information, or uplink power control commands for one RNTI. The RNTI is implicitly encoded in the CRC, refer to [CRC Attachment](#crc-attachment).

## DCI Formats

* **DCI Format 0**

    * Uplink
    * 上行共享信道
    * Function: 用于上行 PUSCH 的调度
    * Specs: TS 36.213 Table 8-3, 8-5, 8-6
    <p/>

* **DCI Format 1**

    * Downlink
    * 单码字
    * Function: 用于下行单码字 PDSCH 的调度
    * Transmission Mode: 1, 2, 7
    * Specs: TS 36.213 Table 7.1-5, 7.1-6
    <p/>

* **DCI Format 1A**

    * Downlink
    * 单码字
    * Function: 用于下行单码字 PDSCH 和随机接入流程的紧凑型调度
    * Transmission Mode: All TM, SI-RNTI, P-RNTI, RA-RNTI
    * Specs: TS 36.213 Table 7.1-1, 7.1-2, 7.1-3, 7.1-5, 7.1-6, 7.1-7, 8-4
    <p/>

* **DCI Format 1B**

    * Downlink
    * 单码字
    * Function: 用于预编码的下行单码字 PDSCH 的紧凑型调度
    * Transmission Mode: 6
    * Specs: TS 36.213 Table 7.1-5
    <p/>

* **DCI Format 1C**

    * Downlink
    * 单码字
    * Function: 用于下行单码字 PDSCH 的更紧凑模型调度
    * Transmission Mode: SI-RNTI, P-RNTI, RARNTI
    * Specs: TS 36.213 Table 7.1-1, 7.1-2, 7.1-3
    <p/>

* **DCI Format 1D**

    * Downlink
    * 单码字
    * Function: 用于具有预编码与功率偏移信息的下行单码字 PDSCH 的紧凑型调度
    * Transmission Mode: 5
    * Specs: TS 36.213 Table 7.1-5
    <p/>

* **DCI Format 2**

    * Downlink
    * 双码字
    * Function: 用于闭环空间复用情况下的双码字 PDSCH 的调度
    * Transmission Mode: 4
    * Specs: TS 36.213 Table 7.1-5, 7.1-6
    <p/>

* **DCI Format 2A**

    * Downlink
    * 双码字
    * Function: 用于开环空间复用情况下的双码字 PDSCH 的调度
    * Transmission Mode: 3
    * Specs: TS 36.213 Table 7.1-5, 7.1-6
    <p/>

* **DCI Format 2B**

    * Downlink
    * 双码字
    * Function: 用于双层的双码字 PDSCH 的调度
    * Transmission Mode: 8
    * Specs: Rel 9 TS 36.213 Table 7.1-5, 7.1-6
    <p/>

* **DCI Format 3**

    * Uplink
    * 功率控制信息
    * Function: 用于传输一组用户的 PUCCH 和 PUSCH 的功率控制信息，其中功率控制信息采用 2 比特指示
    * Specs: TS 36.213 Table 8-7, 8-8
    <p/>

* **DCI Format 3A**

    * Uplink
    * 功率控制信息
    * Function: 用于传输一组用户的 PUCCH 和 PUSCH 的功率控制信息，其中功率控制信息采用 1 比特指示
    * Specs: TS 36.213 Table 8-7, 8-8
    <p/>

## DCI Length before CRC Attachment

According to **TS 36.212 SS5.3.3.1**, the length of DCI formats before CRC attachment are shown in the following table:

![DCI_length_before_CRC_attachment](/assets/DCI_length_before_CRC_attachment.png)

NOTE1：上表中 DCI format 1C 行中存在两个长度值（在某些系统带宽下） ，这是根据 $$N_{gap}$$ 区分的，前者为 $$N_{gap} = N_{gap,1}$$，后者为 $$N_{gap} = N_{gap,2}$$；

NOTE2：上表中 DCI format 1B/1D 行中存在两个长度值，这是根据基站天线数的不同进行区分的，参见 TS 36.212 Table 5.3.3.1.3A-2, Table 5.3.3.1.4A-1，前者为 AP=2，后者为 AP=4；

NOTE3：上表中 DCI format 2/2A 行中存在两个长度值，这是根据基站天线数的不同（基站天线数不同，则对应的 Precoding information 域的宽度不同） 进行区分的，参见 TS 36.212 Table 5.3.3.1.5-3, Table 5.3.3.1.5A-1，前者为 AP=2，后者为 AP=4。

NOTE4：由上表可知， DCI format 1B/1D 的长度相等。

NOTE5：上表中 DCI format 2B 行中存在两个长度值，这是根据传输的 TB 块的数目不同进行区分的，前者为 1 TB，后者为 2 TBs。

# CRC Attachment

The CRC parity bits are 16 bits. The CRC parity bits may be scrambled with *Antenna selection mask* (refer to **TS 36.212 Table 5.3.3.2-1**) and *corresponding RNTI* (refer to **TS 36.212 S5.3.3.1**) if UE transmit antenna selection is configured and applicable, refer to **TS 36.212 S5.3.3.2**, **TS 36.213 S8.7** and the following configuration from higher layer:

```
PhysicalConfigDedicated
-> antennaInfo
   -> explicitValue     AntennaInfoDedicated
      -> ue-TransmitAntennaSelection
         -> setup ENUMERATED {closedLoop, openLoop}
```

# Channel Coding

The coding scheme for DCI is *Tail biting convolutional coding* with *1/3 coding rate*, refer to **TS 36.212 S5.3.3.3**.

# Rate Matching

Refer to **TS 36.212 S5.3.3.4**.

# Multiplexing and Scrambling

Refer to **TS 36.211 S6.8.2**.

# Modulation

Modulation scheme for PDCCH is **QPSK**, refer to **TS 36.211 S6.8.3**.

# Layer Mapping and Precoding

Refer to **TS 36.211 S6.8.4**.

# Mapping to REs

Refer to **TS 36.211 S6.8.5**.

Also refer to the following sheets in **R8_TS36.XXX_LTE_PHY_Parameters_v2.xlsx**:

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

* TS 36.213 E-UTRA - Physical layer procedures, section 8.7 UE Transmit Antenna Selection
* TS 36.212 E-UTRA - Multiplexing and channel coding, section 5.3.3 Downlink control information
* TS 36.211 E-UTRA - Physical Channels and Modulation, section 6.8 Physical downlink control channel
* [ShareTechnote](http://www.sharetechnote.com/)
* [3GLTEinfo](http://www.3glteinfo.com/)

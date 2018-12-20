---
layout: post
title: "RF Performance"
tag: Telecom
toc: true
---

This article introduce the RF characteristic of a radio unit.

<!--more-->

# Signal-to-Noise Ratio (SNR)

* [Signal-to-Noise Ratio (SNR)](https://en.wikipedia.org/wiki/Signal-to-noise_ratio)

# Error Vector Magnitude (EVM)

Error Vector Magnitude (EVM) is a measure used to quantify the performance of a digital radio transmitter or receiver. A signal sent by an ideal transmitter or received by a receiver would have all constellation points precisely at the ideal locations, however various imperfections in the implementation (such as carrier leakage, low image rejection ratio, phase noise etc.) cause the actual constellation points to deviate from the ideal locations. Informally, EVM is a measure of how far the points are from the ideal locations.

Noise, distortion, spurious signals, and phase noise all degrade EVM, and therefore EVM provides a comprehensive measure of the quality of the radio receiver or transmitter for use in digital communications. Transmitter EVM can be measured by specialized equipment, which demodulates the received signal in a similar way to how a real radio demodulator does it. One of the stages in a typical phase-shift keying demodulation process produces a stream of I-Q points which can be used as a reasonably reliable estimate for the ideal transmitted signal in EVM calculation.

## Definition of EVM

![Constellation Diagram and EVM](/assets/QAM_mit_EVM.png)

An error vector is a vector in the I-Q plane between the ideal constellation point and the point received by the receiver. In other words, it is the difference between actual received symbols and ideal symbols. The average amplitude of the error vector, normalized to peak signal amplitude, is the EVM. For the percentage format, [Root Mean Square (RMS)](https://en.wikipedia.org/wiki/Root_mean_square) average is used.

The Error Vector Magnitude (EVM) is equal to the ratio of the amplitude of the error vector to the [Root Mean Square (RMS)](https://en.wikipedia.org/wiki/Root_mean_square) amplitude of the reference. It is defined in dB as:

$$EVM(dB) = 20 ∙ log_{10} (\frac {P_{error}} {P_{reference}})$$

where $$P_{error}$$ is the RMS amplitude of the error vector. For single carrier modulations, $$P_{reference}$$ is, by convention, the amplitude of the outermost (highest power) point in the reference signal constellation. More recently, for multi-carrier modulations, $$P_{reference}$$ is defined as the reference constellation average power.

EVM is defined as a percentage in a compatible way:

$$EVM(\%) = \sqrt{\frac {P_{error}} {P_{reference}}} × 100\%$$

with the same definitions.

EVM, as conventionally defined for single carrier modulations, is a ratio of a mean amplitude to a peak amplitude. Because the relationship between the peak and mean signal power is dependent on constellation geometry, different constellation types (e.g. 16-QAM and 64-QAM), subject to the same mean level of interference, will report different EVM values.

EVM, as defined for multi carrier modulations, is arguably the more satisfactory measurement because it is a ratio of two mean powers and is insensitive to the constellation geometry. In this form, EVM is closely related to Modulation error ratio, the ratio of mean signal power to mean error power.

## Measurement of EVM

* [8 Hints for Making and Interpreting EVM Measurements](/docs/8_Hints_for_Making_and_Interpreting_EVM_Measurements.pdf)
* [EVM Degradation in LTE Systems by RF Filtering](/docs/EVM_Degradation_in_LTE_Systems_by_RF_Filtering.pdf)

# ACLR

# CFR and DPD


# References

* [Signal-to-Noise Ratio (SNR)](https://en.wikipedia.org/wiki/Signal-to-noise_ratio)
* [EVM on Wikipedia](https://en.wikipedia.org/wiki/Error_vector_magnitude)
* [EVM Calculation for Broadband Modulated Signals](/docs/EVM_Calculation_for_Broadband_Modulated_Signals.pdf)

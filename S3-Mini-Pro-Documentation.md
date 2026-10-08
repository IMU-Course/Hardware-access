# IMU course
# Embedded Systems with Uli
# WEMOS S3 Mini Pro – Technical Research

**Author:** James Buabeng Inkoom  
**Document Type:** Hardware & Interface Technical Research  
**Platform:** ESP32-S3 / WEMOS S3 Mini Pro  

> A structured technical reference covering the onboard hardware, GPIO mapping, communication interfaces, software-development considerations, verification status, and testing notes for the WEMOS S3 Mini Pro.

---

## Device List and Hardware Connections

## 1. Introduction

This document provides a comprehensive hardware and interface analysis of the WEMOS S3 Mini Pro development board. The S3 Mini Pro is a compact, feature-rich microcontroller board based on the ESP32-S3 System-on-Chip (SoC), which offers Wi-Fi and Bluetooth LE connectivity alongside a wide array of integrated peripherals. The primary purpose of this technical research is to document the exact hardware connections between the ESP32-S3 and its onboard devices. By studying the official board schematic, this document establishes a verified reference for firmware and software development, ensuring correct GPIO assignments and communication protocol configurations.

---

## 2. Objectives

The core objectives of this technical research are to:

* Identify all onboard devices and peripherals.
* Identify their exact GPIO and pin connections to the ESP32-S3.
* Identify the communication protocols and interfaces utilized by each device.
* Understand the board's hardware architecture and power routing.
* Verify all peripheral connections using the official board schematic.
* Provide a reliable, GitHub-ready reference for future software development.

---

## 3. S3 Mini Pro Board Overview

The S3 Mini Pro is designed for IoT applications, embedded interfaces, and sensor data acquisition. It leverages the ESP32-S3's dual-core architecture and extensive IO multiplexing capabilities. The board integrates visual feedback mechanisms (TFT display, RGB LED), environmental/motion sensing (6-DoF IMU), optical transmission (IR LED), and user inputs (tactile switches) into a single compact footprint.

[Insert S3 Mini Pro board image here]

Major onboard components include the ST7789-driven TFT display for graphical output, a QMI8658C IMU for motion tracking, and standard user interface elements necessary for standalone operation.

---

# 4. Complete Device and Peripheral List

The following table catalogs the onboard devices identified based on available schematic data and board documentation.

| No. | Device/Component | Part/Model | Function | Interface/Protocol | ESP32-S3 GPIO/Pin(s) |
| --- | --- | --- | --- | --- | --- |
| 1 | TFT Display | 0.85-inch LCD | Visual Output | SPI + GPIO | 34, 35, 36, [Not verified from the available schematic] |
| 2 | Display Controller | ST7789 | Drives TFT pixels | SPI | SCK/MOSI: [Not verified from the available schematic] |
| 3 | RGB LED | WS2812B | Status/Visual Output | Single-wire Digital | 8 (Data), 7 (Power Control) |
| 4 | Infrared Transmitter | IR LED | IR Signal Transmission | PWM / Digital GPIO | 9 |
| 5 | 6-Axis IMU | QMI8658C | Accel/Gyro Sensing | I2C | SDA/SCL: [Not verified from the available schematic] |
| 6 | User Button (Left) / BOOT | Tactile Switch | Boot Mode / User Input | Digital GPIO | 0 |
| 7 | User Button (Center) | Tactile Switch | User Input | Digital GPIO | 47 |
| 8 | User Button (Right) | Tactile Switch | User Input | Digital GPIO | 48 |
| 9 | Hardware Reset | Tactile Switch | System Reset | Hardware EN/RST line | EN (CHIP_PU) |

---

# 5. Master GPIO and Hardware Connection Table

The exact connections routing the ESP32-S3 to the onboard peripherals are detailed below.

| Device | Device Pin/Signal | ESP32-S3 GPIO | Direction | Interface | Function | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| ST7789 TFT | CS (Chip Select) | 35 | Output | SPI Control | Selects display on SPI bus | Active Low |
| ST7789 TFT | DC (Data/Command) | 36 | Output | SPI Control | Toggles data vs command |  |
| ST7789 TFT | RST (Reset) | 34 | Output | GPIO Control | Hardware reset for screen | Active Low |
| ST7789 TFT | SCK (Serial Clock) | Not verified from the available schematic | Output | SPI | Clock signal for TFT |  |
| ST7789 TFT | MOSI (Serial Data) | Not verified from the available schematic | Output | SPI | Data output to TFT |  |
| QMI8658C | SDA (Serial Data) | Not verified from the available schematic | In/Out | I2C | IMU Data line | Requires pull-up |
| QMI8658C | SCL (Serial Clock) | Not verified from the available schematic | Output | I2C | IMU Clock line | Requires pull-up |
| WS2812B | DIN (Data In) | 8 | Output | Single-wire | Addressable LED data |  |
| WS2812B | Power Control | 7 | Output | GPIO Control | LED Power switching | If applicable to board revision |
| IR LED | Anode/Control | 9 | Output | PWM / GPIO | Drives IR diode | Often uses transistor driver |
| Left Switch | Signal | 0 | Input | GPIO | Boot mode & User input | Active Low (Pull-up) |
| Center Switch | Signal | 47 | Input | GPIO | User input | Active Low (Pull-up) |
| Right Switch | Signal | 48 | Input | GPIO | User input | Active Low (Pull-up) |

---

# 6. Communication Interfaces

## 6.1 I2C

I2C (Inter-Integrated Circuit) is a synchronous, multi-master, multi-slave packet-switched, single-ended, serial communication bus. It utilizes two distinct lines: Serial Data (SDA) and Serial Clock (SCL). On the S3 Mini Pro, the I2C bus is primarily utilized for sensor communication.

| Device | SDA | SCL | I2C Address | Function |
| --- | --- | --- | --- | --- |
| QMI8658C IMU | Not verified from the available schematic | Not verified from the available schematic | Not verified from the available schematic | Accelerometer and Gyroscope data |

---

## 6.2 SPI

SPI (Serial Peripheral Interface) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems. It uses dedicated clock (SCK), data (MOSI, MISO), and chip select (CS) lines.

The ST7789 TFT relies on a unidirectional SPI implementation (MOSI only, no MISO needed for writing to the display) alongside additional control pins.

| Signal | ESP32-S3 GPIO | Function |
| --- | --- | --- |
| SCK | Not verified from the available schematic | SPI Clock |
| MOSI | Not verified from the available schematic | SPI Master Out Slave In (Data to Display) |
| CS | 35 | Chip Select (Active Low) |
| DC | 36 | Data/Command Toggle |

---

## 6.3 GPIO

General-Purpose Input/Output (GPIO) pins are used for digital signals that do not require complex protocols. On this board, GPIOs control the TFT Reset line, read the state of the three tactile switches (Left, Center, Right), and provide the high-speed bit-banged or RMT-driven timing sequence for the WS2812B RGB LED.

---

## 6.4 UART

No onboard peripheral was identified that communicates exclusively over a dedicated internal UART interface. The ESP32-S3's primary UART (UART0) is typically routed to the USB-to-Serial converter or native USB for programming and serial console output.

---

## 6.5 PWM

Pulse Width Modulation (PWM) is heavily utilized for the IR LED to generate the specific carrier frequencies (e.g., 38kHz) required for infrared remote control transmission. The ESP32-S3 LEDC (LED Control) hardware peripheral is ideal for driving GPIO 9 for this purpose. It can also be used to dim the TFT backlight if the backlight pin is exposed.

---

## 6.6 Other Interfaces

* **Single-Wire Digital:** The WS2812B uses a proprietary timing-specific, single-wire protocol to transmit 24-bit RGB color data. The ESP32-S3 handles this using the RMT (Remote Control Transceiver) peripheral or I2S.

---

# 7. Detailed Device Documentation

## 7.1 0.85-inch TFT / ST7789

### Overview

The board features a compact 0.85-inch, 128x128 pixel resolution color TFT display driven by the ST7789 controller. It is used for rendering text, graphical user interfaces, and telemetry data.

### Technical Information

| Parameter | Details |
| --- | --- |
| Device | 0.85-inch TFT LCD |
| Part number | ST7789 (Controller) |
| Function | Graphical Output |
| Interface | 4-Wire SPI |
| Supply voltage | 3.3V |

### Hardware Connections

| Device Signal | ESP32-S3 GPIO | Purpose |
| --- | --- | --- |
| CS | 35 | Enables SPI communication |
| DC | 36 | Differentiates pixel data from controller commands |
| RST | 34 | Hardware reset for initialization |
| SCK | Not verified from the available schematic | Clock |
| MOSI | Not verified from the available schematic | Data |

### Communication

The ESP32-S3 communicates with the ST7789 via hardware SPI. The ESP32-S3 must assert CS low, set DC to the appropriate state (Low for commands, High for data), and clock data out over MOSI.

### Schematic Observation

The display control pins (34, 35, 36) are assigned to standard GPIOs, while the SPI bus routing requires confirmation against the final hardware schematic to ensure optimal SPI host selection.

---

## 7.2 WS2812B RGB LED

### Overview

A digitally addressable RGB LED capable of displaying 16 million colors. Used for system status indication and visual debugging.

### Technical Information

| Parameter | Details |
| --- | --- |
| Device | Addressable RGB LED |
| Part number | WS2812B |
| Function | Status Indication |
| Interface | Single-wire digital |

### Hardware Connections

| Device Signal | ESP32-S3 GPIO | Purpose |
| --- | --- | --- |
| DIN | 8 | Receives color data payload |
| Power Enable | 7 | Controls VCC to the LED |

### Communication

The WS2812B does not use standard I2C or SPI. It requires a precisely timed continuous data stream. The ESP32-S3 typically uses the built-in `neopixel` library (which wraps the RMT peripheral) to handle this strict microsecond timing.

### Schematic Observation

Data is routed directly from GPIO 8 to the DIN pin of the LED.

---

## 7.3 QMI8658C 6-Axis IMU

### Overview

An Inertial Measurement Unit combining a 3-axis accelerometer and a 3-axis gyroscope. Used for step counting, orientation detection, and motion-based interactions.

### Technical Information

| Parameter | Details |
| --- | --- |
| Device | 6-DoF IMU |
| Part number | QMI8658C |
| Function | Motion Tracking |
| Interface | I2C |

### Hardware Connections

| Device Signal | ESP32-S3 GPIO | Purpose |
| --- | --- | --- |
| SDA | Not verified from the available schematic | I2C Data |
| SCL | Not verified from the available schematic | I2C Clock |

### Communication

The IMU acts as an I2C slave device. The ESP32-S3 requests and reads registers containing the latest accelerometer and gyroscope X, Y, and Z-axis values.

### Schematic Observation

Connected to the common I2C bus. Pull-up resistors must be present on the SDA and SCL lines.

---

## 7.4 IR LED

### Overview

An infrared emitting diode utilized for sending remote control signals to external appliances (e.g., TVs, air conditioners).

### Hardware Connections

| Device Signal | ESP32-S3 GPIO | Purpose |
| --- | --- | --- |
| Anode / Driver | 9 | Modulates the IR beam |

### Communication

The ESP32-S3 uses PWM to pulse GPIO 9 at a specific carrier frequency (usually 38 kHz). Data is encoded by turning this PWM signal on and off for specific durations.

---

## 7.5 RESET Button

### Overview

A tactile button used to manually hard-reset the microcontroller.

### Hardware Connections

It is mechanically connected between the ESP32-S3's `EN` (Enable / CHIP_PU) pin and Ground. Pulling `EN` low restarts the SoC. This does not consume a standard programmable GPIO.

---

## 7.6 BOOT Button / User Button (Left)

### Overview

Serves a dual purpose. Held down during power-up or reset, it pulls GPIO 0 low, placing the ESP32-S3 into UART Download/Bootloader mode for flashing firmware. During normal operation, it acts as a standard user input.

### Hardware Connections

Connected to GPIO 0. It is active-low and requires an internal or external pull-up resistor.

---

## 7.7 USER Button(s) (Center and Right)

### Overview

Standard tactile inputs for user interaction, menu navigation, or triggering interrupts.

### Hardware Connections

* **Center Button:** Connected to GPIO 47.
* **Right Button:** Connected to GPIO 48.

Both act as active-low inputs. When pressed, the GPIO is pulled to Ground.

---

# 8. Schematic Analysis

Analysis of the ESP32-S3 multiplexing indicates a separation of high-speed and low-speed buses. The SPI bus is dedicated to the ST7789 display to ensure high framerates without contention, while the I2C bus manages the QMI8658C IMU.

[Insert relevant S3 Mini Pro schematic image here]

**Hardware Block Diagram:**

```text
ESP32-S3
│
├── SPI (SCK, MOSI) ───────────────> ST7789 TFT Display
├── GPIO 34, 35, 36  ──────────────> TFT Control (RST, CS, DC)
│
├── I2C (SDA, SCL)   ──────────────> QMI8658C 6-Axis IMU
│
├── GPIO 8 (Data), 7 (Pwr) ────────> WS2812B RGB LED
│
├── GPIO 9 (PWM)     ──────────────> IR Transmitter LED
│
├── GPIO 0           ──────────────> Left Button / BOOT
├── GPIO 47          ──────────────> Center Button
└── GPIO 48          ──────────────> Right Button

```

---

# 9. Device-to-Protocol Summary

| Device | Communication Method | Main GPIO(s) | Purpose |
| --- | --- | --- | --- |
| ST7789 TFT | SPI | CS:35, DC:36, RST:34 | Visual Output |
| QMI8658C IMU | I2C | Not verified from the available schematic | Motion Tracking |
| WS2812B | Single-wire | 8 | RGB Indicator |
| IR LED | PWM | 9 | IR Transmission |
| Switches | Digital GPIO | 0, 47, 48 | User Input |

---

# 10. GPIO Usage Summary

| ESP32-S3 GPIO | Connected Device | Signal | Interface | Purpose |
| --- | --- | --- | --- | --- |
| 0 | Left Button | Signal | GPIO In | User Input / Boot Mode |
| 7 | WS2812B | Power | GPIO Out | LED Power Enable |
| 8 | WS2812B | DIN | Single-wire | Addressable LED Data |
| 9 | IR LED | Control | PWM Out | Infrared Modulation |
| 34 | ST7789 TFT | RST | GPIO Out | Display Hardware Reset |
| 35 | ST7789 TFT | CS | GPIO Out | Display Chip Select |
| 36 | ST7789 TFT | DC | GPIO Out | Display Data/Command Toggle |
| 47 | Center Button | Signal | GPIO In | User Input |
| 48 | Right Button | Signal | GPIO In | User Input |

---

# 11. Hardware Design Observations

* **Active-Low Logic:** The user buttons (GPIO 0, 47, 48) utilize active-low logic. They pull the pins to ground when pressed, meaning software must configure internal pull-up resistors and trigger actions on a falling edge.
* **TFT Reset Isolation:** Supplying a dedicated GPIO (34) for the TFT reset line allows the software to reinitialize the screen independently of an ESP32-S3 hard reset.
* **Power Management:** GPIO 7 acts as a power gate for the WS2812B, preventing idle current draw when the LED is supposed to be fully off.

---

# 12. Software Development Considerations

When developing MicroPython or C/C++ firmware for the S3 Mini Pro, the hardware topology imposes the following constraints:

* **Switch Bouncing:** The tactile switches on GPIO 0, 47, and 48 will experience mechanical bouncing. Software debouncing algorithms (using interrupts with timestamp checks or timer callbacks) must be implemented.
* **Shared Display Memory:** When initializing the ST7789 in MicroPython, ensure external files (like fonts and graphics) are uploaded to the Virtual File System (VFS) beforehand, as the display drivers pull assets directly from flash memory.
* **Pin Safety:** Avoid reconfiguring GPIOs 34, 35, and 36 as inputs, as this will disrupt the state of the TFT display. Avoid reassigning GPIO 9 if the IR LED is populated to prevent accidental infrared flooding.

---

# 13. Verification and Testing

| Device | Hardware Identified | Pins Verified | Communication Verified | Software Tested | Status |
| --- | --- | --- | --- | --- | --- |
| ST7789 TFT | Yes | Partially | Yes | Yes (Exercises) | Tested |
| WS2812B LED | Yes | Partially | Yes | Yes (MicroPython demo) | Tested |
| Switches (3x) | Yes | Yes | Yes | Yes | Tested |
| IR LED | Yes | Yes | Pending | Pending | Not yet tested |
| QMI8658C IMU | Yes | No | Pending | Pending | Not yet tested |

---

# 14. Conclusion

This technical research has mapped the primary hardware architecture of the WEMOS S3 Mini Pro. The board isolates high-speed graphical data via SPI for the ST7789 controller, while managing complex sensor data via I2C for the QMI8658C IMU. Direct GPIO mapping efficiently handles user inputs and optical outputs (WS2812B, IR LED). Missing GPIO data for the SPI and I2C buses requires immediate verification against the physical schematic. This document serves as the foundational hardware reference for upcoming software development and repository documentation.

---

# 15. References

1. Official S3 Mini Pro documentation and board schematic.
2. Espressif ESP32-S3 Series Datasheet.
3. Sitronix ST7789V Datasheet.
4. QST QMI8658C 6-DoF IMU Datasheet.
5. Worldsemi WS2812B Intelligent Control LED Datasheet.
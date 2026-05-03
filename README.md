# 🎡 Wheel of Emotion
## Art - Engineering - Social Experiment

## Overview
An interactive installation exploring emotional contagion.

## Hardware List So Far
* Raspberry Pi Pico 2022
* PN532 NFC Module
* WS2812B 16x16 LED Panel

## Current Progress
- [x] Basic LED "Smile" test
- [x] NFC UID Scanner logic
- [ ] P2P Handshake between two Picos (In Progress)

## How to Run
1. Wire the Pico to the PN532 via I2C (GP4/GP5).
2. Save `src/main.py` to the Pico.
3. Power via 5V PowerBank.

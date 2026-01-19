# Mobility Project (Python + Raspberry Pi Pico)

## What this repository is
This repository contains the files uploaded to a **Raspberry Pi Pico** to run a **Python-based mobility system**.  
The system is designed by breaking mobility functions into **small, well-defined components** and organizing them with **object-oriented programming (OOP)**.

## Design approach (OOP-focused)
- Each mobility function is separated into a **class/module** with a clear responsibility.
- Hardware-related features are treated as **independent components** that can be developed, tested, and replaced without affecting the whole system.
- The project aims to improve **maintainability, readability, and scalability** by using:
  - clear interfaces between components
  - reusable modules
  - structured initialization and control flow

## What gets uploaded to the Pico
- Core Python modules that implement the mobility system structure
- Component-based control logic (organized for extension)
- Configuration and entry-point files needed to run the project on-device

## Outcome
A clean baseline for a mobility platform where functionality is modularized through OOP, making it easy to expand with additional features (e.g., sensors, control logic, safety rules) without rewriting the entire codebase.

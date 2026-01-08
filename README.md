# Gelos Enterprises: User Authentication & Security Management System

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Security Focus](https://img.shields.io/badge/Security-Blacklist--Protected-red)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Project Overview
This project represents a major milestone in my **career transition into Software Development**. It was developed as a core component of the **ICT30120 Certificate III in Information Technology at TAFE NSW**.

The system is a professional-grade solution for user identity management, designed for the **Gelos Enterprises business framework**. It goes beyond basic classroom exercises by implementing a security-first architecture for user authentication, account auditing, and unauthorized access prevention.

## 🚀 Functional Modules

Instead of a single-purpose script, this system is divided into three enterprise-ready functional modules, ensuring a professional user experience without the need for a GUI.

### 1. Advanced User Registration Module
* **Uniqueness Validation:** Implements a lookup algorithm to ensure no duplicate usernames exist in the global registry.
* **Security Enforcement:** Enforces strict password policies (8+ characters) to align with enterprise security standards.
* **Auto-Persistence:** Instantly synchronizes new user data with the `accounts.txt` database.

### 2. Multi-Tier Authentication & Security Gatekeeping
* **Blacklist Pre-Screening:** Prior to credential entry, the system cross-references the `lockUserList.txt` to prevent unauthorized access from compromised accounts.
* **Three-Factor Match:** Validates user existence, password accuracy, and account status simultaneously.
* **Error Resilience:** Handles empty inputs and invalid characters gracefully to prevent runtime crashes.

### 3. Administrative Audit & Data Retrieval
* **Privileged Access:** A restricted module for administrators to perform system-wide auditing.
* **Formatted Data Display:** Extracts raw data from text-based repositories into a structured console format with multi-dimensional sorting logic.

## 💻 System Interaction Preview
This snippet demonstrates the core workflow: **Authentication > Secure Access > Data Sorting**.

```shell
Welcome to Gelos Enterprises User Management System!

    Gelos Enterprises User Management System
    ========================================
                   Options
                   =======
            1. Register a new user
            2. View accounts
            3. Exit

Enter your option please [1, 2, or 3]: 2

Displaying Registered Users
---------------------------
[System: Access Restricted. Identity Verification Required.]

Please enter your username: fredsmart1
Please enter your password: **********

[SUCCESS] You have successfully logged in.

Would you like to view users sorted?
------------------------------------------------------------------------
1. By registration date (earliest first)
2. By registration date (latest first)
3. By username (A-Z)
4. By username (Z-A)

Enter your option please [1, 2, 3, or 4]: 3

All registered user accounts are listed below sorted by username (A-Z):
1. bob101
2. fredsmart1
3. jrobertson4
...
8. sbj2021

Total users = 8
[System: Press <Enter> to Return to Menu]
```

## 💻 System Logic & Performance

### 🛡️ Core Workflow (Logic Flow)
The application follows a secure execution path to ensure data integrity:
1. **Status Verification**: Interrogates the Lockout Registry (`lockUserList.txt`) before initiating the login sequence.
2. **Identity Authentication**: Performs high-precision matching against the encrypted-style `accounts.txt` database.
3. **Session Management**: Grants access to the privileged menu and handles multi-dimensional data requests.

### 🧠 Logic Behind the Screen
Beyond the basic flow, the system implements several "invisible" engineering features:
* **Pre-emptive Gatekeeping**: By validating account status **before** asking for a password, the system effectively mitigates brute-force risks.
* **Algorithm-Based Sorting**: Leverages Python's `sort()` methods and `lambda` functions to handle complex data presentation (A-Z, Date sorting).
* **Input Sanitization**: The system is built to be "crash-proof." Any unexpected user input is caught by validation logic, ensuring continuous uptime and a robust user experience.

## 📐 Design & Methodology (SDLC)
Following standard Software Development Life Cycle (SDLC) practices, I developed a logical blueprint before moving into the implementation phase. This ensured that complex edge cases, such as account lockouts and empty inputs, were handled gracefully.

* **[View Original Pseudocode (Initial Design Phase)](https://github.com/Tina-YingWang-AU/tafe-it-portfolio/blob/main/01-Certificate-III-IT/02-Software-Design-and-Development/design_docs/pseudocode_login_system.md)**
  * *Note: This document tracks the foundational logic that evolved into the current robust system.*

## 📂 System Architecture
The project follows a **Modular Design** pattern to separate concerns:
* **GelosLoginApplication.py**: The **Orchestration Layer** (Entry Point). 
* **GelosLibraries.py**: The **Core Logic Engine** (Registration, Login, View).
* **Data Layer**: Includes `accounts.txt` and `lockUserList.txt`.

## 🚀 Quick Start
1. **Clone the repository**:
   `git clone https://github.com/Tina-YingWang-AU/User-Auth-System-Python.git`
2. **Navigate to the folder**:
   `cd User-Auth-System-Python`
3. **Run the application**:
   `python GelosLoginApplication.py`

## 🚀 Learning & Growth Path
As a **career changer**, this project was instrumental in mastering:
* **Engineering Mindset**: Breaking down business scenarios into functional modules.
* **Clean Code Practices**: Transitioning to a structured **UDF (User Defined Functions)** approach.
* **Problem Solving**: Implementing security layers to handle edge cases.

---
**Institutional Context:** TAFE NSW (ICT30120-01V02 Certificate III in Information Technology)  
**Author:** [Tina Ying Wang](https://github.com/Tina-YingWang-AU)

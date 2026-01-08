# Gelos Enterprises: User Authentication & Security Management System

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Security Focus](https://img.shields.io/badge/Security-Blacklist--Protected-red)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Project Overview
This project represents a major milestone in my **career transition into Software Development**. It was developed as a core component of the **ICT30120 Certificate III in Information Technology at TAFE NSW**.

The system is a professional-grade solution for user identity management, designed for the **Gelos Enterprises business framework**. It goes beyond basic classroom exercises by implementing a security-first architecture for user authentication, account auditing, and unauthorized access prevention.

## 🛠️ Key Technical Features
* **Smart Authentication Logic:**
    * **Pre-login Security Gatekeeping:** The system interrogates `lockUserList.txt` prior to authentication to intercept locked accounts.
    * **Credential Validation:** High-precision matching against the `accounts.txt` data repository.
* **Robust Registration Workflow:**
    * **Data Integrity:** Real-time duplicate username detection to ensure database uniqueness.
    * **Security Standards:** Enforced password complexity policies (e.g., **Minimum 8-character requirement**).
* **Administrative Auditing:** A dedicated administrative module designed for system overseers to list and audit accounts.
* **State Persistence:** Full **File I/O integration** ensures all records are preserved between restarts.

## 📂 System Architecture
The project follows a **Modular Design** pattern to separate concerns:
* **GelosLoginApplication.py**: The **Orchestration Layer** (Entry Point). 
* **GelosLibraries.py**: The **Core Logic Engine** (Registration, Login, View).
* **Data Layer**: Includes `accounts.txt` and `lockUserList.txt`.

## 💻 Logic Flow
1. **Status Verification:** Checks the Lockout Registry first.
2. **Identity Authentication:** Matches credentials against the database.
3. **Session Management:** Provides a seamless UI until secure logout.

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

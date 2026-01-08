# User Authentication & Security Management System

## 🌟 Project Overview
This Python-based system provides a robust solution for user identity management. Developed for **Gelos Enterprises**, the application goes beyond basic CRUD operations by implementing a security-first approach to user authentication and account auditing.

## 🛠️ Key Technical Features
- **Smart Authentication Logic:** - Validates credentials against `accounts.txt`.
  - Implements a **Security Blacklist**: The system checks `lockUserList.txt` *before* allowing login attempts to prevent unauthorized access from locked accounts.
- **Robust Registration Workflow:**
  - **Duplicate Prevention:** Checks if a username already exists to maintain data integrity.
  - **Security Standards:** Enforces a minimum 8-character password policy.
- **Administrative Auditing:** A dedicated administrative view to list and audit all registered users in a clean, numbered format.
- **State Persistence:** Full File I/O integration ensures all user data and lock statuses are preserved between system restarts.

## 📂 System Structure
- `main.py`: The core engine containing the multi-layered authentication logic.
- `accounts.txt`: The primary database for active user credentials.
- `lockUserList.txt`: The security registry for restricted/locked users.

## 💻 How It Works (Logic Flow)
1. **Check Lock Status:** System verifies if the user is in the lockout registry.
2. **Verify Identity:** If not locked, the system matches the username and password.
3. **Session Management:** Provides a continuous menu-driven experience until the user chooses to exit.

---
*This project was completed as part of the **TAFE NSW - ICT30120-01V02 Certificate III in Information Technology (focusing on Programming and Web)**.*

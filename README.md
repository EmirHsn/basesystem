# base user system 
# 🛡️ Admin Panel Management System (Python)

A comprehensive Python-based login and management system developed as part of my programming studies (EPAL Curriculum). This project simulates a real-world admin dashboard with user authentication, database-like list management, and administrative privileges.

---

## 🚀 Key Features
* **Secure Login System:** Validates users against a list with a 3-attempt limit to prevent brute-force entries.
* **Dynamic User Management:**
    * **Show Users:** View a complete list of registered accounts (Admin only).
    * **Add User:** Register new members to the system dynamically.
    * **Delete User:** Remove specific users from the database.
* **Profile Customization:** Every user can change their own username while logged in.
* **Admin Controls:** Specialized menu for the `admin` account, including the ability to reset the admin password.
* **Session Management:** Features a "Logout" option to return to the login screen and a "System Exit" to terminate the program.

## 🛠️ Technical Stack & Concepts
* **Language:** Python 3.x
* **Core Concepts:**
    * **Functions:** Modularized login logic for reusability.
    * **Nested Loops:** Main system loop combined with authenticated session loops.
    * **Data Structures:** Utilizes synchronized lists for storing usernames and passwords.
    * **List Methods:** Implements `append()`, `pop()`, and `index()` for data manipulation.
    * **Error Handling:** Validates user choices to prevent system crashes.

## 📖 How to Run
1. Ensure you have **Python 3** installed on your machine.
2. Clone this repository or download the `.py` file.
3. Open your terminal and navigate to the project folder.
4. Run the following command:
   ```bash

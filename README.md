# 🔥 Personal Firewall Simulation

A simple Python-based firewall simulation that demonstrates how a firewall can block or allow access to websites based on predefined rules. This project is developed as part of a Cyber Security Internship.

---

## 📌 Project Description

A firewall is one of the most important components of network security. This project simulates a personal firewall by checking whether a website is present in a list of blocked domains. If the website is blocked, access is denied; otherwise, the program resolves and displays its IP address.

---

## 🎯 Objectives

- Understand the basic concept of a firewall.
- Simulate website filtering using Python.
- Learn hostname-to-IP address resolution.
- Gain practical knowledge of network security.

---

## 🛠️ Technologies Used

- Python 3
- Socket Module (Built-in)
- Visual Studio Code

---

## 📂 Project Structure

```
Personal-Firewall/
│
├── firewall.py
├── rules.txt
├── requirements.txt
├── README.md
└── Screenshot 2026-06-29 120136.png
```

---

## ✨ Features

- Blocks websites listed in `rules.txt`
- Allows access to other websites
- Displays the IP address of allowed websites
- Easy to update firewall rules
- Simple command-line interface

---

## 📋 Requirements

- Python 3.x

No external Python libraries are required.

---

## 🚀 Installation

1. Download or clone the project.
2. Open the project folder in Visual Studio Code.
3. Make sure Python is installed.

Check Python version:

```bash
python --version
```

---

## ▶️ Running the Project

Open the terminal and run:

```bash
python firewall.py
```

---

## 📝 Sample Output

```
========================================
Personal Firewall Simulation
========================================

Enter website (or type exit):
facebook.com

❌ Access Blocked!

Enter website (or type exit):
github.com

✅ Access Allowed
IP Address: 140.82.xxx.xxx

Enter website (or type exit):
exit

Firewall Closed.
```

---

## 📸 Project Screenshot

> The screenshot below shows the firewall simulation running.

![Firewall Output](Screenshot%202026-06-29%20120136.png)

---

## 📚 Learning Outcomes

- Understood the basic working of a firewall.
- Learned how to block websites using predefined rules.
- Gained experience with Python socket programming.
- Improved knowledge of network security concepts.

---

## 🚀 Future Enhancements

- Add IP address blocking.
- Add whitelist functionality.
- Store firewall logs.
- Develop a graphical user interface (GUI).

---

## 👩‍💻 Author

**Priyadharshini E**

Cyber Security Internship

---

## 📄 License

This project is intended for educational and internship purposes only.

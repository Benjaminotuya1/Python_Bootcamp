## Project 1: Clinical Trial Manager
* **Date:** 12/8/2025
* **The Struggle:** I struggled to understand where to put the `input()` logic—inside the class or outside?
* **The Breakthrough:** I learned that a Class is usually just a Blueprint. If I want the Class to create itself from user input, I need a `@classmethod` (The Factory Pattern).
* **Key Concept:** `self` = The specific patient. `cls` = The generic blueprint.

## Project 2: The Secure Bank Vault 🏦
* **Date:** 12/9/2025
* **The Struggle:** Understanding why I can't just access `p1.balance` directly.
* **The Breakthrough:** I learned about **Encapsulation**. By putting `__` (double underscore) before a variable, I make it **Private**.
* **Key Concept:** You need "Getters" (to see data) and "Setters" (to change data) to protect the Vault from hackers or bad logic (like negative deposits).
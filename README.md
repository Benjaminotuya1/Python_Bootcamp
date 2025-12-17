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

## Project 3: The Zoo Simulator 🦁
* **Date:** 12/17/2025
* **The Concept:** **Inheritance** (Don't Repeat Yourself).
* **The Breakthrough:** I learned that I can create a generic "Parent" class (`Animal`) and have "Child" classes (`Lion`) inherit all its code.
* **The Magic:** **Polymorphism**. I can put Lions, Birds, and Elephants in the same list and loop through them. Even though I call the same method `.sleep()`, they all behave differently.

## Project 4: The Shape Calculator 📐
* **Date:** 12/17/2025
* **The Concept:** **Abstract Base Classes** (The Enforcer).
* **The Breakthrough:** I learned how to create a "Blueprint" class that forces other classes to follow specific rules.
* **Why it matters:** In large systems (like Banking or Hospitals), you need to prevent other developers from creating incomplete objects. This makes the code "Fail Fast" and prevents bugs.

# Secure Bank Vault 🔒

## Project Overview
A Python implementation of a banking system that strictly enforces **Encapsulation**. It simulates a secure vault where account balances are private and can only be modified through validated transactions.

## The Problem
In basic programming, data is "public"—anyone can change a bank balance to an invalid number (e.g., -500 or 1,000,000). This project solves that by locking the data away and forcing all interaction to go through secure methods.

## Features
* **Private Attributes:** Uses `__balance` to prevent direct access or modification.
* **Validation Logic:** The `deposit` method rejects negative numbers.
* **Safe Withdrawal:** Checks for sufficient funds before allowing a transaction.
* **Getter Methods:** Allows users to view their balance without touching the private variable.

## How to Run
1. Navigate to the folder.
2. Run the script:
   python main.py

# Clinical Trial Manager 🏥

## Project Overview
This is a Python-based Command Line Interface (CLI) tool designed to manage patient data for clinical trials. It demonstrates the power of **Object-Oriented Programming (OOP)** by structuring raw patient data into organized Objects, rather than using loose variables.

## The Problem
Managing clinical data with simple lists or loose variables is error-prone; sorting one list can de-sync it from another (e.g., names and ages getting mixed up). This project solves that by encapsulating patient data into a single source of truth: the `Patient` class.

## Features
- **Dynamic Data Entry:** Uses a `@classmethod` factory pattern to handle user inputs cleanly.
- **Data Encapsulation:** Uses a Python Class to blueprint patient attributes.
- **Formatted Dashboard:** Detailed f-string formatting to generate a clean, readable data table.

## How to Run
1. Navigate to the project folder.
2. Run the program
   python main.py

## Key Learnings
* **Factory Pattern:** Learned to use `@classmethod` to separate the creation logic from the main loop.
# Geometry Engine (Abstract Base Classes) 📐

## Project Overview
A robust Geometry Calculator that uses **Abstract Base Classes (ABCs)** to enforce strict architectural rules. It prevents the creation of invalid shapes and ensures that every specific shape (Circle, Rectangle) implements the required mathematical formulas.

## The Concepts
* **Abstract Base Classes (ABC):** The `Shape` class acts as a contract. It forces all child classes to have `area()` and `perimeter()` methods.
* **Architecture:** The system prevents "Developer Errors" by crashing if a new shape is added without the necessary logic.
* **Separation of Concerns:** Calculations return raw numerical data, allowing the display logic to be handled separately (crucial for Data Science pipelines).

## How to Run
1. Navigate to the folder.
2. Run the script:
   python main.py
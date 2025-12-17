# Zoo Simulator 🦁

## Project Overview
A Python simulation demonstrating **Inheritance** and **Polymorphism**. This project models a zoo where different species share common traits from a parent `Animal` class but demonstrate unique behaviors through method overriding.

## The Concepts
* **Inheritance:** The `Lion`, `Bird`, and `Elephant` classes inherit DNA (attributes like name/species) from the generic `Animal` class, preventing code duplication.
* **Method Overriding:** The `Bird` class rejects the default sleeping behavior and defines its own version ("sleeping in a nest").
* **Polymorphism:** A loop iterates through a list of mixed animals, treating them all as generic "Animals," yet each executes its specific behavior automatically.

## How to Run
1. Navigate to the folder.
2. Run the script:
   python main.py
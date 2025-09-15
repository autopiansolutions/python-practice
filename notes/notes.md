# Notes

About This File

This file is my personal learning journal while studying Python and Computer Science fundamentals.
I use it to take notes, summarize concepts, and reflect on what I’ve learned.

## Table of Contents

1. Hello World

## Hello World

### Welcome 

- Python is a programming language used to communicate commands to a computer.
- Commands are written in text files called programs.
- Running a program = computer reads → translates → executes instructions.
- Python is popular because it’s readable, versatile, and beginner-friendly.

### Comments

- Comments = text ignored by the Python interpreter.
- Created with #.
- Uses:
  - Provide context for why code is written a certain way.
  - Help others (or future you) understand code faster.
  - Temporarily disable a line of code without deleting it.

### Print

- `print()` makes the computer display information (**output**).  
- Messages must be inside **quotes** (`" "` or `' '`).  
- **Output** = what the program displays after running.  

### Strings

- A **string** is a block of text.  
- Defined by surrounding text with either:  
  - Double quotes: `"Hello world"`  
  - Single quotes: `'Hello world'`  
- Both work the same — just be consistent.

### Variables

- **Variables** store data for reuse.  
- Created with the assignment operator `=`.  
- Naming rules:  
  - No spaces or special symbols (except `_`)  
  - Cannot start with a number  
  - Can include numbers after the first letter (`cool_variable_5`)  
- Called “variables” because their values can be updated while keeping the same name.
- Variables can be **reassigned** to new values.  
- The variable name stays the same, but the stored value changes.  
- Useful when program context changes (e.g., greeting vs. goodbye).

### Errors

- Since humans make mistakes, programming languages help us identify and fix them.  
- In Python, mistakes are called **errors**.  
- Python will show where an error occurs using a `^` character.  
- Unexpected errors are called **bugs**.  
- The process of fixing these is called **debugging**.  

**Common Error Types:**  
- **SyntaxError**:  
  - Problem with code structure.  
  - Examples: missing parenthesis, misplaced punctuation, wrong command placement.  

- **NameError**:  
  - Python doesn’t recognize a word.  
  - Happens when using a variable that hasn’t been defined.

### Numbers

- **Integer (`int`)**  
  - Whole numbers (no decimals).  
  - Includes positive, negative numbers, and 0.  
  - Examples: counting people, jellybeans in a jar, keys on a keyboard.  
  - Example: `5`, `-12`, `0`  

- **Floating-point number (`float`)**  
  - Numbers with decimal points.  
  - Used for fractions and precise measurements.  
  - Examples: wall length, average test score, baseball batting average.  
  - Example: `3.14`, `-0.5`, `42.0`

 ### Calculations
 
 **Basic Arithmetic in Python:**  
- Addition: `+`  
- Subtraction: `-`  
- Multiplication: `*`  
- Division: `/`  

### Exponents

- In Python, the `**` operator is used for exponentiation.  
- Equivalent to “raise a number to the power of another.”  
- Works with integers, floats, and fractional powers. 

### Modulo 

- The **modulo operator** (`%`) returns the remainder of a division.  
- If two numbers divide evenly, the result is `0`.  
- Useful for detecting divisibility and creating repeating patterns.

 ### Concatenation

- The `+` operator can **combine strings** (not just numbers).  
- This is called **string concatenation**.  
- Concatenation creates a new string → first string + second string.  
- No space is automatically added — include `" "` if needed.

### Plus Equals

- The `+=` operator updates a variable **in place**.  
- Saves you from rewriting the variable name on both sides of `=`.  
- Works with **numbers** (incrementing) and **strings** (concatenation).

### Multi-line Strings

Python strings are very flexible, but if we try to create a string that spans multiple lines using single (`'`) or double (`"`) quotes, we get a **SyntaxError**.

**Solution: Triple Quotes**
Python provides **multi-line strings** using three quotes (`"""` or `'''`).  
With triple quotes, the string doesn’t end until the next triple-quote.  

This is especially useful when:
- The string contains a lot of quotation marks.
- We want to preserve line breaks as part of the string.







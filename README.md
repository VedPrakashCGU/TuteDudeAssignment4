# TuteDudeAssignment4
# File Handling in Python

This repository contains two Python programs demonstrating basic file handling:
1. **Reading a File and Handling Errors**
2. **Writing, Appending, and Reading a File**

## 📝 Program 1: Read a File and Handle Errors

### 📌 Problem Statement
Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

### 🖥️ Code
```python
try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes extra spaces/newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

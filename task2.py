# Step 1: Take user input and write to a file
with open("output.txt", "w") as file:
    text = input("Enter text to write to the file: ")
    file.write(text + "\n")

# Step 2: Append additional data
with open("output.txt", "a") as file:
    more_text = input("Enter additional text to append: ")
    file.write(more_text + "\n")

# Step 3: Read and display the final content
print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    print(file.read())

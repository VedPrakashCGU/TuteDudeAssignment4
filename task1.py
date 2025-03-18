try:
    # Open the file in read mode
    with open(r'C:\Users\user\Desktop\TudeDude\Assignment4\sample.txt', "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes extra spaces/newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
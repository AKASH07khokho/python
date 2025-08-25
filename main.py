# This program extracts a substring from a given string

# Get input from the user
text = input("Enter a string: ")          # e.g., "akash"
start = int(input("Enter start index: ")) # e.g., 1
end = int(input("Enter end index: "))     # e.g., 4

# Check if the indices are valid
if start < 0 or end > len(text) or start >= end:
    print("Invalid start or end index!")
else:
    # Extract the substring
    substring = text[start:end]

    # Display the result
    print("Substring:", substring)

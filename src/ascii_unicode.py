# Convert text to ASCII numbers
def text_to_ascii(text):
    ascii_values = []
    for char in text:
        ascii_values.append(ord(char))
    return ascii_values


# Convert ASCII numbers back to text
def ascii_to_text(numbers):
    text = ""
    for num in numbers:
        text += chr(num)
    return text


# Program starts here
if __name__ == "__main__":

    print("1: Text to ASCII")
    print("2: ASCII to Text")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        text = input("Enter text: ")
        result = text_to_ascii(text)
        print("ASCII Values:", result)

    elif choice == "2":
        numbers = input("Enter ASCII numbers separated by space: ")
        number_list = numbers.split()
        number_list = [int(n) for n in number_list]
        result = ascii_to_text(number_list)
        print("Text:", result)

    else:
        print("Invalid choice")

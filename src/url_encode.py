import urllib.parse

def url_encode(text):
    return urllib.parse.quote(text)

if __name__ == "__main__":
    user_input = input("Enter text to URL encode: ")
    result = url_encode(user_input)
    print("Encoded URL:", result)

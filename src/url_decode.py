import urllib.parse

def url_decode(text):
    return urllib.parse.unquote(text)

if __name__ == "__main__":
    user_input = input("Enter URL encoded text: ")
    result = url_decode(user_input)
    print("Decoded URL:", result)

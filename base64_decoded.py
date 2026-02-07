import base64

def base64_decode(text):
    decoded_bytes = base64.b64decode(text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

if __name__ == "__main__":
    user_input = input("Enter Base64 text to decode: ")
    try:
        result = base64_decode(user_input)
        print("Decoded Output:", result)
    except Exception:
        print("Invalid Base64 input")

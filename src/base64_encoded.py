import base64

def encode_base64(txt):
    encode_bytes = base64.b64encode(txt.encode("utf-8"))
    return encode_bytes.decode("utf-8")

if __name__ == "__main__":
    user_input = input("enter text to encode: ")
    encoded = encode_base64(user_input)
    print(f"Encoded text: {encoded}")
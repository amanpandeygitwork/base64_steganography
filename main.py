import qrcode
import base64

def img_to_base64():
    with open("instagram.png","rb") as image:
        base64_bytes = base64.b64encode(image.read())
        base64_string = base64_bytes.decode()
        return base64_string

def create_msg():
    msg = img_to_base64()
    msg+=";https://www.google.com/"
    return msg

def create_qr(msg):
    qr = qrcode.make(msg)
    qr.save("qrcode.png")

def main():
    encoded_str = create_msg()
    create_qr(encoded_str)

if __name__ == "__main__":
    main()

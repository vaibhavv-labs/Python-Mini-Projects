import qrcode

url = input("Enter The URL : ").strip()
img = qrcode.make(url)
img.save("Your QR Code.png")
print("QR Code")

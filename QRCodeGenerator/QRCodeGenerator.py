import qrcode

data = "https://github.com/bkaradag"

qr = qrcode.QRCode(version=1, box_size=15, border=7)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="red")

img.save("C:/Users/Berkay Karadag/Desktop/Projekte/qrcode1.png")


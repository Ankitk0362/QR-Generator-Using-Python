import qrcode

data = "Hey welcom to Programming World" #Content you want to display after scanning
qr = qrcode.make(data)
qr.save("qrcode.png") # file where your QR will save 
print("QR code generated successfully")

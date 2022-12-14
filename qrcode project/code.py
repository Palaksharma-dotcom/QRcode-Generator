import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5

)
print("Enter text/link whose QRcode is to be generated")
data=input()
# data="youtube.com/watch?v=B-MfwP_RmHY&list=RDMM_ulT-EQDzEI&index=10"
# data="this is qr code"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")

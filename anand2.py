import qrcode as qr
from PIL import Image
qr = qr.QRCode(version=1 , error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border = 4)
qr.add_data('https://www.youtube.com/')
qr.make(fit=True)
img = qr.make_image(fill_color = "blue", back_color ="black" )
img.save("youtube qr code.png")

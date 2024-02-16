import qrcode as qr
img = qr.make("https://www.instagram.com/anandsoni2017?igsh=MWxud25obDNncW11aQ==")
img.save("instagram_profile.png")
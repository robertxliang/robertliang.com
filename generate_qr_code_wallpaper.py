import qrcode
from PIL import Image

QR_TEXT = "robertliang.com"
PHONE_RESOLUTION = (1125, 2436)
QR_RESOLUTION = (1000, 1000)
VERTICAL_OFFSET = 400
BACKGROUND_COLOR = (14, 35, 46)
FILL_COLOR = (239, 239, 239)


img_bg = Image.new("RGB", PHONE_RESOLUTION, color=BACKGROUND_COLOR)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=16,
    border=4,
)
qr.add_data(QR_TEXT)
qr.make(fit=True)

img_qr = qr.make_image(fill_color=FILL_COLOR, back_color=BACKGROUND_COLOR)
img_qr = img_qr.resize(QR_RESOLUTION)

pos = (
        (img_bg.size[0] - img_qr.size[0])//2, 
        (img_bg.size[1] - img_qr.size[1])//2 + VERTICAL_OFFSET
)

img_bg.paste(img_qr, pos)

img_bg.save(QR_TEXT + ".png")

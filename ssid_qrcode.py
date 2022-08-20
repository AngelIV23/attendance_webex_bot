import qrcode, os, glob
from PIL import Image

def create_qrcode(qrcode_str):
    for image in os.listdir("./images"):
        # If is png image
        if image.endswith(".png"):
            im = Image.open('./images/' + image)
            # and is not RGBA
            if im.mode != 'RGBA':
                im.convert("RGBA").save(f"images/rgb-{image}")

    logo_link = './images/rgb-cisco-logo.png'
    logo = Image.open(logo_link)
    
    # taking base width
    basewidth = 100
    
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.BICUBIC)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    
    # taking url or text
    qr_string = qrcode_str
    
    # adding URL or text to QRcode
    QRcode.add_data(qr_string)
    
    # generating QR code
    QRcode.make()
    
    # taking color name from user
    QRcolor = 'Black'
    
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
    
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    
    # save the QR code generated
    QRimg.save(f'./images/qr-code-wifi.png', quality = 95)
    for filename in glob.glob("./images/rgb-*"):
        os.remove(filename) 


ssid     = 'this_is_your_SSID'
password = 'add_your_psk'
auth_type = "WPA2"
hidden = False
wifi_qrcode_string = f"WIFI:T:{auth_type};S:{ssid};P:{password};H:{hidden};;"

create_qrcode(wifi_qrcode_string)
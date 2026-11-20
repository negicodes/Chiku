"""Usage: python make_qr.py https://negicodes.github.io/chiku/
Needs: pip install "qrcode[pil]"
"""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = sys.argv[1] if len(sys.argv) > 1 else input("Profile URL: ").strip()

qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=20, border=4)
qr.add_data(url)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save("chiku_qr.png")
print("Saved chiku_qr.png ->", url)

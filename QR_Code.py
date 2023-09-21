# Run "pip install pyqrcode" before run the program
import pyqrcode

data = input("Enter your text or link or generate code: ")

# Using pyqrcode.create() to create a qr code of the input data
qr = pyqrcode.create(data)

# Using .svg method to save the qr code as SVG file of provided name a& scale
qr.svg('qr_code.svg', scale= 8)


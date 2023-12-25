import qrcode

# Replace 'C:\\Users\\KY\\Desktop\\qr\\login.html' with the actual path to your HTML file
html_file_path = r'C:\Users\KY\Desktop\qr\login.html'

# Create a string with the HTML file path
data_to_encode = f'file://{html_file_path}'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data_to_encode)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save or display the QR code
img.save("wifi_qr.png")
img.show()

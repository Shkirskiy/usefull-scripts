import qrcode

def generate_qr_code(url: str) -> None:
    """
    Generate a QR code from a given URL and save it as a PNG file.
    
    Args:
        url (str): The URL to encode in the QR code.
    """

    # Create a QRCode object with default settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save("qrcode.png")


def main() -> None:
    """
    Main entry point for the script.
    """

    # Define the URL you want to encode
    url = "https://www.example.com"
    
    generate_qr_code(url)


if __name__ == "__main__":
    main()

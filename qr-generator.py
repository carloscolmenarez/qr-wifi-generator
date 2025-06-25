import qrcode

def generate_wifi_qr(ssid, password, security="WPA"):
    """
    Generate a QR code for WiFi connection.

    Args:
        ssid (str): The WiFi SSID.
        password (str): The WiFi password.
        security (str): The security type (WPA, WEP, or empty for open network).

    Returns:
        None
    """
    wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};;"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_string)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill="black", back_color="white")
    img.save("wifi_qr.png")

    print("QR code saved as wifi_qr.png")

if __name__ == "__main__":
    # Example usage:
    ssid = input("Enter your WiFi SSID: ")
    password = input("Enter your WiFi password: ")
    security = input("Enter security type (WPA/WEP or leave empty for open): ").strip().upper() or "WPA"
    
    generate_wifi_qr(ssid, password, security)

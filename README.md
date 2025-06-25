# WiFi QR Code Generator

Generate a QR code that allows users to connect to your WiFi network by simply scanning it — no typing required!

## 📦 Features

- Supports WPA, WEP, or open networks
- Saves the QR code as a PNG image
- Simple command-line interface

## 🛠️ Requirements

- Python 3.6+
- `qrcode` library with PIL support

## 🚀 Setup Instructions

1. **Clone or download the project folder:**

   ```bash
    git clone https://github.com/carloscolmenarez/qr-wifi-generator.git
    cd qr-wifi-generator
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install qrcode[pil]
    ```

4. **Run the script:**

    ```bash
    python qr-generator.py
    ```

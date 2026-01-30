# Steganography Demo Application
A steganography demo app implemented in Python with OpenCV and a local Flask web interface.
The app allows hiding one image inside another using few different steganographic methods.

## Methods
- **LSB (Least Significant Bit)** – Fast spatial-domain method
- **PVD (Pixel Value Differencing)** – Adaptive spatial-domain method
- **DCT (Discrete Cosine Transformation)** – Frequency-domain method

## Requirements
- Python 3.9+
- Flask
- Pillow
- OpenCV

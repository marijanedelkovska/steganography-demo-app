from lsb import steganography_LSB


if __name__ == "__main__":
    cover_path = r'C:\Users\Marija\PycharmProjects\PythonProject\main\images\lsb - png\lsb1.png'   # bazna
    secret_path = r'C:\Users\Marija\PycharmProjects\PythonProject\main\images\lsb - png\hide.png' # tajna
    output_path = r'C:\Users\Marija\PycharmProjects\PythonProject\main\images\lsb - png\lsb_output1.png' # rez

    steganography_LSB(cover_path, secret_path, output_path)


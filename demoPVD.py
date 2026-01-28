from pvd import steganography_PVD


if __name__ == "__main__":
    cover_path = r'C:\Users\Marija\PycharmProjects\PythonProject\main\images\pvd - png\pvd3.png'  # bazna sl
    secret_path = r'C:\Users\Marija\PycharmProjects\PythonProject\main\images\pvd - png\hide.png'  # tajna sl
    output_path = r'C:\Users\Marija\PycharmProjects\PythonProject\main\images\pvd - png\pvd_output3.png'  # rez

    steganography_PVD(cover_path, secret_path, output_path)

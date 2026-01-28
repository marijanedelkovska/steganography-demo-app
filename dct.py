import cv2
import numpy as np


def steganography_DCT(base_path, hide_path, output_path):
    base = cv2.imread(base_path, cv2.IMREAD_GRAYSCALE)
    hidden = cv2.imread(hide_path, cv2.IMREAD_GRAYSCALE)

    hidden = cv2.resize(hidden, base.shape[::-1])

    _, hide_binary = cv2.threshold(hidden, 127, 1, cv2.THRESH_BINARY)

    base_copy = np.copy(base)

    height, width = base.shape

    for i in range(0, height, 8):
        for j in range(0, width, 8):
            if i + 8 <= height and j + 8 <= width:
                block = np.float32(base[i:i + 8, j:j + 8])
                block = cv2.dct(block)

                bit = hide_binary[i // 8, j // 8]

                coef = block[4, 3]

                if bit == 0:
                    if int(coef) % 2 == 0:
                        coef = np.floor(coef)
                    else:
                        coef = np.floor(coef) - 1
                else:
                    if int(coef) % 2 != 0:
                        coef = np.floor(coef)
                    else:
                        coef = np.floor(coef) + 1
                block[4, 3] = coef

                inverse_block = cv2.idct(block)
                base_copy[i:i + 8, j:j + 8] = np.clip(inverse_block, 0, 255)

    cv2.imwrite(output_path, np.uint8(base_copy))

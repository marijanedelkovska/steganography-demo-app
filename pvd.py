from PIL import Image
import math

rang = [(0, 7), (8, 15), (16, 31), (32, 63), (64, 127), (128, 255)]

def intToBin(n, bits=8):
    return format(n, f'0{bits}b')

def imgToBin(img):
    img = img.convert("L")
    binary = ''
    for pixel in img.getdata():
        binary += intToBin(pixel)
    return binary

def rangInfo(diff):
    for lower, upper in rang:
        if lower <= diff <= upper:
            bit_count = int(math.floor(math.log2(upper - lower + 1)))
            return lower, bit_count
    return 0, 0

def steganography_PVD(base_path, hide_path, output_path):
    base = Image.open(base_path).convert("L")
    hidden = Image.open(hide_path).resize(base.size)
    hiddenBit = imgToBin(hidden)

    encoded = base.copy()
    pixels = list(base.getdata())
    newPixels = []
    i = 0
    b = 0

    while i < len(pixels) - 1 and b < len(hiddenBit):
        p1 = pixels[i]
        p2 = pixels[i+1]

        diff = abs(p1 - p2)
        lower, count = rangInfo(diff)

        if count == 0 or b + count > len(hiddenBit):
            newPixels.extend([p1, p2])
            i += 2
            continue

        bits = hiddenBit[b:b+count]
        b += count
        diff2 = int(bits, 2) + lower

        if p1 >= p2:
            if p1 + p2 + diff2 % 2 == 1:
                new_p1 = (p1 + p2 + diff2 + 1) // 2
            else:
                new_p1 = (p1 + p2 + diff2) // 2
            new_p2 = new_p1 - diff2
        else:
            if p1 + p2 + diff2 % 2 == 1:
                new_p1 = (p1 + p2 - diff2 + 1) // 2
            else:
                new_p1 = (p1 + p2 - diff2) // 2
            new_p2 = new_p1 + diff2

        new_p1 = max(0, min(255, new_p1))
        new_p2 = max(0, min(255, new_p2))

        newPixels.extend([new_p1, new_p2])
        i += 2

    newPixels.extend(pixels[i:])


    encoded.putdata(newPixels)
    encoded.save(output_path)


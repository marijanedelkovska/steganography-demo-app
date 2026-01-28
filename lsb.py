from PIL import Image

def intToBin(n):
    return format(n, '08b')


def white_background(path):
    img = Image.open(path).convert("RGBA")
    white = Image.new("RGB", img.size, (255, 255, 255)) 
    white.paste(img, mask=img.split()[3])  
    return white


def steganography_LSB(base_path, hide_path, output_path):
    base = white_background(base_path)
    hidden = white_background(hide_path)

    if hidden.size != base.size:
        hidden = hidden.resize(base.size)

    newPic = base.copy()

    width, height = base.size

    for x in range(width):
        for y in range(height):
            basePixel = base.getpixel((x, y))
            hiddenPixel = hidden.getpixel((x, y))

            newPixel = []
            for i in range(3):  # For R, G, B
                binaryB = intToBin(basePixel[i])
                binaryH = intToBin(hiddenPixel[i])

                combo = binaryB[:6] + binaryH[:2]
                newPixel.append(int(combo, 2))

            newPic.putpixel((x, y), tuple(newPixel))

    newPic.save(output_path)

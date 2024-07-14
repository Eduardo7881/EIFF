import struct
from PIL import Image

def write_eiff(image_path, output_path):
    if not output_path.lower().endswith('.eiff'):
        raise ValueError("The file extension must be .eiff")
        
    image = Image.open(image_path)
    width, height = image.size

    with open(output_path, 'wb') as f:
        f.write(struct.pack('>I', width))
        f.write(struct.pack('>I', height))

        for y in range(height):
            for x in range(width):
                rgba = image.getpixel((x, y))
                hex_pixel = '{:02X}{:02X}{:02X}{:02X}'.format(rgba[0], rgba[1], rgba[2], rgba[3])
                f.write(bytes.fromhex(hex_pixel))


def read_eiff(file_path):
    if not file_path.lower().endswith('.eiff'):
        raise ValueError("The file extension must be .eiff")


    with open(file_path, 'rb') as f:
        width = struct.unpack('>I', f.read(4))[0]
        height = struct.unpack('>I', f.read(4))[0]

        image = Image.new('RGBA', (width, height))

        for y in range(height):
            for x in range(width):
                hex_pixel = f.read(4).hex()
                rgba = (int(hex_pixel[0:2], 16), int(hex_pixel[2:4], 16), int(hex_pixel[4:6], 16), int(hex_pixel[6:8], 16))
                image.putpixel((x, y), rgba)

        return image



# pip3 install --user pypng

import png
import sys


def e5(img):
    """Transpose une image en données chiffrées."""

    width, height, pixels, info = img.read_flat()

    print('[i] Image size: %u x %u' % (width, height))

    pixel_byte_width = 4 if info['alpha'] else 3
    assert(pixel_byte_width == 4)

    data = []

    for x in range(width):
        for y in range(height):

            pos = (x + y * width) * pixel_byte_width

            r, g, b, a = pixels[pos:pos+4]

            if r != 0 or g != 0 or b != 0 or a != 0:

                data.append(r)
                data.append(g)
                data.append(b)

    return data


def voice_decrypt(data):
    """Déchiffre les données avec leur clef intégrée."""

    key = data[:16]
    data = data[16:]

    print('[i] Key:', bytes(key))

    decrypted = []

    for i in range(len(data)):

        decrypted.append(data[i] ^ key[i % 16])

    return decrypted


if __name__ == '__main__':
    """Point d'entrée du programme."""

    img = png.Reader(sys.argv[1])

    enc = e5(img)

    dec = voice_decrypt(enc)

    with open('stage2.bin', 'wb') as fd:
        fd.write(bytes(dec))

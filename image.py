import os
import numpy
import piexif
import argparse
from PIL import Image

"""
Anton Benfey - 24/08/2021
Generate images of any dimension and roughly any size for testing data.

Example usage:
    python3 generate_image.py 100 100 1.5 kb

Output:
    A 100x100 image of size ~1.5kb
"""

def generate_image(dimensions):
    data = numpy.zeros((dimensions[1], dimensions[0], 3))
    Image.fromarray(data, 'RGB').save('temp.png')

def add_metadata(magnitude, factor):

    img = Image.open('temp.png')

    exifData = {}
    factors = {'kb': 1024, 'mb': 1024*1024, 'gb': 1024*1024*1024}
    assert factor.lower() in factors

    size = os.path.getsize('temp.png')
    exif_size = int(magnitude*factors[factor.lower()])

    if size < exif_size:
        data = bytes("a" * (exif_size - size), 'utf-8')
    else:
        data = bytes("a" * exif_size, 'utf-8')

    exif_ifd = {piexif.ExifIFD.UserComment: data}
    exif_dict = {"0th": {}, "Exif": exif_ifd, "1st": {}, "thumbnail": None, "GPS": {}}
    exif_dat = piexif.dump(exif_dict)

    img.save(f'{img.size[0]}x{img.size[1]}-{round(magnitude)}{factor}.png',  exif=exif_dat)
    os.remove("temp.png")

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(dest='width', type=int, help="Width of image in pixels (int)")
    parser.add_argument(dest='height', type=int, help="Height of image in pixels (int)")
    parser.add_argument(dest='magnitude', type=float, help="Magnitude of file size (float)")
    parser.add_argument(dest='factor', type=str, help="Factor of file size (str)")

    args = parser.parse_args()

    img = generate_image((args.width, args.height))
    add_metadata(args.magnitude, args.factor)

if __name__ == "__main__":
    main()

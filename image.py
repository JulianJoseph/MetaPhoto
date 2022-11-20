from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS

img = Image.open("C://Users//jules//Pictures//Frame//2022//2022_07//Sicily-Avola-2022-07-08-001.jpg")

exif = img._getexif()
#print(exif)

if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)
            print(f"{name}: {exif[name]}")


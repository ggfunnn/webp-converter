from PIL import Image
import os
import glob


class Convert(object):
    """Class which converts .jpg/.png files to .webp"""

    def __init__(self):
        path = None
        while path is None:
            path = input('Please specify the path to your file/files (or press Enter if it\'s in the same path): ')
            if path == "":
                self.path = os.getcwd()

            else:
                if os.path.isdir(path):
                    self.path = path

                else:
                    print('Error: Path doesn\'t exist!\n')
                    path = None

    def convert(self):
        EXTENSIONS = ('*.jpg', '*.png')

        os.chdir(self.path)

        for extension in EXTENSIONS:
            for file in glob.glob(extension):
                filename = file.replace(extension.replace('*', ''), '')

                with Image.open(file) as im:
                    im.save(filename + '.webp', format="WebP", lossless=True)

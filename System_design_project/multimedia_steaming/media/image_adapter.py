"""  
Adapter design pattern

"""

from .interface import IMedia
from .image import Image

class ImageAdapter(IMedia):
    def __init__(self, image: Image):
        self.__image = image

    def play(self):
        self.__image.display()
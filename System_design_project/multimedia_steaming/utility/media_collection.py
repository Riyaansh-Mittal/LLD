"""  
Composit design pattern

"""

from multimedia_steaming.media.interface import IMedia
from typing import List

class MediaCollection(IMedia):
    def __init__(self, medialist: List[IMedia]):
        self.__medialist = medialist
        

    def play(self):
        for media in self.__medialist:
            media.play()

    def add_media(self, media: IMedia):
        self.__medialist.append(media)


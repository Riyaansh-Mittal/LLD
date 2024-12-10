from .media_decorator import MediaDecorator
from multimedia_steaming.media.interface import IMedia

class HighQuality(MediaDecorator):
    def __init__(self, decorateMedia: IMedia):
        super().__init__(decorateMedia)


    def play(self):
        super().play()
        print("Enhancing playback quality")
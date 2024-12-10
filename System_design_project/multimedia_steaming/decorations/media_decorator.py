from multimedia_steaming.media.interface import IMedia

class MediaDecorator(IMedia):
    def __init__(self, decoratedMedia: IMedia):
        self._decoratedMedia = decoratedMedia

    def play(self):
        self._decoratedMedia.play()
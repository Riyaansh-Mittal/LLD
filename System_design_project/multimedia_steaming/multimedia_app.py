from .media.interface import IMedia
from .media.video import Video
from .media.audio import Audio
from .media.image import Image
from .media.image_adapter import ImageAdapter
from .decorations.high_quality import HighQuality
from .utility.media_collection import MediaCollection

# import sys
# sys.path.append('/path/to/parent/directory')

if __name__ == "__main__":
    video: IMedia = Video(filename="movie.mp4")
    audio: IMedia = Audio(filename="song.mp3")
    img: Image = Image(filename="image.png")
    image: Image = ImageAdapter(img)

    high_quality_audio: IMedia = HighQuality(audio)

    all_media: MediaCollection = MediaCollection(list())

    all_media.add_media(video)
    all_media.add_media(high_quality_audio)
    all_media.add_media(image)

    all_media.play()
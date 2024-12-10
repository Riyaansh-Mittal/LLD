from composit.directory import Directory
from composit.file import File
from composit.file_system import FileSystem

if __name__ == "__main__":

    movie_directory: Directory = Directory("Movie")

    boarder: FileSystem = File("Border")
    movie_directory.add(boarder)

    comedy_movie_directory: Directory = Directory("ComedyMovie")
    halchal: File = File("Halchal")
    comedy_movie_directory.add(halchal)
    movie_directory.add(comedy_movie_directory)
    movie_directory.ls()

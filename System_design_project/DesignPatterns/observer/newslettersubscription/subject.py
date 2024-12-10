from abc import ABC, abstractmethod
from observer import Observer

# Interface
# Subject is the newsletter
class Subject(ABC):
    
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer(self, observer: Observer):
        pass


# Concert subject class newsletter

class SystemsThatScale(Subject):

    def __init__(self):
        self.observer_list: list = list()
    
    def register_observer(self, observer: Observer):
        self.observer_list.append(observer)

    def remove_observer(self, observer: Observer):
        self.observer_list.remove(observer)

    def notify_observer(self):
        for o in self.observer_list:
            o.update(self.article_content)

    def new_article_publish(self, article_content:str):
        self.article_content = article_content
        self.notify_observer()

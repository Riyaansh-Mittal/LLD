from abc import abstractmethod, ABC

# Interface
class Observer(ABC):

    @abstractmethod
    def update(self, article_content: str):
        pass


class IndividualSubscriber(Observer):
    
    def __init__(self, name: str, newsletter):
        self.name = name
        self.newsletter = newsletter
        newsletter.register_observer(self)

    def update(self, article_content: str):
        self.article_content = article_content
        self.article_content_received()


    def article_content_received(self):
        print(f"New content received : {self.article_content} for {self.name}")



class CommunitySubscriber(Observer):
    pass
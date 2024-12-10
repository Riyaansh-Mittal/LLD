from abc import ABC, abstractclassmethod

# interface 
class INotificationAlertObserver():
    @abstractclassmethod
    def update() -> None:
        pass

class EmailAlertObserver(INotificationAlertObserver):
    def __init__(self, email_id, observable):
        self._email_id = email_id
        self._observable = observable
    
    def update(self):
        self.send_mail(self._email_id, "Product is in stock hurry up!!")

    def send_mail(self, email_id: str, message: str) -> None:
        print(f"Mail send to ; {email_id}")


class MobileAlertObserver(INotificationAlertObserver):
    def __init__(self, user_name, observable):
        self._user_name = user_name
        self._observable = observable
    
    def update(self):
        self.send_message(self._user_name, "Product is in stock hurry up!!")

    def send_message(self, user_name: int, message: str) -> None:
        print(f"Mail message to : {user_name}")
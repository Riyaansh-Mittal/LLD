from abc import ABC, abstractclassmethod
from observer.exercice2.observer import INotificationAlertObserver

# Interface
class IStockObservable(ABC):
    @abstractclassmethod
    def add(self, observer: INotificationAlertObserver) -> None:
        pass

    @abstractclassmethod
    def remove(self, observer: INotificationAlertObserver) -> None:
        pass

    @abstractclassmethod
    def notify(self) -> None:
        pass

class IphoneObservable(IStockObservable):
    def __init__(self):
        self._observer_list = list()
        self._stock_count = 0

    def add(self, observer: INotificationAlertObserver) -> None:
        self._observer_list.append(observer)

    def remove(self, observer: INotificationAlertObserver) -> None:
        self._observer_list.remove(observer)
 
    def notify(self) -> None:
        for observer in self._observer_list:
            observer.update()

    def set_stock_count(self, new_stock_added: int) -> None:
        if self._stock_count == 0:
            self.notify()
        self._stock_count += new_stock_added

    @property
    def get_stock_count(self) -> int:
        return self._stock_count
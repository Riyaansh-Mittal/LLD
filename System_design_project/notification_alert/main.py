from observer.exercice2.observer import INotificationAlertObserver,EmailAlertObserver,MobileAlertObserver
from observer.exercice2.observable import IphoneObservable, IStockObservable

if __name__ == "__main__":
    iphone_stock_observable: IStockObservable = IphoneObservable()

    observer1: INotificationAlertObserver = EmailAlertObserver(email_id="tanuj@xyz1.com", observable=iphone_stock_observable) 
    observer2: INotificationAlertObserver = EmailAlertObserver(email_id="tanuj@xyz2.com", observable=iphone_stock_observable) 
    observer3: INotificationAlertObserver = MobileAlertObserver(user_name="tanuj", observable=iphone_stock_observable) 


    iphone_stock_observable.add(observer1)
    iphone_stock_observable.add(observer2)
    iphone_stock_observable.add(observer3)

    iphone_stock_observable.set_stock_count(10)
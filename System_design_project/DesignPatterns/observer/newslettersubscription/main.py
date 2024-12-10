from observer import Observer, IndividualSubscriber
from subject import Subject, SystemsThatScale


newsletter: Subject = SystemsThatScale()
tanuj: Observer = IndividualSubscriber("tanuj",newsletter)

maxx: Observer = IndividualSubscriber("maxx",newsletter)

newsletter.new_article_publish("Observer pattern explained")

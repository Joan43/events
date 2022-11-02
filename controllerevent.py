import random
from event import Event

class Controllerevent:
    def __init__(self):
        self.__pendingevents = {}
        self.__finishedevents = {}

    def addEvent(self,name,date,location,province,regPrice,finished):
        if name not in self.__pendingevents:
            event = Event(name,date,location,province,regPrice,finished)
            self.__pendingevents[name] = event
            return True
        return False

    def addParticipant(self,even,dni,name,age,email):
        event = self.__pendingevents[even]
        event.addParticipant(dni,name,age,email)

    def totalPendingEvents(self):
        return self.__pendingevents
    
    def totalFinishedEvent(self):
        return self.__finishedevents

    def finishEvent(self,even):
        event = self.__pendingevents.pop(even)
        
        e = event.getListParticipants()
        
        num = random.randint(0,(len(e)-1))
        first = e[num]
        num = random.randint(0,len(e)-1)
        second = e[num]
        num = random.randint(0,len(e)-1)
        third = e[num]

        event.addPodium(first,second,third)
        self.__finishedevents[even] = event
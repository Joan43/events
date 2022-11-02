class Event:
    def __init__(self,name,date,location,province,regPrice,finished):
        self.__name = name
        self.__date = date
        self.__location = location
        self.__provice = province
        self.__regPrice = regPrice
        self.__totEvent = 0
        self.__listParticipants = []
        self.__finished = finished
        self.__podium = {}

    def getName(self):
        return self.__name

    def getDate(self):
        return self.__date

    def getLocation(self):
        return self.__location

    def getProvice(self):
        return self.__provice

    def getRegPrice(self):
        return self.__regPrice
    
    def getTotEvent(self):
        return self.__totEvent

    def getListParticipants(self):
        return self.__listParticipants

    def getFinished(self):
        return self.__finished
    
    def getPodium(self):
        return self.__podium

    def addParticipant(self,dni,name,age,email):
        participant = (dni,name,age,email)
        self.__listParticipants.append(participant)

    def addPodium(self,first,second,third):
        self.__podium["FIRST"] = first
        self.__podium["SECOND"] = second
        self.__podium["THIRD"] = third
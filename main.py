from cgi import print_directory
from controllerevent import Controllerevent

controller = Controllerevent()

def menu():
    print("1.- Add Event.")
    print("2.- Add participant to an event.")
    print("3.- List pending event with participants.")
    print("4.- List events finished with podium.")
    print("5.- Finish an event.")
    
def addEvent():
    name = input("Name: ")
    date = input("Date: ")
    location = input("Location: ")
    province = input("Province: ")
    regPrice = input("Price: ")
    finished = input("Finished: ")
    if controller.addEvent(name,date,location,province,regPrice,finished):
        print("Yes!")
    else:
        print("No!")

def addParticipant():
    event = input("Enter event: ")
    dni = input("DNI: ")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    controller.addParticipant(event,dni,name,age,email)  

def totalPendingEvents():
    events = controller.totalPendingEvents()
    for e,event in events.items():
        print(e)
        participants = event.getListParticipants()
        if len(participants) !=0:
            for x in participants:
                    print("\t",x)
        
def totalEventFinished():
    events = controller.totalFinishedEvent()
    for e,event in events.items():
        print(e)
        podium = event.getPodium()
        for x,j in podium.items():
               print("\t",x," - ",j)
    
def addPodium():
    event = input("Enter event: ")
    controller.finishEvent(event)

controller.addEvent("F1","22/03/22","Alberic","Ribera",22,22)
controller.addParticipant("F1","2002344N","Manolo",45,"manolo@gmail.com")
controller.addParticipant("F1","1045644H","Paco",36,"paco@gmail.com")

while True:
    menu()
    opt = int(input("Enter option: "))
    if opt == 1:
        addEvent()
    if opt == 2:
        addParticipant()
    if opt == 3:
        totalPendingEvents()
    if opt == 4:
        totalEventFinished()
    if opt == 5:
        addPodium()
    if opt == 6:
        print("Bye!")
        break
from datetime import *

class Event:
    def __init__(self, name, ven, start, end):
        self.name = name
        self.startTime = start
        self.endTime = end
        #add the new event object to the list of events for the given venue
        ven.addEvent(self)

class Venue:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.events = []
    def addEvent(self, event):
        self.events.append(event)

class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
    def display(self):
        return self.street + "\n " + self.city + ", " + self.state + " " + str(self.zipcode) + "\n " + self.country

#construct 2 adresses:
ad1 = Address("123 Oak Street", "New York", "New York", "USA", 11111)
ad2 = Address("456 Center Ave", "Anna", "Ohio", "USA", 22222)

#construct 2 venues:
v1 = Venue("Theater", ad1)
v2 = Venue("Anna High School", ad2)

#create 3 events:
e1 = Event("Concert", v1, date(2024,6,1), date(2024,6,1))
e2 = Event("Summer Classes", v2, date(2024, 6,1), date(2024,7,31))
e3 = Event("Musical", v2, date(2024, 9,1), date(2024,9,14))

#display info about each venue and the events scheduled there:
for eachven in [v1,v2]:
    print("Venue: ", eachven.name)
    print("Address:\n", eachven.address.display())
    print("Events: ")
    for eachevent in eachven.events:
        print(" Event Name: " + eachevent.name)
        print(" Start: ", eachevent.startTime)
        print(" End: ", eachevent.endTime)
    print("")
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Events, Tickets, Base
 
engine = create_engine('sqlite:///tickets.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Event in the events table
#create a method for the create_event
events = []


def create_events(self,event_name,event_start_date,event_end_date,event_venue):
	if:
	event_name = self.events
	return("Event already exists")


	else:

	new_event = Events(event_name=event_name, event_start_date=event_start_date, event_end_date=event_end_date, event_venue=event_venue)
	self.events.append(event_name)
	self.session.add(new_event)
	self.session.commit()

	return ("You have successfully created an event")

def delete_event(self,event_id):
	try:
		new_delete = self.session.query(Events).filter(event_id=event_id)
		self.session.delete(new_delete)
		self.session.commit()

		return ("Event has been successfully deleted")

	except UnmappedInstanceError:

		return ("Invalid event_id")

def edit_event(self,event_id,new_event_details):


	if:
		new_event_details=self.session.query(Events).filter(event_id=event_id)
		self.session.edit(new_event_details)
		self.session.commit()

		return ("Event successfully editted")

	else:

		return ("Invalid event_id")




def list_events(self):

	list_events= self.session.query(Events).all()
	list_event=[]
	length=0

	for list_event in list_events:
		list_event1=[list_event.event_id, list_event.event_name, list_event.event_start_date, list_event.event_end_date, list_event.event_venue]
		event_list.append(list_event1)

		if length>0:
			self.session.list(list_events)
			self.session.commit()

			return ("The list of events is:" + list_events())

		else:

			return ("No events available")








def view_event(self,event_id):

	if:
		view_event=self.session.query(Events)




def ticket_generate(self,email):




def ticket_invalidate(self,ticket_id):




def ticket(self,event_id):

	new_ticket=Tickets(event_id= new_event.id)
	self.tickets.append(event_id)
	self.session.add(new_ticket)
	self.session.commit()


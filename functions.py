import os
import sys
import smtplib
from sqlalchemy import *
from sqlalchemy.orm import *
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



def create_events(event_name,event_start_date,event_end_date,event_venue):
	if (event_name == events):

		return("Event already exists")

	else:
		new_event = Events(event_name=event_name, event_start_date=event_start_date, event_end_date=event_end_date, event_venue=event_venue)
		events.append(event_name)
		session.add(new_event)
		session.commit()

		return ("You have successfully created an event")

def delete_event(event_id):

	instance= session.query(Events).filter_by(id = event_id).delete()
	session.commit()
	return ("Event successfully deleted")



def edit_event(event_id,event_name,event_start_date,event_end_date,event_venue):

	new_event_details = update(Events). where (Events.id == event_id).values
	({'event_name': event_name, 'event_start_date': event_start_date, 'event_end_date': event_end_date, 'event_venue': event_venue}).execute()
	session.commit()

	return ("Event successfully editted")



def list_events():

	list_events= session.query(Events).all()
	list_event=[]
	length=0
	event_list=[]

	for list_event in list_events:
		list_event1=[list_event.id, list_event.event_name, list_event.event_start_date, list_event.event_end_date, list_event.event_venue]
		event_list.append(list_event1)
		length += 1

	if (length>0):
	
		return (event_list)

	else:

	    return ("No events available")







def view_ticket(event_id):

	

	if (view_ticket==session.query(Tickets).filter_by(event_id=int(event_id))):
		
		session.view(view_ticket)

		return (view_ticket)

	else:
		return ("Invalid event_id")


def generate_tickets(email, event_name):

	"""generate tickets and sends them to the specified email"""

	events=session.query(Events).filter(Events.event_name == event_name).all()

	if len(events)>0:
		event_id = events[0].id
		new_ticket = Tickets()
		new_ticket.event_id = event_id
		session.add(new_ticket)
		session.commit()


		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		
		#Next, log in to the server
		server.login("evalyne", "0716664041")
		#Send the mail
		msg = "TICKET GENERATED"
		server.sendmail("ndanuevalyne12@gmail.com", email, msg)
		server.close()


		print("Email has successfully been sent")


		#return send_mail(email, event_id)

	else:

		return ("Event name does not exist or invalid email")

def ticket_invalidate(event_name):

	"""invalidates a ticket"""
	ticket=session.query(Tickets).filter(Tickets.id == ticket_id).first()
	ticket.ticket_status = 'invalid'

	
	session.commit()

	return ("Ticket has been invalidated")
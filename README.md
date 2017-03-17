# Ticket-booking-service #
Ticket booking service is able to create, delete, edit, view and list events and generate tickets for the events via email and invalidate tickets.

## Installation ##

$gitclone https://github.com/evandanu/bc-16-Ticket-booking-service

$cd bc-16-Ticket-booking-service

## Create a virtual environment ##

$python -m virtualenv project
$project\Scripts\activate
$cd bc-16-Ticket-booking-service

## Install sqlalchemy and docopt to the virtual environment ##

$python -m pip install sqlalchemy
$python -m pip install docopt

## Install dependancies ##
$python -m pip install -r requirements.txt

## To run the app ##
$python app.py


## My app is able to: ###
create_events
delete_event
edit_event
list_events
view_tickets
generate_tickets
invalidate_ticket

## Commands: ##
create_events <event_name> <event_start_date> <event_end_date> <event_venue>
delete_event <id>
edit_event <id> <event_name> <event_start_date> <event_end_date> <event_venue>
list_events
view_ticket <event_id>
generate_tickets <email> <event_name>
ticket_invalidate <event_id>


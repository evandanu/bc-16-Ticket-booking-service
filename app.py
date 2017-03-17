#!/usr/bin/env python
"""
Usage:
    interface.py create_events <event_name> <event_start_date> <event_end_date> <event_venue> [--timeout=<seconds>]
    interface.py delete_event <id>
    interface.py edit_event <id> <event_name> <event_start_date> <event_end_date> <event_venue>
    interface.py list_events
    interface.py view_tickets <event_id>
    interface.py generate_tickets <email> <event_name>
    interface.py ticket_invalidate <event_id>
    interface.py (-i | --interactive)
    interface.py (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit

import functions
from tabulate import tabulate



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyTicketBookingService (cmd.Cmd):
    intro = 'Welcome to my Ticket Booking Service' \
    + ' (type help for a list of commands.)'
    prompt = '(my_ticket_booking_service) '
    file = None

    @docopt_cmd
    def do_create_events(self, args):
        """Usage: create_events <event_name> <event_start_date> <event_end_date> <event_venue> [--timeout=<seconds>]"""
        event_name=args['<event_name>']
        event_start_date=args['<event_start_date>']
        event_end_date=args['<event_end_date>']
        event_venue=args['<event_venue>']

        print (functions.create_events(event_name,event_start_date,event_end_date,event_venue))
    @docopt_cmd
    def do_delete_event(self, arg):
        """Usage: delete_event <event_id>"""
        event_id=arg['<event_id>']

        print(functions.delete_event(event_id))

    @docopt_cmd
    def do_edit_event(self, args):
        """Usage: edit_event <event_id> <event_name> <event_start_date> <event_end_date> <event_venue>"""
        event_id=args['<event_id>']
        event_name=args['<event_name>']
        event_start_date=args['<event_start_date>']
        event_end_date=args['<event_end_date>']
        event_venue=args['<event_venue>']


        print(functions.edit_event(event_id, event_name, event_start_date, event_end_date, event_venue))

    @docopt_cmd
    def do_list_events(self, arg):
        """Usage: list_events"""


        print(tabulate(functions.list_events(), headers=["id", "event_name", "event_start_date", "event_end_date", "event_venue"], tablefmt='orgtbl'))

    @docopt_cmd
    def do_view_tickets(self, arg):
        """Usage: view_tickets <event_id>"""
        event_id=arg['<event_id>']

        print(tabulate(functions.view_tickets(event_id), headers=["id", "event_id", "ticket_status"], tablefmt='orgtbl'))

    @docopt_cmd
    def do_generate_tickets(self,arg):
        """Usage: generate_tickets <email> <event_name>"""
        event_name=arg['<event_name>']
        email = arg['<email>']
        

       

        print (functions.generate_tickets(email, event_name))


    @docopt_cmd
    def do_ticket_invalidate(self, arg):
        """Usage: tickets_invalidate <event_id>"""
        event_id=arg['<event_id>']
      


        print(functions.ticket_invalidate(event_id))


    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    print(__doc__)
    MyTicketBookingService().cmdloop()

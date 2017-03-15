#!/usr/bin/env python
"""
Usage:
    Ticket_Booking create_events 
    Ticket_Booking (-i | --interactive)
    Ticket_Booking(-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit

import methods



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
    def do_create_event(self, args):
        """Usage: create_events <event_name> <event_start_date> <event_end_date> <event_venue> [--timeout=<seconds>]"""
        event_name=args['<event_name>']
        event_start_date=args['<event_start_date>']
        event_end_date=args['<event_end_date>']
        event_venue=args['<event_venue>']

        print (self.create_events.create_event(event_name,event_start_date,event_end_date,event_venue))

    @docopt_cmd
    def do_delete_events(self, arg):
        """Usage: edit_events <event_id> [--timeout=<seconds>]"""

        print(arg)

    def do_edit_events(self, arg):
        """Usage: edit_events <event_id> [--timeout=<seconds>]"""

        print(arg)

    def do_list_events(self, arg):
        """Usage: list_events <event_id> [--timeout=<seconds>]"""

        print(arg)

    def do_view_events(self, arg):
        """Usage: view_events <event_id> [--timeout=<seconds>]"""

        print(arg)

    def do_generate_tickets(self, arg):
        """Usage: generate_tickets <email> <ticket_id> [--timeout=<seconds>]"""

        print(arg)


    def do_ticket_invalidate(self, arg):
        """Usage: tickets_invalidate <ticket_id> [--timeout=<seconds>]"""

        print(arg)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    print(__doc__)
    MyTicketBookingService().cmdloop()

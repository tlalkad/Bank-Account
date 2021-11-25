from menu import Menu, AddEvent, ListCalendar, ListEventsICalendarCommand, ExitCommand

def main():
    calendar = []
    menu = Menu()
    menu.add_command(AddEvent(calendar))
    menu.add_command(ListCalendar(calendar))
    menu.add_command(ListEventsICalendarCommand(calendar))
    menu.add_command(ExitCommand(menu))
    menu.run()


if __name__ == "__main__":
    main()

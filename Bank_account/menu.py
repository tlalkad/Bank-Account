from calendar import ListingStrategyICalendar, list_calendar

class MenuCommand:
    def description(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        self.menu = menu

    def description(self):
        return "Exit"

    def execute(self):
        self.menu.stop()


class Menu:
    def __init__(self):
        self._should_running = True
        self._commands = []

    def add_command(self, cmd):
        self._commands.append(cmd)

    def run(self):
        while self._should_running:
            for i, cmd in enumerate(self._commands, start=1):
                print("{}. {}".format(i, cmd.description()))

            cmd_num = int(input("Enter number: "))

            self._commands[cmd_num - 1].execute()

    def stop(self):
        self._should_running = False


class AddEvent(MenuCommand):
    def __init__(self, menu_all):
        self.menu_all = menu_all

    def description(self):
        return "Add event"


    def execute(self):
        global datet
        while True:
            try:
                title = input("Enter title: ")
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break

        while True:
            try:
                datet= input("Enter date (DD.MM.YYYY): ")
                # datet = datetime.datetime.strptime(datet, "%d.%m.%Y").date()
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break

        import time
        while True:
            try:
                timet = input("Enter time (HH:MM): ")
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        event = {}
        event['title'] = title
        event['date'] = datet
        event['time'] = timet
        self.menu_all.append(event)


class ListCalendar(MenuCommand):
    def __init__(self, menu_all):
        self.menu_all = menu_all

    def description(self):
        return "List Calendar"

    def execute(self):
        for event in self.menu_all:
            print(f'title:{event["title"]}')
            print(f'date:{event["date"]}, {event["time"]}')

class ListEventsICalendarCommand(MenuCommand):
    def __init__(self, calendar):
        self._calendar = calendar

    def description(self):
        return "List all events in iCalendar format"

    def execute(self):
        listing = ListingStrategyICalendar()
        list_calendar(self._calendar, listing)

class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass


class ListingStrategyStandard(ListingStrategy):
    def event(self, title, date, time):
        print(f'Title: {title}\n'
              f'Date: {date}, {time}')


class ListingStrategyICalendar(ListingStrategy):
    def begin(self):
        print('BEGIN:VCALENDAR\n'
              'VERSION:2.0\n'
              'BEGIN:VTIMEZONE\n'
              'TZID:Europe/Warsaw\n'
              'X-LIC-LOCATION:Europe/Warsaw\n'
              'END:VTIMEZONE')

    def event(self, title, date, time):
        temp_date = date.split('.')
        temp_date[0], temp_date[2] = temp_date[2], temp_date[0]
        output = ''
        for el in temp_date:
            output += el
        output += 'T'
        time = time.replace(':', '')
        time += '00'
        output += time
        print('BEGIN:VEVENT\n'
              f'DTSTART:{output}\n'
              f'DTEND:{output}\n'
              f'SUMMARY:{title}\n'
              'END:VEVENT')

    def end(self):
        print('END:VCALENDAR')


def list_calendar(calendar, listing_strategy):
    listing_strategy.begin()

    for event in calendar:
        title = event['title']
        date = event['date']
        time = event['time']
        listing_strategy.event(title, date, time)

    listing_strategy.end()
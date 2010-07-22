from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar, monthrange
from datetime import date, timedelta


class EventsCalendar(HTMLCalendar):

    def __init__(self, pEvents):
        super(EventsCalendar, self).__init__()
        self.events = self.group_by_day(pEvents)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                cssclass += ' filled'
                body = []
                for event in self.events[day]:
                    body.append('<a href="%s">' % event.get_absolute_url())
                    body.append(esc(event.title))
                    body.append('</a><br/>')
                return self.day_cell(cssclass, '<div class="dayNumber">%d</div> %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, '<div class="dayNumber">%d</div>' % day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventsCalendar, self).formatmonth(year, month)

    def group_by_day(self, pEvents):
        field = lambda events: events.start_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(pEvents, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)
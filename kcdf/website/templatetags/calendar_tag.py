from django import template
register = template.Library()
from kcdf.website.models import *
from django.utils.safestring import mark_safe
from kcdf.website.events_calendar import EventsCalendar
from datetime import date, timedelta


def named_month(pMonthNumber):
    """
    Return the name of the month, given the month number
    """
    return date(1900, pMonthNumber, 1).strftime('%B')


@register.inclusion_tag('website/partials/month_cal.html')
def events_cal():
	lYear=date.today().year
	lMonth =date.today().month
	event_list = Events.objects.filter(start_date__year=lYear, start_date__month=lMonth )
	lCalendar = EventsCalendar(event_list).formatmonth(lYear, lMonth )
	lPreviousYear = lYear
	lPreviousMonth = lMonth - 1
	if lPreviousMonth == 0:
		lPreviousMonth = 12
		lPreviousYear = lYear - 1
	lNextYear = lYear
	lNextMonth = lMonth + 1
	if lNextMonth == 13:
		lNextMonth = 1
		lNextYear = lYear + 1
	lYearAfterThis = lYear + 1
	lYearBeforeThis = lYear - 1
	return {'Calendar' : mark_safe(lCalendar),
							'Month' : lMonth,
                                                       'MonthName' : named_month(lMonth),
                                                       'Year' : lYear,
                                                       'PreviousMonth' : lPreviousMonth,
                                                       'PreviousMonthName' : named_month(lPreviousMonth),
                                                       'PreviousYear' : lPreviousYear,
                                                       'NextMonth' : lNextMonth,
                                                       'NextMonthName' : named_month(lNextMonth),
                                                       'NextYear' : lNextYear,
                                                       'YearBeforeThis' : lYearBeforeThis,
                                                       'YearAfterThis' : lYearAfterThis,}

	
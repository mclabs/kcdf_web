from django.contrib.syndication.feeds import Feed
from website.models import News,Program,ResourceType,Resource,Page,Events

class LatestNews(Feed):
	title = "KCDF News"
	link = "/"
	description = "Updates on news on kcdf.or.ke"

	def items(self):
		return News.objects.order_by('-created_at')[:10]
		
class LatestEvents(Feed):
	title = "KCDF Events"
	link = "/"
	description = "Updates on events on kcdf.or.ke"

	def items(self):
		return Events.objects.order_by('-created_at')[:10]
	
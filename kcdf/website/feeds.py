from django.contrib.syndication.feeds import Feed
from website.models import News,Program,ResourceType,Resource,Page

class LatestNews(Feed):
	title = "KCDF News"
	link = "/"
	description = "Updates on news on kcdf.or.ke"

	def items(self):
		return News.objects.order_by('created_at')[:5]
	
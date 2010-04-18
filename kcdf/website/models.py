from django.db import models
from tinymce import models as tinymce_models
from tagging.fields import TagField
from sorl.thumbnail.fields import ThumbnailField
from django.db.models import permalink



class Page(models.Model):
	title=models.CharField(max_length=160,help_text="title of the page e.g. About KCDF")
	content=tinymce_models.HTMLField()
	parent=models.ForeignKey('self',related_name="sub_pages", null=True, blank=True)
	slug=models.SlugField(max_length=160,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Page"
		verbose_name_plural="Pages"
		
		
	

class Program(models.Model):
	title=models.CharField(max_length=160,help_text="title of the program")
	description=models.TextField(help_text="Description of the program")
	slug=models.SlugField(max_length=160)

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="KCDF Program"
		verbose_name_plural="KCDF Programs"

	def get_absolute_url(self):
		return "/program/%s/" % self.slug
		
		

class ResourceType(models.Model):
	resource_type=models.CharField(max_length=100,help_text="resource type e.g. PDF")

	def __unicode__ (self):
		return self.resource_type

	class Meta:
		verbose_name="Resource Type"
		verbose_name_plural="Resource Types"


class BaseResource(models.Model):
	title=models.CharField(max_length=160,help_text="title of the item",db_index=True)
	short_description=models.TextField(help_text="short description (160) characters",null=True)
	long_description=tinymce_models.HTMLField(help_text="long description of the case study")
	url=models.URLField(verify_exists=True,max_length=200,blank=True,null=True,help_text="website link if exists")
	slug=models.SlugField(unique=True)
	created_at=models.DateTimeField(auto_now_add=True)
	tags = TagField()

	class Meta:
		abstract=True
		

	def __unicode__ (self):
		return self.title


class CaseStudy(BaseResource):
	program=models.ForeignKey(Program,help_text="Program the case study belongs to",db_index=True)

	class Meta:
		verbose_name="KCDF Case Study"
		verbose_name_plural="KCDF Case Studies"

	

class Resource(BaseResource):
	resource_type=models.ForeignKey(ResourceType,db_index=True)
	resource_file=models.FileField(upload_to='resource/%Y/%m/%d',blank=True,null=True)

	class Meta:
		verbose_name="KCDF Resource"
		verbose_name_plural="KCDF Resources"



class News(BaseResource):
	news_file=models.FileField(upload_to='news/%Y/%m/%d',blank=True,null=True)

	class Meta:
		verbose_name="KCDF News"
		verbose_name_plural="KCDF News"


		

class Events(BaseResource):
	event_doc=models.FileField(upload_to='events/%Y/%m/%d',blank=True,null=True)

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="KCDF Event"
		verbose_name_plural="KCDF Events"

class Headline(models.Model):
	title=models.CharField(max_length=100)
	photo=models.ImageField(upload_to='headlines/%Y/%m/%d')
	thumbnail=ThumbnailField(upload_to='headlines/thumbnails/%Y/%m/%d',size=(69, 39))
	
	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Home Page Headline"
		verbose_name_plural="Home Page Headlines"


'''Add models here for SMS data which will be populated via web hooks'''
		

	
	
		
	
		
	
	
		
	
from django.db import models
from tinymce import models as tinymce_models
from tagging.fields import TagField
from sorl.thumbnail.fields import ThumbnailField
from django.db.models import permalink
from django.template.defaultfilters import slugify



class Page(models.Model):
	title=models.CharField(max_length=160,help_text="title of the page e.g. About KCDF")
	content=tinymce_models.HTMLField()
	parent=models.ForeignKey('self',related_name="sub_pages", null=True, blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Page"
		verbose_name_plural="Pages"
		
	def get_absolute_url(self):
		return "/page/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.title)
		super(Page,self).save()

	

		
	

class Program(models.Model):
	title=models.CharField(max_length=160,help_text="title of the program")
	short_description=tinymce_models.HTMLField(help_text="Short Description of the program")
	description=tinymce_models.HTMLField(help_text="Description of the program")
	slug=models.SlugField(max_length=255,blank=True)

	def __unicode__ (self):
		return self.title
	
	def save (self):
		self.slug = slugify(self.title)
		super(Program,self).save()

	class Meta:
		verbose_name="KCDF Program"
		verbose_name_plural="KCDF Programs"


	def get_absolute_url(self):
		return "/program/%s/" % self.slug
	
	def save (self):
		self.slug = slugify(self.title)
		super(Program,self).save()
		
		

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
	slug=models.SlugField(max_length=255,unique=True)
	created_at=models.DateTimeField(auto_now_add=True)
	tags = TagField()

	class Meta:
		abstract=True
		

	def __unicode__ (self):
		return self.title

	def save (self):
		self.slug = slugify(self.title)
		super(BaseResource,self).save()


class CaseStudy(BaseResource):
	program=models.ForeignKey(Program,help_text="Program the case study belongs to",db_index=True,null=True, blank=True)

	class Meta:
		verbose_name="KCDF Case Study"
		verbose_name_plural="KCDF Case Studies"

	def get_absolute_url(self):
		return "/case-study/%s/" % self.slug

	

class Resource(BaseResource):
	resource_type=models.ForeignKey(ResourceType,db_index=True)
	resource_file=models.FileField(upload_to='resource/%Y/%m/%d',blank=True,null=True)
	program=models.ForeignKey(Program,help_text="Program the case study belongs to",db_index=True,null=True, blank=True)

	class Meta:
		verbose_name="KCDF Resource"
		verbose_name_plural="KCDF Resources"

	def get_absolute_url(self):
		return "/resource/%s/" % self.slug




class News(BaseResource):
	program=models.ForeignKey(Program,help_text="Program the case study belongs to",db_index=True,null=True, blank=True)
	news_file=ThumbnailField("Large Image",upload_to='news/%Y/%m/%d',size=(500, 250),help_text="Supported file format is PNG only!!. Image dimensions 400x250",blank=True,null=True)
	news_date=models.DateField(auto_now=False, auto_now_add=False);

	class Meta:
		verbose_name="KCDF News"
		verbose_name_plural="KCDF News"

	def get_absolute_url(self):
		return "/news/%s" % self.slug

		

class Events(BaseResource):
	event_doc=models.FileField(upload_to='events/%Y/%m/%d',blank=True,null=True)
	program=models.ForeignKey(Program,help_text="Program the case study belongs to",db_index=True,null=True, blank=True)
	event_date=models.DateField(auto_now=False, auto_now_add=False);
	start_date=models.DateTimeField(auto_now=False, auto_now_add=False);
	end_date=models.DateTimeField(auto_now=False, auto_now_add=False);

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="KCDF Event"
		verbose_name_plural="KCDF Events"

	def get_absolute_url(self):
		return "/events/%s/" % self.slug


class Headline(models.Model):
	STATUS=(
        ('1', 'Active'),
        ('0', 'Inactive'),
	)
	title=models.CharField(max_length=255)
	snippet=tinymce_models.HTMLField(help_text="short snippet (50) characters")
	#photo=models.ImageField("Large Image",upload_to='headlines/%Y/%m/%d',help_text="Supported file format is PNG only!!")
	photo=ThumbnailField("Large Image",upload_to='headlines/%Y/%m/%d',size=(500, 250),help_text="Supported file format is PNG only!!. Image dimensions 400x250")
	slug=models.SlugField(max_length=255,unique=True)
	thumbnail=ThumbnailField("Small Image",upload_to='headlines/thumbnails/%Y/%m/%d',size=(69, 39),help_text="Supported file format is PNG only!!")
	status=models.CharField("Headline Status",max_length=1,default='Active',choices=STATUS,help_text="Set whether this is the active headline")
	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Home Page Headline"
		verbose_name_plural="Home Page Headlines"
	
		
	def save (self):
		self.slug = slugify(self.title)
		super(Headline,self).save()

	def get_thumbnail(self):
		return self.thumbnail
		
	def get_large_image(self):
		return self.photo

	

class Video(models.Model):
	STATUS=(
        ('1', 'Active'),
        ('0', 'Inactive'),
	)
	title=models.CharField(max_length=255)
	snippet=models.TextField(help_text="short snippet (50) characters")
	slug=models.SlugField(max_length=255,unique=True)
	video=models.FileField("Video",upload_to='videos/%Y/%m/%d',help_text="Please convert all videos to FLV format before uploading",null=True, blank=True)
	flvname=models.CharField(max_length=255,unique=True,help_text="name of video including extension e.g. kcdf.flv")
	status=models.CharField("Video Status",max_length=1,default='Active',choices=STATUS,help_text="Set whether this is the active video")
	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Video"
		verbose_name_plural="Videos"
	
		
	def save (self):
		self.slug = slugify(self.title)
		super(Video,self).save()

	def get_absolute_url(self):
		return "/videos/%s/" % self.slug

class Audio(models.Model):
	
	title=models.CharField(max_length=255)
	snippet=models.TextField(help_text="short description about (100) characters")
	slug=models.SlugField(max_length=255,unique=True)
	audiofile=models.FileField("Video",upload_to='audios/%Y/%m/%d',help_text="Please convert all audios to mp3",null=True, blank=True)
	audio_file_name=models.CharField(max_length=255,unique=True,help_text="name of audio file including extension e.g. kcdf.flv")
	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Audio"
		verbose_name_plural="Audio files"
	
		
	def save (self):
		self.slug = slugify(self.title)
		super(Audio,self).save()

	def get_absolute_url(self):
		return "/audio/%s/" % self.slug


class Downloads(models.Model):
	download_type=models.ForeignKey(ResourceType,db_index=True)
	title=models.CharField(max_length=255)
	downloadfile=models.FileField("File",upload_to='uploads/%Y/%m/%d',help_text="select file from local drive")
	description=models.TextField(help_text="short snippet (50) characters")
	slug=models.SlugField(max_length=255,unique=True)

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Download"
		verbose_name_plural="Downloads"
	
		
	def save (self):
		self.slug = slugify(self.title)
		super(Downloads,self).save()

	def get_absolute_url(self):
		return "/downloads/%s/" % self.slug
	

class Stats(models.Model):
	programs=models.CharField(max_length=255,help_text="number of programs")
	communities=models.CharField(max_length=255)
	families=models.CharField(max_length=255)
	people=models.CharField(max_length=255)
	cash_target=models.CharField(max_length=255,help_text="number of programs")

	def __unicode__ (self):
		return self.programs

	class Meta:
		verbose_name="KCDF Stats"
		verbose_name_plural="KCDF Stats"

class Subscription(models.Model):
	name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)

	def __unicode__ (self):
		return self.name

	class Meta:
		verbose_name="KCDF Newsletter Subscription"
		verbose_name_plural="KCDF Newsletter Subscriptions"


class Location(models.Model):
    name = models.CharField(max_length=100, help_text="Name of location")
    code = models.CharField(max_length=30, unique=True)
    latitude  = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True, help_text="The physical latitude of this location")
    longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True, help_text="The physical longitude of this location")
    
    
    def __unicode__(self):
        return self.name

class Grantee(models.Model):
	PERIOD=(
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),

	)

	name=models.CharField(max_length=255,help_text="Name of the grantee")
	description=tinymce_models.HTMLField(help_text="long description of the grantee")
	start_year=models.CharField("Grantee Period",max_length=10,default='2003',choices=PERIOD)
	end_year=models.CharField("Grantee Period",max_length=10,default='2003',choices=PERIOD)
	program=models.ForeignKey(Program,help_text="Program the grantee belongs to",db_index=True,null=True, blank=True)
	amount=models.CharField(max_length=255,help_text="Amount Grantee Donated")
	location=models.ForeignKey(Location,help_text="District they belong to",db_index=True,null=True, blank=True)
	slug=models.SlugField(max_length=255)


	def __unicode__ (self):
		return self.name

	class Meta:
		verbose_name="Grantee"
		verbose_name_plural="Grantees"
	
		
	def save (self):
		self.slug = slugify(self.name)
		super(Grantee,self).save()

	def get_absolute_url(self):
		return "/grantee/%i/" % self.id


'''Add models here for SMS data which will be populated via web hooks'''
		

	
	
		
	
		
	
	
		
	
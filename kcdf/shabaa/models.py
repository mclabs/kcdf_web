from django.db import models
from tinymce import models as tinymce_models
from tagging.fields import TagField
from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField
from kcdf.website.models import Location

class OrganisationCategory(models.Model):
	title=models.CharField(max_length=255)

	def __unicode__ (self):
		return self.title

	class Meta:
		verbose_name="Organisation Category"
		verbose_name_plural="Organisation Categories"

class OrganisationType(models.Model):
	title=models.CharField(max_length=255)

	def __unicode__ (self):
		return self.title
	class Meta:
		verbose_name="Organisation Type"
		verbose_name_plural="Organisation Types"


class Funder(models.Model):
	organisation_name=models.CharField(max_length=255)
	organisation_type=models.ForeignKey(OrganisationType,help_text="Type of Organisation",db_index=True)
	organisation_category=models.ForeignKey(OrganisationCategory,help_text="Category organisation belongs to",db_index=True)
	mission=tinymce_models.HTMLField(null=True,blank=True)
	geographical_coverage=tinymce_models.HTMLField(null=True,blank=True)
	eligibility=tinymce_models.HTMLField(null=True,blank=True)
	funding_partners=tinymce_models.HTMLField(null=True,blank=True)
	implementing_partners=tinymce_models.HTMLField(null=True,blank=True)
	physical_address=tinymce_models.HTMLField(null=True,blank=True)
	postal_address=tinymce_models.HTMLField(null=True,blank=True)
	landline=models.CharField(max_length=255,null=True,blank=True)
	mobile=models.CharField(max_length=255,null=True,blank=True)
	fax=models.CharField(max_length=100,null=True,blank=True)
	email=models.CharField(max_length=100,null=True,blank=True)
	website=models.CharField(max_length=100,null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.organisation_name

	class Meta:
		verbose_name="Funder"
		verbose_name_plural="Funders"
		
	def get_absolute_url(self):
		return "/funder/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.organisation_name)
		super(Funder,self).save()


class ServiceType(models.Model):
	title=models.CharField(max_length=255)

	def __unicode__ (self):
		return self.title

	
class ServiceProvider(models.Model):
	organisation_name=models.CharField(max_length=255)
	service_type=models.ForeignKey(ServiceType,help_text="Type of Service Organisation provides",db_index=True)
	description=tinymce_models.HTMLField(null=True,blank=True)
	funding_partners=tinymce_models.HTMLField(null=True,blank=True)
	implementing_partners=tinymce_models.HTMLField(null=True,blank=True)
	physical_address=tinymce_models.HTMLField(null=True,blank=True)
	postal_address=tinymce_models.HTMLField(null=True,blank=True)
	landline=models.CharField(max_length=255,null=True,blank=True)
	mobile=models.CharField(max_length=255,null=True,blank=True)
	fax=models.CharField(max_length=100,null=True,blank=True)
	email=models.CharField(max_length=100,null=True,blank=True)
	website=models.CharField(max_length=100,null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.organisation_name

	class Meta:
		verbose_name="Service Provider"
		verbose_name_plural="Service Providers"
		
	def get_absolute_url(self):
		return "/service-provider/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.organisation_name)
		super(ServiceProvider,self).save()


class LegalDocument(models.Model):
	title=models.CharField(max_length=255)
	qualification=tinymce_models.HTMLField(null=True,blank=True)
	requirements=tinymce_models.HTMLField(null=True,blank=True)
	fee=tinymce_models.HTMLField(null=True,blank=True)
	application_place=tinymce_models.HTMLField(null=True,blank=True)
	head_office=tinymce_models.HTMLField(null=True,blank=True)
	postal_address=tinymce_models.HTMLField(null=True,blank=True)
	landline=models.CharField(max_length=255,null=True,blank=True)
	mobile=models.CharField(max_length=255,null=True,blank=True)
	fax=models.CharField(max_length=100,null=True,blank=True)
	email=models.CharField(max_length=100,null=True,blank=True)
	website=models.CharField(max_length=100,null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.title
	
	class Meta:
		verbose_name="Legal Document"
		verbose_name_plural="Legal Documents"
		
	def get_absolute_url(self):
		return "/legal-document/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.title)
		super(LegalDocument,self).save()


class BusinessRegistration(models.Model):
	business_type=models.CharField(max_length=255)
	requirements=tinymce_models.HTMLField(null=True,blank=True)
	frequency=models.CharField(max_length=25,help_text="How many times you have to apply for the license",null=True,blank=True)
	organisation=models.CharField(max_length=255,help_text="Organisation that facilitates this business registration",null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)
	
	def __unicode__ (self):
		return self.business_type
	
	class Meta:
		verbose_name="Business Registration"
		verbose_name_plural="Business Registrations"
		
	def get_absolute_url(self):
		return "/business-registration/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.business_type)
		super(BusinessRegistration,self).save()


class IndividualRegistration(models.Model):
	organisation_name=models.CharField(max_length=255)
	description=tinymce_models.HTMLField(null=True,blank=True)
	requirements=tinymce_models.HTMLField(null=True,blank=True)
	cost=models.CharField(max_length=100,null=True,blank=True)
	physical_address=tinymce_models.HTMLField(null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.organisation_name

	def get_absolute_url(self):
		return "/individual-registration/%s/" % self.slug
	
	class Meta:
		verbose_name="Individual Registration"
		verbose_name_plural="Individual Registrations"

	def save (self):
		self.slug = slugify(self.organisation_name)
		super(IndividualRegistration,self).save()


class YouthProgram(models.Model):
	title=models.CharField(max_length=255,help_text="title of the program")
	description=models.TextField()
	geographical_coverage=models.TextField()
	funding_partners=models.TextField()
	implementing_partners=models.TextField()
	contacts=models.TextField()
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.title

	def get_absolute_url(self):
		return "/youth-program/%s/" % self.slug

	class Meta:
		verbose_name="Youth Program"
		verbose_name_plural="Youth Programs"

	def save (self):
		self.slug = slugify(self.title)
		super(YouthProgram,self).save()


class Bank(models.Model):
	name=models.CharField(max_length=255)
	target=models.CharField(max_length=255)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return "/bank/%s/" % self.slug

	class Meta:
		verbose_name="Bank"
		verbose_name_plural="Banks"

	def save (self):
		self.slug = slugify(self.title)
		super(Bank,self).save()


class NationalPark(models.Model):
	name=models.CharField(max_length=255)
	climate=tinymce_models.HTMLField(null=True,blank=True)
	description=tinymce_models.HTMLField(null=True,blank=True)
	location=models.CharField(max_length=255)
	slug=models.SlugField(blank=True,null=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return "/national-park/%s/" % self.slug


	class Meta:
		verbose_name="National Park"
		verbose_name_plural="National Parks"

	def save (self):
		self.slug = slugify(self.name)
		super(NationalPark,self).save()


class ProjectPartner(models.Model):
	name=models.CharField(max_length=255,help_text="Name of project or partner")
	location=models.ForeignKey(Location,help_text="Location of the project")
	partnership_year=models.CharField(max_length=50,help_text="year of partnership")


	
	def get_absolute_url(self):
		return "/partner/%s/" % self.id

	def __unicode__ (self):
		return self.name

	class Meta:
		verbose_name="Shabaa Project Partner"
		verbose_name_plural="Shabaa Project Partners"


'''
class License(models.Model):
	title=models.CharField(max_length=255)
	licensing_body=models.CharField(max_length=255)
	purpose=models.TextField()
	activities=models.TextField()
	requirements=models.TextField()
	fee=models.TextField()
	
'''

	
# Create your models here.

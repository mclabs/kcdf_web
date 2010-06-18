from django.db import models
from tinymce import models as tinymce_models
from tagging.fields import TagField
from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField

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
	mission=models.TextField(null=True,blank=True)
	geographical_coverage=models.TextField(null=True,blank=True)
	eligibility=models.TextField(null=True,blank=True)
	funding_partners=models.TextField(null=True,blank=True)
	implementing_partners=models.TextField(null=True,blank=True)
	physical_address=models.TextField(null=True,blank=True)
	postal_address=models.TextField(null=True,blank=True)
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
	description=models.TextField(null=True,blank=True)
	funding_partners=models.TextField(null=True,blank=True)
	implementing_partners=models.TextField(null=True,blank=True)
	physical_address=models.TextField(null=True,blank=True)
	postal_address=models.TextField(null=True,blank=True)
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
		return "/service/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.organisation_name)
		super(ServiceProvider,self).save()


class LegalDocument(models.Model):
	title=models.CharField(max_length=255)
	qualification=models.TextField(null=True,blank=True)
	requirements=models.TextField(null=True,blank=True)
	fee=models.TextField(null=True,blank=True)
	application_place=models.TextField(null=True,blank=True)
	head_office=models.TextField(null=True,blank=True)
	postal_address=models.TextField(null=True,blank=True)
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
		return "/legal_document/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.title)
		super(LegalDocument,self).save()


class BusinessRegistration(models.Model):
	business_type=models.CharField(max_length=255)
	requirements=models.TextField(null=True,blank=True)
	frequency=models.CharField(max_length=25,help_text="How many times you have to apply for the license",null=True,blank=True)
	organisation=models.CharField(max_length=255,help_text="Organisation that facilitates this business registration",null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)
	
	def __unicode__ (self):
		return self.business_type
	
	class Meta:
		verbose_name="Business Registration"
		verbose_name_plural="Business Registrations"
		
	def get_absolute_url(self):
		return "/business_registration/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.business_type)
		super(BusinessRegistration,self).save()


class IndividualRegistration(models.Model):
	organisation_name=models.CharField(max_length=255)
	description=models.TextField(null=True,blank=True)
	requirements=models.TextField(null=True,blank=True)
	cost=models.CharField(max_length=100,null=True,blank=True)
	physical_address=models.TextField(null=True,blank=True)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.organisation_name
	
	class Meta:
		verbose_name="Individual Registration"
		verbose_name_plural="Individual Registrations"

	def save (self):
		self.slug = slugify(self.organisation_name)
		super(IndividualRegistration,self).save()


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

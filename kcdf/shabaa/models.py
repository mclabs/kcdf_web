from django.db import models
from tinymce import models as tinymce_models
from tagging.fields import TagField
from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField

class OrganisationCategory(models.Model):
	title=models.CharField(max_length=255)

	def __unicode__ (self):
		return self.title


class OrganisationType(models.Model):
	title=models.CharField(max_length=255)

	def __unicode__ (self):
		return self.title


class Funder(models.Model):
	organisation_name=models.CharField(max_length=255)
	organisation_type=models.ForeignKey(OrganisationType,help_text="Type of Organisation",db_index=True)
	organisation_category=models.ForeignKey(OrganisationCategory,help_text="Category organisation belongs to",db_index=True)
	mission=models.TextField()
	geographical_coverage=models.TextField()
	eligibility=models.TextField()
	funding_partners=models.TextField()
	implementing_partners=models.TextField()
	physical_address=models.TextField()
	postal_address=models.TextField()
	landline=models.CharField(max_length=255)
	mobile=models.CharField(max_length=255)
	fax=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	website=models.CharField(max_length=100)
	slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)

	def __unicode__ (self):
		return self.organisation_name

	class Meta:
		verbose_name="Funder"
		verbose_name_plural="Funders"
		
	def get_absolute_url(self):
		return "/funder/%s/" % self.slug

	def save (self):
		self.slug = slugify(self.title)
		super(Funder,self).save()


class ServiceType(models.Model):
	title=models.CharField(max_length=255)

	def __unicode__ (self):
		return self.title

	
class ServiceProvider(models.Model):
	organisation_name=models.CharField(max_length=255)
	service_type=models.ForeignKey(ServiceType,help_text="Type of Service Organisation provides",db_index=True)
	description=models.TextField()
	funding_partners=models.TextField()
	implementing_partners=models.TextField()
	physical_address=models.TextField()
	postal_address=models.TextField()
	landline=models.CharField(max_length=255)
	mobile=models.CharField(max_length=255)
	fax=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	website=models.CharField(max_length=100)
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
	qualification=models.TextField()
	requirements=models.TextField()
	fee=models.TextField()
	application_place=models.TextField()
	head_office=models.TextField()
	postal_address=models.TextField()
	landline=models.CharField(max_length=255)
	mobile=models.CharField(max_length=255)
	fax=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	website=models.CharField(max_length=100)
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

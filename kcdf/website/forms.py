from django import forms
from django.conf import settings
from sorl.thumbnail.fields import ThumbnailField,ImageWithThumbnailsField
from website.widgets import AdminImageWidget
from website.models import *

class AdminImageForm(forms.ModelForm):
    '''
    Basic form to handle wiring up the AdminImageWidget to your
    model that has a 'file' field. This assumes your models
    has a file field. If it doesn't then don't use this form
    but create your own.
    
    '''
    
    photo = forms.FileField(widget=AdminImageWidget, required=True)
    thumbnail = forms.FileField(widget=AdminImageWidget, required=True)

class NewsletterSubscribeForm(forms.ModelForm):
	name=forms.CharField(label="Name",max_length=110,required=True,widget=forms.TextInput(attrs={'class':'long_text'}))
	email=forms.CharField(label="Email Address",required=True,widget=forms.TextInput(attrs={'class':'long_text'}))

	''' Additional validation that's called just after the form'''
	def clean_name(self):
		name=self.cleaned_data.get('name','')
		if len(name.split())==0:
			raise forms.ValidationError("Please enter your name")
		if len(name)>140:
			raise forms.ValidationError("The name is to long")
		return name
		
		

	def save(self):
		subscription = Subscription(name = self.cleaned_data['name'], 
					email = self.cleaned_data['email']
						)
		subscription.save()
		return subscription
	
	
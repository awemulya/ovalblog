from django.db import models
from django.utils import timezone
import datetime
import django_filters

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days = 1) <= self.pub_date <= now 
	was_published_recently.admin_order_field = 'pub_date' 
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def save(self, *args, **kwargs):
		if not self.id:
			self.choice_text = 'No Default Choice'
		super(Choice , self).save(*args , **kwargs)

	def __unicode__(self):
		return self.choice_text

class Manufacturer(models.Model):
	country = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.country

class Product(models.Model):
	name = models.CharField(max_length = 225)
	price = models.DecimalField(decimal_places = 2, max_digits = 20)
	description = models.TextField()
	release_date = models.DateField()
	manufacturer = models.ForeignKey(Manufacturer)

class ProductFilter(django_filters.FilterSet):
	price = django_filters.NumberFilter(lookup_type = 'lt')
	class Meta:
		model = Product
		fields = ['price' , 'manufacturer']
		order_by = (('name', 'Company Name'),('manufacturer' , 'Products Of'),)

	def __init__(self , *args, **kwargs):
		super(ProductFilter , self).__init__(*args ,**kwargs)
		self.filters['manufacturer'].extra.update({'empty_label':'All Manufacturers'})

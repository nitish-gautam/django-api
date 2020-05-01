from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 50)
	productcode = models.CharField(max_length = 50)
	producttype = models.CharField(max_length = 50)
	price = models.CharField(max_length = 10)

	def __str__(self):
		return self.name +" " + self.productcode 



from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

class User(models.Model):
	username = models.CharField(
		validators = [MinLengthValidator(3), MaxLengthValidator(20)],
		unique = True
	)
	email = models.EmailField(unique = True)
	password = models.CharField(validators = [MinLengthValidator(8)])

PRICE_BY = {
	'NIGHT': 'NIGHT',
	'GUEST': 'GUEST'
}

class Property(models.Model):
	address = models.CharField(validators = [MaxLengthValidator(200)])
	owner = models.ForeignKey(User, on_delete = models.CASCADE)
	price = models.FloatField(validators = [MinValueValidator(0.01)])
	priceBy = models.CharField(choices = PRICE_BY)
	max_guests = models.IntegerField(validators = [MinValueValidator(1)])
	description = models.CharField(validators = [MaxLengthValidator(400)])

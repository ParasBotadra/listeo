from django.db import models

# Create your models here.

class PopularCategories(models.Model):
	category_name = models.CharField(max_length=50)
	icon_class = models.CharField(max_length=70, null=True, blank=True)

	def __str__(self):
		return self.category_name

	def get_places_count(self):
		return MostVisitedPlaces.objects.filter(category=self).count()

class MostVisitedPlaces(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=150)
	description = models.CharField(max_length=150)
	image = models.ImageField()
	category = models.ForeignKey(PopularCategories, on_delete=models.CASCADE)
	ratings = models.IntegerField()

	def __str__(self):
		return self.name

	def get_review_count(self):
		return Reviews.objects.filter(place=self).count()

class Reviews(models.Model):
	place = models.ForeignKey(MostVisitedPlaces, on_delete=models.CASCADE)
	review = models.CharField(max_length=200)

	def __str__(self):
		return "{0} - {1}".format(self.place.name, self.review)



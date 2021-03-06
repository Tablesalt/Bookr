from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

#idk about on_delete, might have made some mistakes there.
#probably helps that there is no way to delete users
class BookType(models.Model):
	isbn = models.BigIntegerField()
	title = models.CharField(max_length=200, default='No title found')
	author = models.CharField(max_length=200, default='No authors found')
	picture = models.ImageField(null=True, upload_to='bookr/images/scraped/')

class Book(models.Model):
	booktype = models.ForeignKey(BookType, on_delete=models.CASCADE, null=True)
	picture = models.ImageField(null=True, upload_to='bookr/images/uploaded/')
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.FloatField()
	condition = models.CharField(max_length=100)

@receiver(models.signals.post_delete, sender=Book)
def delete_contact(sender, instance, **kwargs):
	if not Book.objects.filter(contact=instance.booktype):
		instance.booktype.delete()

class Wish(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Seller(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	rating = models.IntegerField(null=True)
	avatar = models.ImageField()

class Contact(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	PHONE = 'PH'
	EMAIL = 'EM'
	CONTACT_TYPE_CHOICES = (
		(PHONE, 'Phone'),
		(EMAIL, 'Email'),
	)
	contact_type = models.CharField(max_length=2, choices=CONTACT_TYPE_CHOICES, default=PHONE)
	contact_text = models.CharField(max_length=40)

class Review(models.Model):
	#these related_names might cause issues?????!?!?!?!!!
	rater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raters')
	ratee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratees')
	stars = models.IntegerField()
	text = models.TextField()
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	STAR_CHOICES = (
		(ONE, '★☆☆☆☆'),
		(TWO, '★★☆☆☆'),
		(THREE, '★★★☆☆'),
		(FOUR, '★★★★☆'),
		(FIVE, '★★★★★'),
	)
	stars = models.IntegerField(choices=STAR_CHOICES, default=THREE)


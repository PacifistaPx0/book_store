from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


# / creates a database table called books which has a title, rating etc columns
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[
                                 MinValueValidator(1.0), MaxValueValidator(5.0)])
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-details", kwargs={"slug": self.slug})

    def __str__(self):  # / used to convert an object to a string for /admin/
        return f"{self.title} ({self.rating})"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        'Address', on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.postal_code} {self.street} {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"
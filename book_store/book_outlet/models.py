from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} - {self.code}"

    class Meta:
        verbose_name_plural = 'Country Entries'
class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)

    def full_address(self):
        return f"{self.street} {self.city}, {self.postal_code}"

    def __str__(self):
        return self.full_address()

    class Meta:
        verbose_name_plural = 'Address Entries'

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True
                                    ,related_name='author')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
class Book(models.Model):
    title=models.CharField(max_length=100)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    author=models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling=models.BooleanField(default=False)
    slug=models.SlugField(default = '', null=False, db_index=True, blank=True)
    published_countries=models.ManyToManyField(Country)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])

    def __str__(self):
        return f"{self.title} -  {self.author} ({self.rating})"
from django.db import models

from django.urls import reverse

# Create your models here.

class Category(models.Model): # it is inheritance: it is inheriting form models.Model to access its
                            # properties

    name = models.CharField(max_length=255, db_index=True)

    # Slug is used for unique, readable URLs (e.g., categories/books/)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):

    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    
    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=4)

    slug = models.SlugField(max_length=250)

    image = models.ImageField(upload_to='image/')

    class Meta:

        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product-info", args=[self.slug])
    
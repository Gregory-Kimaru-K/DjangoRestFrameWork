from django.db import models
import string
import random

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def generate_unique_slug(self):
        characters = string.ascii_letters + string.digits + string.punctuation

        slug = ''.join(random.choices(characters, k=13))

        while Task.objects.filter(slug=slug).exists():
            slug = ''.join(random.choices(characters, k=13))

        return slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
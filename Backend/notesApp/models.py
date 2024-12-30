from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.
class Note(models.Model):
    CATEGORY = (
        ("BUSINESS", "Business"),
        ("PERSONAL", "Personal"),
        ("IMPORTANT", "Important"),
    )

    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=200, choices=CATEGORY,default="PERSONAL")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(self.title)
            slug = slug_base
            if Note.objects.filter(slug=slug).exists():
                self.slug = f"{slug_base}-{get_random_string(length=5)}"
        super(Note, self).save(*args, **kwargs)

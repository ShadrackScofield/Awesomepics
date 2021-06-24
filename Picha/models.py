from django.db import models


# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=150)
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.name


class Dog_pics(models.Model):
    name = models.CharField(max_length=150)
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/dogs/')

    class Meta:
        verbose_name_plural = 'Dogs'

    def __str__(self):
        return self.name


class Tech_pics(models.Model):
    name = models.CharField(max_length=150)
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/tech/')

    class Meta:
        verbose_name_plural = 'Techies'

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class Category(models.Model):
    c_name = models.CharField(max_length=256)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.c_name


class Title(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='media')
    data = models.DateTimeField(auto_now_add=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=256)
    user_title = models.ForeignKey(Title, on_delete=models.CASCADE)
    user_comment = models.TextField(blank=True)
    user_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    login = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.login


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title} | {self.body[:50]}...'
from django.db import models

class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=50)
    text = models.TextField('Описание')
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
from django.db import models

from main.models import MyUser


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'BookJournal'
        verbose_name_plural = 'BookJournals'
        abstract = True

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.name, self.price, self.description, self.created_at)


class Book(BookJournalBase):
    GENRE = (
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Western', 'Western'),
        ('Historical', 'Historical'),
    )
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(choices=GENRE, max_length=200, default='Drama')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.name, self.price, self.num_pages, self.genre)


class Journal(BookJournalBase):
    TYPE = (
        ('Bullet', 'Bullet'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Sport', 'Sport'),
    )
    type = models.CharField(choices=TYPE, max_length=200, default='Bullet')
    publisher = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.name, self.price, self.type, self.publisher)

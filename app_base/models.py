from dataclasses import fields
from django.db import models
from django.contrib.auth import get_user_model
import datetime


USER = get_user_model()


GENDER = (
    ('-', '-'),
    ('Diverse', 'Diverse'),
    ('Female', 'Female'),
    ('Male', 'Male'),
)


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False, choices=GENDER, default=GENDER[0][1])
    born = models.DateField(null=False, blank=False)
    died = models.DateField(null=True, blank=True)
    passed = models.BooleanField(default=False)
    created_from = models.ForeignKey(USER, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            models.UniqueConstraint(fields=['last_name', 'first_name'], name="unique autor constraint")
        ]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def save(self, *args, **kwargs):
        self.passed = True if self.died is not None else False
        super(Author, self).save(*args, **kwargs)

    @property
    def age(self):
        if self.passed:
            return self.died.year - self.born.year
        else:
            now = datetime.datetime.today()
            return now.year - self.born.year

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    author = models.ForeignKey(Author, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    created_from = models.ForeignKey(USER, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'author']
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name="unique book constraint")
        ]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return self.title
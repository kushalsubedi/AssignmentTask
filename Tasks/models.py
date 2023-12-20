from django.db import models

from django.contrib.auth.models import User
# Create your models here.

priorities = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=10, choices=priorities, default='Low', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    submission_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

from django.db import models


class Category(models.Model):
    name       = models.CharField(max_length=100, unique=True)
    color      = models.CharField(max_length=7, default='#6366f1')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = [
        ('pending',     'Pending'),
        ('in_progress', 'In Progress'),
        ('done',        'Done'),
    ]

    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status      = models.CharField(
                      max_length=20,
                      choices=STATUS_CHOICES,
                      default='pending'
                  )
    completed   = models.BooleanField(default=False)
    category    = models.ForeignKey(
                      Category,
                      on_delete=models.SET_NULL,
                      null=True,
                      blank=True,
                      related_name='tasks'
                  )
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
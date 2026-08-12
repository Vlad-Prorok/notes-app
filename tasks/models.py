from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    priority_choices = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, default='medium')
    
    def __str__(self):
        return f'{self.title} ({self.get_priority_display()})'

# Create your models here.

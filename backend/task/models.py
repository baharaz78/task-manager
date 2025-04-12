from django.contrib.auth.models import User
from django.db import models

from core.models import AbstractBaseModel
from kafka_producer import send_task_event


class Task(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
    )
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        task_data = {
            'task_id': self.id,
            'title': self.title,
            'status': self.status,
            'description': self.description,
            'assigned_to': self.assigned_to.username,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

        send_task_event(task_data)

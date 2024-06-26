from django.db import models


# Create your models here.
class Topic(models.Model):
    text = models.TextField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "topics"

    # Return string representing the model
    def __str__(self):
        return f"{self.text[:50]}"


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.topic.text

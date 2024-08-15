from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.video.title} by {self.text[:20]}'


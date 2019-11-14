from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, db_index=True)
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return "{}".format(self.title)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'url'], name='unique_title_url_combo'),
        ]
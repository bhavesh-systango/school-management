from django.db import models

from django.db import models

from authentication.models import CustomUser

class Post(models.Model):

    title = models.CharField(max_length = 200, unique = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    class Meta:

        ordering = ['-created_on']

    def __str__(self):

        return self.title


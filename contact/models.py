from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=112)
    number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
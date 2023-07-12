from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='authors/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name() != "":
            return self.user.get_full_name()
        return self.user.username


def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)


post_save.connect(user_post_save, sender=User)
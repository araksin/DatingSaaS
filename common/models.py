from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Profile(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    premium = models.BooleanField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    description = models.TextField()


class ProfilePhoto(models.Model):
    is_main = models.BooleanField(default=False)
    path = models.TextField()


class Like(models.Model):
    class Meta:
        unique_together = ('giver', 'receiver')

    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    giver = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='like_givers_set')
    receiver = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='like_accessors_set')

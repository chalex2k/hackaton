from django.db import models
from django.contrib.auth.models import User


class ContestModel(models.Model):
    CONTEST_TYPE = (
        (0, 'individual'),
        (1, 'command'),
    )
    CONTEST_FORMAT = (
        (0, 'task_based'),
        (1, '???'),
    )
    name = models.TextField(blank=False)
    description = models.TextField(blank=False)
    datetime_start = models.DateTimeField(blank=False)
    datetime_end = models.DateTimeField(blank=False)
    organizer = models.ForeignKey('UserModel', related_name='contests', on_delete=models.DO_NOTHING)
    city = models.ForeignKey('CityModel', on_delete=models.DO_NOTHING)
    format = models.TextField(default=0, choices=CONTEST_FORMAT)
    feeding = models.BooleanField()
    difficulty = models.IntegerField()
    type = models.IntegerField(default=0, choices=CONTEST_TYPE)
    active = models.BooleanField(default=False, blank=False)
    employer = models.TextField(default='', blank=False)
    image_path = models.ImageField(upload_to="img") # todo move to config
    participants = models.ManyToManyField("UserModel", through='ContestParticipantThroughModel')
    # title = models.CharField(max_length=100, blank=True, default='')
    # body = models.TextField(blank=True, default='')
    # owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datetime_start']


class TeamModel(models.Model):
    name = models.CharField(max_length=255)


class UserModel(User):
    USER_TYPE = [
        (0, "sportsman"),
        (1, "partner"),
        (2, "regional"),
        (3, "admin")
    ]

    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    type = models.IntegerField(default=0, choices=USER_TYPE)
    city = models.ForeignKey('CityModel', on_delete=models.DO_NOTHING)
    models.ForeignKey(TeamModel, related_name='members', on_delete=models.CASCADE, null=True)


class CityModel(models.Model):
    name = models.CharField(blank=False, max_length=255)


class ContestParticipantThroughModel(models.Model):
    contest_id = models.ForeignKey('ContestModel', on_delete=models.DO_NOTHING)
    participant_id = models.ForeignKey('UserModel', on_delete=models.DO_NOTHING)
    position = models.IntegerField()
    positive_feedback = models.TextField()
    negative_feedback = models.TextField()
    common_feedback = models.TextField()
    mark_feedback = models.IntegerField()
    mark_difficulty = models.IntegerField()
    mark_interest = models.IntegerField()
    mark_organization = models.IntegerField()
    mark_quality = models.IntegerField()


class ContestPartnersModel(models.Model):
    contest_id = models.ForeignKey('ContestModel', on_delete=models.DO_NOTHING)
    participant_id = models.ForeignKey('UserModel', on_delete=models.DO_NOTHING)


class Favorites(models.Model):

    user = models.CharField(max_length=255)
    contest = models.ForeignKey(ContestModel, on_delete=models.CASCADE, related_name="favorites")
    on_create = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['user', 'contest'])]

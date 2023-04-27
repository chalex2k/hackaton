from django.db import models


class Contest(models.Model):
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
    organizer = models.ForeignKey('auth.User', related_name='contests', on_delete=models.DO_NOTHING)
    city = models.TextField(blank=True)  # TODO FK
    format = models.TextField(default=0, choices=CONTEST_FORMAT)  # TODO FK
    feeding = models.BooleanField()
    difficulty = models.IntegerField()
    type = models.IntegerField(default=0, choices=CONTEST_TYPE)
    active = models.BooleanField(default=False, blank=False)
    employer = models.TextField(default='', blank=False)
    image_path = models.TextField(default='', blank=False)
    participants = models.ManyToManyField("auth.User", through='ContestParticipant')
    # title = models.CharField(max_length=100, blank=True, default='')
    # body = models.TextField(blank=True, default='')
    # owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datetime_start']


class City(models.Model):
    name = models.TextField(blank=False)


class ContestParticipant(models.Model):
    contest_id = models.ForeignKey('Contest', on_delete=models.DO_NOTHING)
    participant_id = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    position = models.IntegerField()
    positive_feedback = models.TextField()
    negative_feedback = models.TextField()
    common_feedback = models.TextField()
    mark_feedback = models.IntegerField()


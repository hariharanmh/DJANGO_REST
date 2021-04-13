from django.db import models
from django.core.exceptions import ValidationError

#basic validation
def validate_participants(value):
    if value.startswith('[') and value.endswith(']') and len(value[1:-1].split(',')) <= 10:
        if all([True if not len(str(participant)) > 100 else False for participant in value[1:-1].split(',')]):
            return value
        else:
            return ValidationError("This field accepts only list as string and list of sting should be ")
    else:
        return ValidationError("This field accepts only list as string")

class AudioFile(models.Model):
    audio_file_id = models.IntegerField(primary_key=True)
    audio_file_types = [('Song', 'Song'), ('Podcast', 'Podcast'), ('Audiobook', 'Audiobook')]
    audio_file_type = models.CharField(max_length=16, choices=audio_file_types)
    date_of_entry = models.DateTimeField(auto_now_add=True, editable=True)
    date_of_update = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return str(self.audio_file_id)

class Song(models.Model):
    song_id = models.ForeignKey(AudioFile, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(null=True, blank=True)
    uploaded_time = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return str(self.song_id)

class Podcast(models.Model):
    podcast_id = models.ForeignKey(AudioFile, on_delete=models.CASCADE)
    podcast_name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now=True, editable=True)
    host = models.CharField(max_length=100)
    # SQLite don't heve deticated list field, so we are using CharField insted
    participants = models.CharField(max_length=1020, validators =[validate_participants])

    def __str__(self):
        return str(self.podcast_id)

class Audiobook(models.Model):
    audiobook_id = models.ForeignKey(AudioFile, on_delete=models.CASCADE)
    audiobook_title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now=True, editable=True)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)

    def __str__(self):
        return str(self.audiobook_id)
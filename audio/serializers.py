from rest_framework import serializers
from .models import AudioFile, Song, Podcast, Audiobook

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('audio_file_id', 'audio_file_type')


class SongSerializer(serializers.ModelSerializer):
    # audio = AudioFileSerializer()

    class Meta:
        model = Song
        fields = ('song_name', 'duration')

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('podcast_name', 'duration', 'host', 'participants')

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ('audiobook_title', 'duration', 'author', 'narrator')
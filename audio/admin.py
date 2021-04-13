from django.contrib import admin
from .models import AudioFile, Song, Podcast, Audiobook


@admin.register(AudioFile)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('audio_file_id', 'audio_file_type', 'date_of_entry', 'date_of_update')
    readonly_fields = ('date_of_entry', 'date_of_update')
    ordering = ('-date_of_update',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_id', 'song_name', 'duration', 'uploaded_time')
    
@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('podcast_id', 'podcast_name', 'duration', 'uploaded_time', 'host', 'participants')
    
@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('audiobook_id', 'audiobook_title', 'duration', 'uploaded_time', 'author', 'narrator')
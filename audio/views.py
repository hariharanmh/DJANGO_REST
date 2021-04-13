from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from .models import AudioFile, Song, Podcast, Audiobook


def overview(request):
    return JsonResponse("API Overview", safe=False)


# Base Class to handle all the Audio Endpoints
class AudioView(APIView):

    def get(self, request, audio_file_type=None, audio_file_id=None):
        try:

            if audio_file_type or audio_file_id:
                audio_file_type = audio_file_type.capitalize()

                if audio_file_type == 'Song':
                    if audio_file_id:
                        songs = Song.objects.filter(song_id=audio_file_id)
                    else:
                        songs = Song.objects.all()
                    if songs:
                        serialized_song = SongSerializer(songs, many=True)
                        return Response(
                            serialized_song.data,
                            status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {'Message': 'No Song found'},
                            status=status.HTTP_204_NO_CONTENT
                        )

                elif audio_file_type == 'Podcast':
                    if audio_file_id:
                        podcasts = Podcast.objects.filter(
                            podcast_id=audio_file_id)
                    else:
                        podcasts = Podcast.objects.all()
                    if podcasts:
                        serialized_podcast = PodcastSerializer(
                            podcasts, many=True)
                        return Response(
                            serialized_podcast.data,
                            status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {'Message': 'No Podcast found'},
                            status=status.HTTP_204_NO_CONTENT
                        )

                elif audio_file_type == 'Audiobook':
                    if audio_file_id:
                        audiobooks = Audiobook.objects.filter(
                            audiobook_id=audio_file_id)
                    else:
                        audiobooks = Audiobook.objects.all()
                    if audiobooks:
                        serialized_audiobook = AudiobookSerializer(
                            audiobooks, many=True)
                        return Response(
                            serialized_audiobook.data,
                            status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {'Message': 'No Audiobook found'},
                            status=status.HTTP_204_NO_CONTENT
                        )
                else:
                    return Response(
                        {'Status': 'Error', 'Message': 'Check audio file type'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            else:
                songs = Song.objects.all()
                podcasts = Podcast.objects.all()
                audiobooks = Audiobook.objects.all()
                serialized_song = SongSerializer(songs, many=True)
                serialized_podcast = PodcastSerializer(podcasts, many=True)
                serialized_audiobook = AudiobookSerializer(
                    audiobooks, many=True)
                return Response(
                    {
                        'songs': serialized_song.data,
                        'podcasts': serialized_podcast.data,
                        'audiobooks': serialized_audiobook.data
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {'Status': 'Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, audio_file_type=None, audio_file_id=None):
        try:

            audio_file_type = request.data['audio_file_type'].capitalize()
            audio_file_metadata = request.data['audio_file_metadata']
            
            if audio_file_type == 'Song':
                song_serializer = SongSerializer(data=audio_file_metadata)
                if song_serializer.is_valid():
                    AudioFile.objects.create(audio_file_type=audio_file_type)
                    audio = AudioFile.objects.latest('date_of_entry')
                    song_serializer.save(song_id=audio)
                    return Response(
                        song_serializer.data,
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {'Status': 'Error', 'Message': 'Invalid data'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
            
            elif audio_file_type == 'Podcast':
                podcast_serializer = PodcastSerializer(data=audio_file_metadata)
                if podcast_serializer.is_valid():
                    AudioFile.objects.create(audio_file_type=audio_file_type)
                    audio = AudioFile.objects.latest('date_of_entry')
                    podcast_serializer.save(podcast_id=audio)
                    return Response(
                        podcast_serializer.data,
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {'Status': 'Error', 'Message': 'Invalid data'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            elif audio_file_type == 'Audiobook':
                audiobook_serializer = AudiobookSerializer(data=audio_file_metadata)
                if audiobook_serializer.is_valid():
                    AudioFile.objects.create(audio_file_type=audio_file_type)
                    audio = AudioFile.objects.latest('date_of_entry')
                    audiobook_serializer.save(audiobook_id=audio)
                    return Response(
                        audiobook_serializer.data,
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {'Status': 'Error', 'Message': 'Invalid data'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            else:
                return Response(
                    {'Status': 'Error', 'Message': 'Check audio file type'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print('^^', e)
            return Response(
                {'Status': 'Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, audio_file_type=None, audio_file_id=None):
        try:
            if audio_file_type and audio_file_id:
                audio_file_type = audio_file_type.capitalize()

                if audio_file_type == 'Song':
                    song = Song.objects.filter(song_id=audio_file_id).first()
                    if song:
                        song_serializer = SongSerializer(song, data=request.data)
                        if song_serializer.is_valid():
                            song_serializer.save()
                            return Response(
                                song_serializer.data,
                                status=status.HTTP_200_OK
                            )
                        else:
                            return Response(
                                {'Status': 'Error', 'Message': 'Invalid data'},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {'Message': 'No Song found'},
                            status=status.HTTP_204_NO_CONTENT
                        )
                
                elif audio_file_type == 'Podcast':
                    podcast = Podcast.objects.filter(podcast_id=audio_file_id).first()
                    if podcast:
                        podcast_serializer = PodcastSerializer(podcast, data=request.data)
                        if podcast_serializer.is_valid():
                            podcast_serializer.save()
                            return Response(
                                podcast_serializer.data,
                                status=status.HTTP_200_OK
                            )
                        else:
                            return Response(
                                {'Status': 'Error', 'Message': 'Invalid data'},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {'Message': 'No Podcast found'},
                            status=status.HTTP_204_NO_CONTENT
                        )

                elif audio_file_type == 'Audiobook':
                    audiobook = Audiobook.objects.filter(audiobook_id=audio_file_id).first()
                    if audiobook:
                        audiobook_serializer = AudiobookSerializer(audiobook, data=request.data)
                        if audiobook_serializer.is_valid():
                            audiobook_serializer.save()
                            return Response(
                                audiobook_serializer.data,
                                status=status.HTTP_200_OK
                            )
                        else:
                            return Response(
                                {'Status': 'Error', 'Message': 'Invalid data'},
                                status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {'Message': 'No Audiobook found'},
                            status=status.HTTP_204_NO_CONTENT
                        )
                else:
                    return Response(
                        {'Status': 'Error', 'Message': 'Check audio file type'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'Status': 'Error', 'Message': 'Missing argument'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {'Status': 'Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, audio_file_type=None, audio_file_id=None):
        try:

            if audio_file_type and audio_file_id:
                audio_file_type = audio_file_type.capitalize()

                if audio_file_type in ['Song', 'Podcast', 'Audiobook']:
                    audio = AudioFile.objects.filter(
                        audio_file_id=audio_file_id)
                    if audio:
                        audio.delete()
                        return Response(
                            {'Message': 'Audio Deleted'},
                            status=status.HTTP_200_OK
                        )
                    else:
                        return Response(
                            {'Message': 'No Audio found'},
                            status=status.HTTP_204_NO_CONTENT
                        )
                else:
                    return Response(
                        {'Status': 'Error', 'Message': 'Check audio file type'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'Status': 'Error', 'Message': 'Missing argument'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return Response(
                {'Status': 'Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# DJANGO_REST
DJANGO REST 

Implementation of create, read, upload, and delete endpoints for an audio file as defined below:

Create API:
  The request will have the following fields:
    - audioFileType – mandatory, one of the 3 audio types possible
    - audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook)

Delete API:
    - The route will be in the following format: “<audioFileType>/<audioFileID>”

Update API:
    - The route be in the following format: “<audioFileType>/<audioFileID>”
    - The request body will be the same as the upload
Get API:
    - The route “<audioFileType>/<audioFileID>” will return the specific audio file
    - The route “<audioFileType>” will return all the audio files of that type
    
    
Audio file type can be one of the following:
  1 – Song
  2 – Podcast
  3 – Audiobook

  Song file fields:
    - ID – (mandatory, integer, unique)
    - Name of the song – (mandatory, string, cannot be larger than 100 characters)
    - Duration in number of seconds – (mandatory, integer, positive)
    - Uploaded time – (mandatory, Datetime, cannot be in the past)
  Podcast file fields:
    - ID – (mandatory, integer, unique)
    - Name of the podcast – (mandatory, string, cannot be larger than 100 characters)
    - Duration in number of seconds – (mandatory, integer, positive)
    - Uploaded time – (mandatory, Datetime, cannot be in the past)
    - Host – (mandatory, string, cannot be larger than 100 characters)
    - Participants – (optional, list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible)
  Audiobook file fields:
    - ID – (mandatory, integer, unique)
    - Title of the audiobook – (mandatory, string, cannot be larger than 100 characters)
    - Author of the title (mandatory, string, cannot be larger than 100 characters)
    - Narrator - (mandatory, string, cannot be larger than 100 characters)
    - Duration in number of seconds – (mandatory, integer, positive)
    - Uploaded time – (mandatory, Datetime, cannot be in the past)

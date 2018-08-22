from mutagen.mp3 import MP3
mp3 = MP3('remove_tags.mp3')
mp3.delete()
mp3.save()
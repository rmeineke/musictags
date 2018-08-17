from mutagen import File

file = File('a.mp3')
print(f'{type(file)}')
print(f'{mutagen.File(a.mp3)}')
# artwork = file.tags['APIC:'].data
#
# with open('image.jpg', 'wb') as img:
#     img.write(artwork)  # write artwork to new image

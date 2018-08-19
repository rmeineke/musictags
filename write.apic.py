#
# > from mutagen import id3, mp3
# > file = mp3.MP3('test.mp3')
# > imagedata = open('cover.png', 'rb').read()
# > file.tags.add(id3.APIC(3, 'image/png', 3, 'Front cover', imagedata))
# > file.save()
# >

from mutagen import id3, mp3
file = mp3.MP3('test.mp3')
imagedata = open('bw_duke.jpg', 'rb').read()
file.tags.add(id3.APIC(encoding=3, desc='Description goes here.', type=3, data=imagedata))
file.save()


#
# class mutagen.id3.APIC(encoding=<Encoding.UTF16: 1>, mime=u'', type=<PictureType.COVER_FRONT: 3>, desc=u'', data='')
#
#     Bases: mutagen.id3.Frame
#
#     Attached (or linked) Picture.
#
#     Attributes:
#
#         encoding – text encoding for the description
#         mime – a MIME type (e.g. image/jpeg) or ‘–>’ if the data is a URI
#         type – the source of the image (3 is the album front cover)
#         desc – a text description of the image
#         data – raw image data, as a byte string
#
#     Mutagen will automatically compress large images when saving tags.

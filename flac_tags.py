import os
from mutagen import File


def main():
    tags_found = []
    for root, dirs, files in os.walk("/home/robertm/programming"):
        for file in files:
            if file.endswith(".flac"):
                f = os.path.join(root, file)
                mutobj = File(f, easy=True)
                stray_tags = []
                for i in mutobj:
                    if i not in tags_found:
                        tags_found.append(i)
                    if (
                        i == "title"
                        or i == "tracknumber"
                        or i == "albumartist"
                        or i == "date"
                        or i == "tracktotal"
                        or i == "album"
                        or i == "artist"
                        or i == "discnumber"
                    ):
                        # print(f"{mutobj['title'][0]}")
                        continue
                    else:
                        stray_tags.append(i)
                if stray_tags:
                    print(
                        f"........................................................................"
                    )
                    print(f"STRAYS: {f}")
                    for j in stray_tags:
                        print(f"{mutobj[j][0]}")
                        print(f"{j}")
    print(f"--------------------------------------------------------")
    print(f"{tags_found}")


if __name__ == "__main__":
    main()


# title
# date
# tracknumber
# albumartist
# tracktotal
# album
# artist
# discnumber
# 02 - Corned Beef City.flac:METADATA block #1
# 02 - Corned Beef City.flac:  type: 4 (VORBIS_COMMENT)
# 02 - Corned Beef City.flac:  is last: false
# 02 - Corned Beef City.flac:  length: 706
# 02 - Corned Beef City.flac:  vendor string: reference libFLAC 1.2.1 20070917
# 02 - Corned Beef City.flac:  comments: 26
# 02 - Corned Beef City.flac:    comment[0]: TITLE=Corned Beef City
# 02 - Corned Beef City.flac:    comment[1]: ARTIST=Knopfler, Mark
# 02 - Corned Beef City.flac:    comment[2]: ALBUMARTIST=Mark Knopfler
# 02 - Corned Beef City.flac:    comment[3]: ALBUM=Tracker US-Live in-Berkeley-2015-09-18
# 02 - Corned Beef City.flac:    comment[4]: DATE=2015
# 02 - Corned Beef City.flac:    comment[5]: TRACKNUMBER=02
# 02 - Corned Beef City.flac:    comment[6]: TRACKTOTAL=15
# 02 - Corned Beef City.flac:    comment[7]: GENRE=Folk Blues Pop Rock
# 02 - Corned Beef City.flac:    comment[8]: DESCRIPTION=www.bleecker-street-shop.com
# 02 - Corned Beef City.flac:    comment[9]: _MarkerListVersion=2
# 02 - Corned Beef City.flac:    comment[10]: _MarkerCount=15
# 02 - Corned Beef City.flac:    comment[11]: Marker1=535604 bb
# 02 - Corned Beef City.flac:    comment[12]: Marker2=16846390 cbc
# 02 - Corned Beef City.flac:    comment[13]: Marker3=33603157 priv
# 02 - Corned Beef City.flac:    comment[14]: Marker4=55985262 fshf
# 02 - Corned Beef City.flac:    comment[15]: Marker5=83637851 sd
# 02 - Corned Beef City.flac:    comment[16]: Marker6=104041450 lajadas
# 02 - Corned Beef City.flac:    comment[17]: Marker7=125338830 lt
# 02 - Corned Beef City.flac:    comment[18]: Marker8=144747923 rj
# 02 - Corned Beef City.flac:    comment[19]: Marker9=172143981 sos
# 02 - Corned Beef City.flac:    comment[20]: Marker10=194206922 pfp
# 02 - Corned Beef City.flac:    comment[21]: Marker11=223311094 mt
# 02 - Corned Beef City.flac:    comment[22]: Marker12=258759763 san
# 02 - Corned Beef City.flac:    comment[23]: Marker13=279030131 tr
# 02 - Corned Beef City.flac:    comment[24]: Marker14=325432886 sofa
# 02 - Corned Beef City.flac:    comment[25]: Marker15=344777501 lh
# 02 - Corned Beef City.flac:METADATA block #2
# :

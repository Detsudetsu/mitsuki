import mutagen
from pathlib import Path

album_dir = Path("Peachy!")

for i, file in enumerate(album_dir.iterdir(), 1):
    chim = mutagen.File(file)
    chim.tags["DISCNUMBER"] = str(1)
    chim.tags["TRACKNUMBER"] = str(i)
    chim.tags["TITLE"] = ""
    chim.tags["ARTIST"] = ""
    chim.tags["ALBUM"] = ""
    chim.tags["ALBUMARTIST"] = [""]
    chim.save()

    filename = "Track " + str(i).zfill(2) + file.suffix
    file.rename(album_dir / filename)

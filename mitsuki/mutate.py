import mutagen

chim = mutagen.File("不明なタイトル/1.01. トラック01.flac")
chim.tags["DISCNUMBER"] = str(1)
chim.tags["TRACKNUMBER"] = str(1)
chim.tags["TITLE"] = "もう気が狂う"
chim.tags["ARTIST"] = "珍宝"
chim.tags["ALBUM"] = "仏法僧"
chim.tags["ALBUMARTIST"] = ["ちんちん"]
print(chim)
chim.save()

ramu = mutagen.File("不明なタイトル/1.02. トラック02.flac")
print(ramu)
import metallum


band = metallum.Band('bands/Aephanemer')
print(band)
band = metallum.Band('bands/Aephanemer/3540375286')
print(band)
band = metallum.Band(
    'bands/' +
    'random_string_to_show_it_works_by_just_by_id_as_well/3540375286')
print(band)
# band = metallum.band_for_id('3540375286')
band = metallum.band_for_id('3540442600')

print(band)

print('band id:', band.id)
print('band url:', band.url)
print('band name:', band.name)
print('band genres:', band.genres)
print('band country of origin:', band.country)
print('band location:', band.location)
print('band status:', band.status)
print('year of band\'s creature:', band.formed_in)
print('band themes:', band.themes)
print('band label:', band.label)
print('band albums:', band.albums)

albums = band.albums
album = albums[1]

print()
print('album:', album)
print('album\'s id:', album.id)
print('album\'s url', album.url)
print('album\'s title:', album.title)
print('album\'s type:', album.type)
print('album\'s bands:', album.bands)
print('album\'s tracks:', album.tracks)
print('album\'s disc count:', album.disc_count)
print('album\'s duration (in seconds):', album.duration)
print('album\'s release date:', album.date)
# album was released independently so output is absent
print('album\'s label:')

tracks = album.tracks
track = tracks[0]

# number in parenthesis means duration in seconds
print()
print('track duration:', track.duration)
print('count of tracks in the same album:', track.overall_number)
print('disc number:', track.disc_number)
print('track\'s full title:', track.full_title)
print('track\'s title:', track.title)
print('track duration:', track.duration)
print('band that released track:', track.band)

print('---------------------------------------------------------------------')
lyrics = track.lyrics
print(lyrics)
print('---------------------------------------------------------------------')

bands = metallum.band_search('Abaddon', year_created_from='1980')
print(type(bands), bands, sep='\n')

print()
albums = metallum.album_search(title='war', strict=False, band='sabaton')
print(type(albums), albums, sep='\n')

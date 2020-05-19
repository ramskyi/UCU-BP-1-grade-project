from band_adt import BandsStatusesCollection, BandsSongsFrequencyCollection
import time
from pathlib import Path


def collect_and_store_band_data():
    status_collec = BandsStatusesCollection()
    freq_collec = BandsSongsFrequencyCollection()

    with open(Path('..') / 'polygon' / 'band_url_list.txt', 'r') as file:
        ids = file.readlines()
        for i in range(len(ids)):
            ids[i] = int(ids[i].split()[0].split('/')[-1])

    start_time = time.time()
    i = 0
    print('len = ', len(ids))
    for id_ in ids:
        i += 1

        try:
            status_collec.add(id_)
        except Exception:
            pass
        try:
            freq_collec.add(id_)
        except Exception:
            pass

        if i % 10 == 0:
            print(i, time.time() - start_time, (time.time()-start_time) / i)

    with open(Path('..') / 'polygon' / 'status_result', 'w') as file:
        file.write(str(status_collec.genre) + '\n')
        file.write(str(status_collec.songs_duration) + '\n')
        file.write(str(status_collec.genres_count) + '\n')
        file.write(str(status_collec.country) + '\n')
        file.write(str(status_collec.songs_per_album) + '\n')

    with open(Path('..') / 'polygon' / 'freq_result', 'w') as file:
        file.write(str(freq_collec.time_of_existence) + '\n')
        file.write(str(freq_collec.genre) + '\n')
        file.write(str(freq_collec.genres_count) + '\n')
        file.write(str(freq_collec.country) + '\n')
        file.write(str(freq_collec.song_duration_mean) + '\n')
        file.write(str(freq_collec.label) + '\n')

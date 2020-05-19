import re
import matplotlib.pyplot as plt
from pathlib import Path


def line_to_dict(line, index1_type, index2_type):
    """
    Takes a string which represents a dict, fixes data from line and
    returns back a dict.
    """
    dct = {}
    pattern = re.compile('\([^:]*, [^:]*\): \d*')
    data = re.findall(pattern, line)
    for item in data:
        raw_index, value = item.split(': ')
        value = int(value)

        pattern1 = re.compile('\([^,]*,')
        index1 = re.findall(pattern1, raw_index)[0][1: -1]

        pattern2 = re.compile(', .*\)')
        raw_index2 = re.findall(pattern2, raw_index)[0][2: -1]
        if raw_index2 == "''":
            continue

        index2, i, length = [], 0, len(raw_index2)
        while i < length and raw_index2[i] not in ',(':
            index2.append(raw_index2[i])
            i += 1

        index2 = ''.join(index2)

        if index1_type is str:
            index1 = index1[1: -1]
        if index2_type is str:
            index2 = list(index2[1: -1])
            while index2[-1] in ' ,()':
                del index2[-1]
            index2 = ''.join(index2)
            if index2.endswith(' Metal'):
                index2 = index2[: -6]
        index1 = index1_type(index1)
        index2 = index2_type(index2)

        if index1 not in dct:
            dct[index1] = {}
        if index2 not in dct[index1]:
            dct[index1][index2] = 0
        dct[index1][index2] += value

    return dct


def plot_lists_genre_or_country(genre_info, most_popular_genres, status):
    """
    Takes a dict with data about band (about countries of genres), list
    of genres/countries sorted by descending count of bands with that
    property, and status of bands with such data. Returns lists for
    building a bar chart.
    """
    most_status_genre = sorted(
        [(genre_info[most_popular_genres[i][1]][status],
         '\n'.join(most_popular_genres[i][1].split())) for i in range(25)])
    plot_y = [most_status_genre[i][0] for i in range(25)]
    plot_x = [most_status_genre[i][1] + '\n' + str(plot_y[i])[:4]
              for i in range(25)]
    return plot_x, plot_y


def visualize_genre_or_country(dct, code='genres'):
    """
    Takes dict of data about genres or countries and code (to visualize
    genres or countries data). Builds and shows bar charts for each
    status from it.
    """
    genre_info = {}
    most_popular_genres = []
    for genre in dct['Active']:
        total = 0
        for status in dct:
            try:
                total += dct[status][genre]
            except KeyError:
                pass

        most_popular_genres.append((total, genre))

        for status in dct:
            try:
                if genre not in genre_info:
                    genre_info[genre] = {}
                genre_info[genre][status] = dct[status][genre] / total
            except KeyError:
                pass
    most_popular_genres.sort(reverse=True)

    for status in 'Active', 'Split-up', 'Changed name', 'Unknown', 'On hold':
        plot_x, plot_y = plot_lists_genre_or_country(
            genre_info, most_popular_genres, status)
        plt.figure(figsize=(21, 12), dpi=80)
        plt.bar(plot_x, plot_y)
        plt.title(label='Share of {0} bands among 25 most popular '.
                  format(status.lower()) + code)
        plt.show()


def visualize_duration(duration_dct):
    """
    Takes dict of data about mean of song duration for bands.
    Builds and show bar charts for each status from it.
    """
    int_duration_dct = {}

    for status in duration_dct:
        if status not in int_duration_dct:
            int_duration_dct[status] = [0]*1001
        for duration in duration_dct[status]:
            if 0 < duration <= 1000:
                int_duration_dct[status][int(duration)] = \
                    int(duration_dct[status][duration])

    for status in 'Active', 'Split-up', 'Changed name', 'Unknown', 'On hold':
        plot_x = list(range(1001))
        plot_y = int_duration_dct[status]
        plt.plot(plot_x, plot_y)
        plt.title(label='Count of {0} bands with song duration mean'.
                  format(status.lower()))
        plt.xlabel('seconds')
        plt.show()


def visualize_genres_count(genres_count_dct_dct):
    """
    Takes dict of data about count of genres for a band.
    Builds and show bar charts for each status from it.
    """
    genres_count_list_dct = {'Total': [0]*8}
    for status in genres_count_dct_dct:
        if status not in genres_count_list_dct:
            genres_count_list_dct[status] = [0]*8
        for cnt in genres_count_dct_dct[status]:
            genres_count_list_dct[status][cnt] = \
                genres_count_dct_dct[status][cnt]
            genres_count_list_dct['Total'][cnt] += \
                genres_count_dct_dct[status][cnt]

    for status in 'Active', 'Split-up', 'Changed name', 'Unknown', 'On hold':
        for cnt in range(8):
            if genres_count_list_dct['Total'][cnt] != 0:
                genres_count_list_dct[status][cnt] = (
                    genres_count_list_dct[status][cnt],
                    genres_count_list_dct[status][cnt] /
                    genres_count_list_dct['Total'][cnt])
            else:
                genres_count_list_dct[status][cnt] = (0, 0)

    for status in 'Active', 'Split-up', 'Changed name', 'Unknown', 'On hold':
        func = lambda x: str(x) + '\n' + str(
            genres_count_list_dct[status][x][1])[:4] + '\n' + \
            str(genres_count_list_dct[status][x][0])[:4]
        plot_x = list(map(func, range(8)))
        plot_y = [genres_count_list_dct[status][x][1] for x in range(8)]
        plt.bar(plot_x, plot_y)
        plt.title(label='Share of {0} bands that work in several genres'.
                  format(status.lower()))
        plt.xlabel('count of genres, share, count of bands')
        plt.show()


def visualize_per_album(songs_per_album):
    """
    Takes dict of data about count of songs per an album for a band.
    Builds and show plots for each status from it.
    """
    songs_per_album['Total'] = {}
    for status in songs_per_album:
        for cnt in songs_per_album[status]:
            if cnt not in songs_per_album['Total']:
                songs_per_album['Total'][cnt] = 0
            songs_per_album['Total'][cnt] += songs_per_album[status][cnt]

    for cnt in songs_per_album['Total']:
        for status in ('Active', 'Split-up', 'Changed name', 'Unknown',
                       'On hold'):
            if cnt not in songs_per_album[status]:
                songs_per_album[status][cnt] = 0
            songs_per_album[status][cnt] = songs_per_album[status][cnt] / \
                songs_per_album['Total'][cnt]

    for status in 'Active', 'Split-up', 'Changed name', 'Unknown', 'On hold':
        plot_x = list(range(max(songs_per_album['Total'].keys()) + 1))
        plot_y = list(map(lambda x: songs_per_album[status][x]
                          if x in songs_per_album[status] else 0, plot_x))
        plt.plot(plot_x, plot_y)
        plt.title(label='Share of {0} bands with '.format(status.lower()) +
                  'mean of count of songs per album')
        plt.show()


def draw_all():
    """() -> NoneType
    Draws plots and bar charts to visualize collected data.
    """
    with open(Path('..') / 'polygon' / 'status_result', 'r') as file:
        lines = file.readlines()
        genre = line_to_dict(lines[0], str, str)
        visualize_genre_or_country(genre)
        duration = line_to_dict(lines[1], str, float)
        visualize_duration(duration)
        genres_count = line_to_dict(lines[2], str, int)
        visualize_genres_count(genres_count)
        country_dct = line_to_dict(lines[3], str, str)
        visualize_genre_or_country(country_dct, code='countries')
        songs_per_album = line_to_dict(lines[4], str, int)
        visualize_per_album(songs_per_album)


if __name__ == '__main__':
    draw_all()

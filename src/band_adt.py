import metallum


def _incr_in_dict(index, dictionary):
    """(tuple, dict) -> NoneType
    Increases item in dictionary by one, creating it, if it didn't
    exist before
    """
    if index not in dictionary:
        dictionary[index] = 0
    dictionary[index] += 1


class BandsStatusesCollection:
    """
    Represents ADT that stores quotient of the count of bands with
    specific characteristic and its current status data about bands.
    Class allows to get data by band id on www.metal-archives.com

    Attributes:
    + genre: dict((str, str), int)
        Stores count of bands of certain status that play songs of
        certain genre
    + songs_duration: dict((str, float), int)
        Stores count of bands of certain status that have certain mean of
        song duration
    + genres_count: dict((str, int), int)
        Stores count of bands of certain status that work using certain
        count of genres
    + countries: dict((str, str), int)
        Stores count of bands of certain status with origin in certain
        country
    + songs_per_album: dict((str, float), int)
        Stores count of bands of certain status that have certain mean
        of song count in single album

    Methods:
    + __init__(): NoneType
        Initialization
    + add(int): bool
        Adds data about band given by id to class object
    """

    def __init__(self):
        """() -> NoneType
        """
        self.genre = {}
        self.songs_duration = {}
        self.genres_count = {}
        self.country = {}
        self.songs_per_album = {}

    def add(self, id_):
        """(int) -> NoneType
        Recalculates data considering new band with given id. Returns
        False if there is no band with such id or no data for a band
        with such id, True otherwise
        """
        band = metallum.band_for_id(str(id_))

        # Checking if band and data about it does exist
        if str(band) == '<Band: >' or band.status == '' or \
                band.genres == [''] or band.country == '':
            return False
        try:
            albums = band.albums
        except TypeError:
            return False
        status = band.status

        # Collecting data on genres of the band
        genres_count = 0
        for curr_genre in band.genres:
            curr_genre = curr_genre.split('/')
            for genre in curr_genre:
                genres_count += 1
                _incr_in_dict((status, genre), self.genre)
        _incr_in_dict((status, genres_count), self.genres_count)

        # Collecting data in songs duration mean and count of songs per
        # one album mean
        summary_duration = 0
        tracks_count = 0
        for album in albums:
            _incr_in_dict((status, len(album.tracks)),
                          self.songs_per_album)
            summary_duration += album.duration
            tracks_count += len(album.tracks)
        _incr_in_dict((status, summary_duration / tracks_count),
                      self.songs_duration)

        # Collecting data on country of band's origin
        _incr_in_dict((status, band.country), self.country)
        
        return True


class BandsSongsFrequencyCollection:
    """
    Represents ADT that stores quotient of the count of bands with
    specific characteristics and its frequency of songs producing.

    Attributes:
    + self.time_of_existence: dict((float, int), int)
        Stores count of bands with certain frequency of songs
        production and certain count of years since origin
    + self.genre: dict((float, str), int)
        Stores count of bands with certain frequency of songs
        production and certain genre
    + self.genres_count: dict((float, int), int)
        Stores count of bands with certain frequency of songs
        production and certain count of genres
    + self.country: dict((float, str), int)
        Stores Stores count of bands with certain frequency of songs
        production and certain country of origin
    + self.song_duration_mean: dict((float, float), int)
        Stores count of bands with certain frequency of songs
        production and certain mean of songs duration
    + self.label: dict((float, bool), int)
        Stores count of bands with certain frequency of songs
        production and which have label or don't

    Methods:
    + __init__(): NoneType
        Initialization
    + add(int): bool
        Adds data about band given by id to class object
    """

    def __init__(self):
        """() -> NoneType
        """
        self.time_of_existence = {}
        self.genre = {}
        self.genres_count = {}
        self.country = {}
        self.song_duration_mean = {}
        self.label = {}

    def add(self, id_):
        """(int) -> NoneType
        Recalculates data considering new band with given id. Returns
        False if there is no band with such id or no data for a band
        with such id, True otherwise
        """
        band = metallum.band_for_id(str(id_))
        if str(band) == '<Band: >' or band.genres == [''] or \
                band.country == '' or band.label == '':
            return False
        try:
            albums = band.albums
        except TypeError:
            return False
        time_of_exis = 2020 - int(band.formed_in)

        # How many songs produced a band
        songs_count = 0
        for album in band.albums:
            songs_count += len(album.tracks)
        # Songs producing frequency
        freq = songs_count / time_of_exis

        # Collecting data on existence time
        _incr_in_dict((freq, time_of_exis), self.time_of_existence)

        # Collecting data on genres
        genres_count = 0
        for curr_genre in band.genres:
            curr_genre = curr_genre.split('/')
            for genre in curr_genre:
                genres_count += 1
                _incr_in_dict((freq, genre), self.genre)
        _incr_in_dict((freq, genres_count), self.genres_count)

        # Collecting data on country
        _incr_in_dict((freq, band.country), self.country)

        # Collecting data on song duration mean
        summary_duration = 0
        track_count = 0
        for album in band.albums:
            summary_duration += album.duration
            track_count += len(album.tracks)
        mean = summary_duration / track_count
        _incr_in_dict((freq, mean), self.song_duration_mean)

        # Collecting data on band label
        signed_to_label = 'unsigned' not in band.label.lower() and \
            'independent' not in band.label.lower()
        _incr_in_dict((freq, signed_to_label), self.label)

        return True

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
    + (static) incr_in_dict(tuple, dict): NoneType
        Increment by one in dict
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
        False if there is no band with such id or response from site
        took more then 2 seconds, True otherwise
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
        for curr_genre in band.genres:
            _incr_in_dict((status, curr_genre), self.genre)

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

        # Collecting data on count of genres of band
        _incr_in_dict((status, len(band.genres)), self.genres_count)

        # Collecting data on country of band's origin
        _incr_in_dict((status, band.country), self.country)
        
        return True


class BandsSongsFrequencyCollection:
    """

    """
    def __init__(self):
        self.time_of_existence = {}
        self.genre = {}
        self.genres_count = {}
        self.country = {}
        self.song_duration_mean = {}
        self.label = {}

    def add(self, id_):
        band = metallum.band_for_id(str(id_))
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
        for genre in band.genres:
            _incr_in_dict((freq, genre), self.genre)
        _incr_in_dict((freq, len(band.genres)), self.genres_count)

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
        _incr_in_dict((freq, band.label))

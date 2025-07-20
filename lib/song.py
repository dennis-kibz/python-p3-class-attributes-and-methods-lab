class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        """Initialize a new song with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call class methods to update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increment the total count of songs."""
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to genres list, avoiding duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to artists list, avoiding duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Update the genre count histogram."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Update the artist count histogram."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage and testing:
if __name__ == "__main__":
    # Create some songs
    ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
    crazy_in_love = Song("Crazy in Love", "Beyonce", "Pop")
    hotline_bling = Song("Hotline Bling", "Drake", "Rap")
    single_ladies = Song("Single Ladies", "Beyonce", "Pop")
    empire_state = Song("Empire State of Mind", "Jay-Z", "Rap")
    
    # Test instance attributes
    print("Instance attributes:")
    print(f"Name: {ninety_nine_problems.name}")
    print(f"Artist: {ninety_nine_problems.artist}")
    print(f"Genre: {ninety_nine_problems.genre}")
    print()
    
    # Test class attributes and methods
    print("Class attributes:")
    print(f"Total count: {Song.count}")
    print(f"Artists: {Song.artists}")
    print(f"Genres: {Song.genres}")
    print(f"Genre count: {Song.genre_count}")
    print(f"Artist count: {Song.artist_count}")
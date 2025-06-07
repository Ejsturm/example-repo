'''Create an album class that stores relevant information. Then, sort
the files by the number of songs on each. 2025-05-30 EJS'''

import copy


class Album:
    "Contains name, artist, and songs. Can be called to display info."

    def __init__(self, album_name, number_of_songs, album_artist):
        '''Constructor, no defaults'''
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def print_info(self):
        '''Return a string of all album info.'''
        return (f"{self.album_name}, {self.album_artist}, "
                f"{self.number_of_songs}")


def get_number_of_songs(album):
    '''Extract the number of songs from a single album.'''
    album_info = album.print_info().split(", ")
    return int(album_info[2])


def get_album_name(album):
    '''Extract the album name from a single album.'''
    album_info = album.print_info().split(", ")
    return album_info[0]


# Create a list with albums, print it.
albums1 = [Album("Drones", 10, "Muse"),
           Album("Pastorale", 5, "Beethoven"),
           Album("Ori OST", 26, "Gary Coker"),
           Album("Hazbin Hotel Soundtrack", 13, "Hazbin Cast"),
           Album("River of Dreams", 12, "Billy Joel")
           ]

print("The original list of albums1:")
for a in albums1:
    print(a.print_info())

# Sort albums1 according to the number of songs.
albums1.sort(key=get_number_of_songs)

# Swap elements 0 and 1 of the list using temp variable.
temp_album = albums1[0]
albums1[0] = albums1[1]
albums1[1] = temp_album

print("\nalbum1 ordered according to number of songs with 1 and 2 swapped:")
for a in albums1:
    print(a.print_info())

# Create another list with 5 more albums
albums2 = [Album("Hat in Time OST", 60, "Pasqual"),
           Album("Gladiator Soundtrack", 14, "Hans Zimmerman"),
           Album("Skeleta", 10, "Ghost"),
           Album("Jazz", 1, "Queen"),
           Album("Phantom of the Opera", 30, "Llyod Webber")
           ]

# Add all of albums1 entries to albums2. I am creating new objects,
# not 're-using' the same memory of albums1.
for a in albums1:
    copied_album = copy.deepcopy(a)
    albums2.append(copied_album)

# Add two additional albums to albums2.
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did it Again", 16, "Britney Spears"))

# Alphabetize albums2 according to the album name and print.
albums2.sort(key=get_album_name)

print("\nalbums2 alphabetized according to album name:")
for a in albums2:
    print(a.print_info())

# What index is 'Dark Side of the Moon' located at?
for i, a in enumerate(albums2):
    album_title = get_album_name(a)
    if album_title == "Dark Side of the Moon":
        print(f"\n'Dark Side of the Moon is at index {i}.\n")

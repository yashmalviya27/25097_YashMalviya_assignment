# Exercise 2: Movie Night Playlist
def Movie_Night_Playlist():
    movir_playlist = ["Inception", "The Matrix", "Interstellar"]
    add_movie = input("Enter the move name you want to add: ")
    if add_movie in movir_playlist:
        print(f"Already added!")
        movir_playlist = sorted(movir_playlist)
        print(f"Alphabetical Playlist: {movir_playlist}")
    else:
        movir_playlist.append(add_movie)
        movir_playlist = sorted(movir_playlist)
        print(f"Added {add_movie}!\nAlphabetical Playlist: {movir_playlist}")


Movie_Night_Playlist()

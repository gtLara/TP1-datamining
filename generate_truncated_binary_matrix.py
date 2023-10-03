import numpy as np
import json
from collections import Counter
import os

n_tracks = 5000
n_files = 50

# Directory containing the JSON files
json_directory = "data/"

# Initialize a dictionary to store playlist information
playlist_info = {}

# Initialize a list to store all track URIs
all_track_uris = []

# Iterate through the JSON files in the directory
for f, filename in enumerate(os.listdir(json_directory)):
    if f > n_files:
        break
    if filename.endswith(".json"):
        file_path = os.path.join(json_directory, filename)
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)

            # Extract playlists
            playlists = json_data["playlists"]

            for playlist in playlists:
                # Extract playlist information
                playlist_identifier = playlist["name"]  # You can use a different identifier if needed
                track_uris = [track["track_uri"] for track in playlist["tracks"]]

                playlist_info[playlist_identifier] = track_uris

                # Extract track URIs and add them to the list
                all_track_uris.extend(track_uris)

# Count the frequency of each track URI
track_uri_counts = Counter(all_track_uris)

# Sort the track URIs by frequency in decreasing order
sorted_track_uris = [uri for uri, _ in track_uri_counts.most_common()] \
                    [:n_tracks]

# Initialize a 2D binary matrix with rows (playlists) and columns (songs)
binary_matrix = []

# Iterate through each playlist
for playlist_identifier in playlist_info:
    playlist_track_uris = playlist_info[playlist_identifier]
    playlist_row = []

    # Iterate through each track URI sorted by frequency
    for track_uri in sorted_track_uris:
        # Check if the track URI is in the playlist's set of track URIs
        playlist_row.append(1 if track_uri in playlist_track_uris else 0)

    # Append the binary row to the binary matrix
    binary_matrix.append(playlist_row)

binary_matrix = np.array(binary_matrix)

np.save("binary_matrix", binary_matrix)

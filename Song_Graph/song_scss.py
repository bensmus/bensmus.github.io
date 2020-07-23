# generates scss for song_specific.scss

from song_util import return_data, return_specific_scss

data = return_data(r'C:\Users\Ben Smus\Learning_Programming\bensmus.github.io\Song_Graph\song.yml')
songs = list(data.keys())

string = '''
    $Dance: rgb(89, 255, 122);
    $Electronic: rgb(89, 249, 255);
    $Rock: rgb(89, 111, 255);
    $Pop: rgb(240, 65, 164);
    $Classical: rgb(204, 166, 255);

'''

for song in songs:
    string += return_specific_scss(song, data)
print(string)

with open(r'C:\Users\Ben Smus\Learning_Programming\bensmus.github.io\Song_Graph\song_specific.scss', 'w') as f:
    f.write(string)
# generates html for songs.html

from song_util import return_data, return_short_name
from yattag import Doc  # for making the html

doc, tag, text = Doc().tagtext()  # (html) connects tag to doc, text to tag

data = return_data(r'C:\Users\Ben Smus\Learning_Programming\bensmus.github.io\Song_Graph\song.yml')
songs = list(data.keys())


with tag('html'):
    
    with tag('head'):
        with tag('title'):
            text('Song Map')
        doc.stag('link', href='song_general.css', rel='stylesheet')
        doc.stag('link', href='song_specific.css', rel='stylesheet')
    
    with tag('body'):
        with tag('h1'):
            text('Song Map')
        
        # div for each song
        for song in songs:

            # getting song specific data
            songname = data[song]['Song']
            short_songname = return_short_name(songname)
            link = data[song]['Link']
            artist = data[song]['Artist']
            genre = data[song]['Genre']
            year = data[song]['Year']

            with tag('div', id=song, klass='song-bubble'):
                # make the default view for the song
                with tag('span', klass='default'):
                    text(short_songname)
                with tag('span', klass='expanded'):
                    with tag('a', href=link, target='_blank'):
                        text(songname)
                    doc.stag('br')
                    text(artist)
                    doc.stag('br')
                    text(genre)
                    doc.stag('br')
                    text(year)

htmlstr = doc.getvalue()
print(htmlstr)

with open(r'C:\Users\Ben Smus\Learning_Programming\bensmus.github.io\Song_Graph\song.html', 'w') as f:
    f.write(htmlstr)
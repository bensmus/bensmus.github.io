import yaml  # for getting content to put in html
from yattag import Doc  # for making the html
doc, tag, text = Doc().tagtext()

# with works with any class that has __enter__ and __exit__ methods, not just files
with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\songs.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

songnames = list(data.keys())

with tag('html'):
    with tag('body'):

        # song is a key in data
        for song in songnames:
            with tag('div', id=song):
                text(song)
                with tag('a', href=data[song]['Link'], target='_blank'):
                    text('YT')

html = doc.getvalue()
print(html)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\songs.html', 'w') as f:
    f.write(html)

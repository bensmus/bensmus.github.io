import yaml  # for getting content to put in html
from yattag import Doc  # for making the html
doc, tag, text = Doc().tagtext()  # (html) connects tag to doc, text to tag

# with works with any class that has __enter__ and __exit__ methods, not just files
with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\songs.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

songs = list(data.keys())


def return_marginstr(song, data):
    '''e.g {margin-left: 100; margin-top: 100;}'''

    marginstr = f"margin-left: {data[song]['Left']};" \
        + f"margin-top: {data[song]['Top']};"
    
    return marginstr

with tag('html'):
    with tag('style'):

        # song is a key in data

        cssstr = ''
        for song in songs:

            # making the css rule
            
            # line 1
            cssstr += f'#{song}' + '{'

            # inside the block
            cssstr += return_marginstr(song, data)

            # closing brace
            cssstr += '}'

        text(cssstr)
        
    with tag('body'):

        # song is a key in data
        for song in songs:
            with tag('div', id=song):
                with tag('a', href=data[song]['Link'], target='_blank'):
                    text(data[song]['Song'])

htmlstr = doc.getvalue()
print(htmlstr)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\songs.html', 'w') as f:
    f.write(htmlstr)

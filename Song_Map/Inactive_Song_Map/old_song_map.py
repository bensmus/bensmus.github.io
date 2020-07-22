import yaml  # for getting content to put in html
from yattag import Doc  # for making the html
doc, tag, text = Doc().tagtext()  # (html) connects tag to doc, text to tag

# with works with any class that has __enter__ and __exit__ methods, not just files
with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\songs.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

songs = list(data.keys())


def return_css_content(song, data):
    '''e.g {margin-left: 100; margin-top: 100;}'''

    content = f"position: absolute; top: {data[song]['Top']}px; left: {data[song]['Left']}px;"
    return content


with tag('html'):
    with tag('style'):

        # nicer font
        text("body {font-family: 'Roboto', sans-serif;}")

        # header rules
        text("h1 {position: absolute; left: 100; top: 10; font-weight: 300; line-height: normal;}")

        # general style for all songs
        text(".dropdown {display: inline-block;}")

        # song is a key in data
        cssstr = ''
        for song in songs: 

            # making the css rule
            
            # line 1
            cssstr += f'#{song}' + '{'

            # inside the block
            cssstr += return_css_content(song, data)

            # closing brace
            cssstr += '}'

        text(cssstr)

    with tag('body'):

        with tag('h1'):
            text('Song Map')
        
        # song is a key in data
        for song in songs:
            with tag('div', id=song, klass='dropdown'):
                with tag('a', href=data[song]['Link'], target='_blank'):
                    text(data[song]['Song'])
                # adding dropdown content to the div
                with tag('div', klass='dropdown-content'):
                    text(data[song]['Artist'])
                

htmlstr = doc.getvalue()
print(htmlstr)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\songs.html', 'w') as f:
    f.write(htmlstr)

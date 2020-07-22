# generates html for songs.html
import yaml  # for getting content to put in html
from yattag import Doc  # for making the html
doc, tag, text = Doc().tagtext()  # (html) connects tag to doc, text to tag

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\songs.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

songs = list(data.keys())


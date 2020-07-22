import yaml

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\songs.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
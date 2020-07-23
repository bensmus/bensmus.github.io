import yaml  # for getting content to put in html

def return_data(file_path):
    with open(file_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

charlimit = 12  # limiting width for song 

def return_short_name(name):
    if len(name) > charlimit:
        return name[:9] + '...'
    return name

def return_specific_scss(song, data):
    '''
    #Skrillex-SMaNS {
    background-color: $Dance;
    top: 100px;
    left: 100px;
    }
    '''
    # line by line
    string = f'#{song}' + '{'
    string += f"background-color: ${data[song]['Supergenre']};"
    string += f"top: {data[song]['Top']}px;"
    string += f"left: {data[song]['Left']}px;" + '}'
    return string
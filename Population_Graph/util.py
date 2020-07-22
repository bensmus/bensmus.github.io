import csv
import numpy as np

def update_html_string(html_existing, html_fig, html_target_id):
    
    insertion_index = html_existing.find(f'<div id="{html_target_id}">') \
        + len(f'<div id="{html_target_id}">')

    html_new = html_existing[0:insertion_index] + html_fig \
        + html_existing[insertion_index:] 
    
    return html_new


def replace_keys(key_list, old_dict):
    new_dict = dict(zip(key_list, old_dict.values()))
    return new_dict


def passed_spec_check(index_string_dict, row):
    for i in index_string_dict.keys():
        if row[i] != index_string_dict[i]:
            return False
    return True


def get_desired_col(col_index_list, row):
    '''
    take ([0, 2], ['asdf', 'qwer', 'zxcv']) --> (['asdf', 'zxcv'])
    '''
    row = [row[i] for i in range(len(row)) if (i in col_index_list)]
    return row


def get_csv(csv_file, **kwargs):
    '''
    Returns a 2d list 
    kwargs are spec and col

    spec: what rows to get from the csv
    col: what columns to get from the specified rows
    '''
    
    spec = kwargs['spec']  # e.g spec = # {Location: 'China', Variant: 'Medium'}
    col = kwargs['col']  # e.g col = ['Time', 'PopTotal']

    csv_2dlist = []

    with open(csv_file) as f:
        reader = list(csv.reader(f))
        csv_header_list = reader[0]
        spec_header_list = list(spec.keys())
        spec_index_list = [csv_header_list.index(header) for header in spec_header_list]
        col_index_list = [csv_header_list.index(header) for header in col]

        # index of specification and expected string value
        index_string_dict = replace_keys(spec_index_list, spec)
        print(index_string_dict)  # {1: 'China', 3: 'Medium'}

        # index of desired columns
        print(col_index_list)  # [1, 2]
        # breakpoint()

        for row in reader:
            if passed_spec_check(index_string_dict, row):
                row_filtered = get_desired_col(col_index_list, row)  
                csv_2dlist.append(row_filtered)  # we passed all the spec checks

        return csv_2dlist
        

def plot_ready(pop):
    '''takes a 2d pop list and returns two seperate lists'''
    pop_dict = dict(pop)
    xstring = list(pop_dict.keys())
    ystring = list(pop_dict.values())
    x = np.array([float(elem) for elem in xstring])
    y = np.array([float(elem) for elem in ystring])
    return x, y


if __name__ == "__main__":
    csv_2dlist = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location':'China', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
    print('---------------------')
    print(csv_2dlist)
    print('---------------------')
    print(plot_ready(csv_2dlist))


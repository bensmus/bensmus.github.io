import csv

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


def get_csv_if(csv_file, header_string_dict):
    '''gets certain rows from a csv if the header is a certain string value,
    in the format of a 2d list.

    takes csv that matches the spec.
    
    e.g only takes rows that have a Variant of Medium and a Location of China
    '''
    
    csv_2dlist = []

    with open(csv_file) as f:
        reader = list(csv.reader(f))
        csv_header_list = reader[0]
        spec_header_list = list(header_string_dict.keys())
        spec_index_list = [csv_header_list.index(header) for header in spec_header_list]

        # index of specification and expected string value
        index_string_dict = replace_keys(spec_index_list, header_string_dict)
        print(index_string_dict)  # {1: 'China', 3: 'Medium'}

        # breakpoint()

        for row in reader:
            if passed_spec_check(index_string_dict, row):
                csv_2dlist.append(row)  # we passed all the spec checks

        return csv_2dlist
        

'''
csv_2dlist = get_csv_if(r'RawData\world_population.csv', {'Location':'China', 'Variant':'Medium'})
print(csv_2dlist)
'''
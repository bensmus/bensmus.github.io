def update_html_string(html_existing, html_fig, html_target_id):
    
    insertion_index = html_existing.find(f'<div id="{html_target_id}">') \
        + len(f'<div id="{html_target_id}">')

    html_new = html_existing[0:insertion_index] + html_fig \
        + html_existing[insertion_index:] 
    
    return html_new

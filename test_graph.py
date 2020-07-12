import os
import matplotlib.pyplot as plt
import mpld3
from util import update_html_string
import lxml.etree, lxml.html

fig = plt.figure()
plt.plot([1, 2, 3])
html_fig = mpld3.fig_to_html(fig)

# look for a div with the following id
html_target_id = os.path.basename(__file__)
print(html_target_id)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\index.html') as f:
    html_existing = f.read()

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\index.html', 'w') as f:
    html_new = update_html_string(html_existing, html_fig, html_target_id)
    f.write(html_new)




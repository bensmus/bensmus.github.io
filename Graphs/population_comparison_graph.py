import os
from util import update_html_string, get_csv_if

# graphing modules
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins  # for interactive behaviour

china_pop = get_csv_if(r'RawData\world_population.csv', {'Location':'China', 'Variant':'Medium'})
india_pop = get_csv_if(r'RawData\world_population.csv', {'Location':'India', 'Variant':'Medium'})
us_pop = get_csv_if(r'RawData\world_population.csv', {'Location': 'United States of America', 'Variant':'Medium'})
indonesia_pop = get_csv_if(r'RawData\world_population.csv', {'Location':'Indonesia', 'Variant':'Medium'})
pakistan_pop = get_csv_if(r'RawData\world_population.csv', {'Location':'Pakistan', 'Variant':'Medium'})
nigeria_pop = get_csv_if(r'RawData\world_population.csv', {'Location':'Nigeria', 'Variant':'Medium'})
pops = [china_pop, india_pop, us_pop, indonesia_pop, pakistan_pop, nigeria_pop]

fig, ax = plt.subplots()
labels = ['China', 'India', 'United States of America', 'Indonesia', 'Pakistan', 'Nigeria']

lines = []
for pop in pops:
    lines.append(ax.plot(pop))





plt.plot()
html_fig = mpld3.fig_to_html(fig)

# look for a div with the following id
html_target_id = os.path.basename(__file__)
print(html_target_id)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\index.html') as f:
    html_existing = f.read()

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\index.html', 'w') as f:
    html_new = update_html_string(html_existing, html_fig, html_target_id)
    f.write(html_new)




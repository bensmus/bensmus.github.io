import os
from util import update_html_string, get_csv, plot_ready

# graphing modules
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins  # for interactive behaviour

china_pop = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location':'China', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
india_pop = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location':'India', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
us_pop = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location': 'United States of America', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
indonesia_pop = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location':'Indonesia', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
pakistan_pop = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location':'Pakistan', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
nigeria_pop = get_csv(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\RawData\world_population.csv', spec={'Location':'Nigeria', 'Variant':'Medium'}, col=['Time', 'PopTotal'])
pops = [china_pop, india_pop, us_pop, indonesia_pop, pakistan_pop, nigeria_pop]

fig, ax = plt.subplots()
labels = ['China', 'India', 'United States of America', 'Indonesia', 'Pakistan', 'Nigeria']

for pop in pops:
    years = plot_ready(pop)[0]
    populations = plot_ready(pop)[1] * 1000  # unit conversion
    ax.plot(years, populations)

ax.legend(labels, loc='upper left')

html_fig = mpld3.fig_to_html(fig)

# look for a div with the following id
html_target_id = os.path.basename(__file__)
print(html_target_id)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\index.html') as f:
    html_existing = f.read()

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\index.html', 'w') as f:
    html_new = update_html_string(html_existing, html_fig, html_target_id)
    f.write(html_new)




import matplotlib.pyplot as plt
import mpld3

fig = plt.figure()
plt.plot([1, 2, 3])
html = mpld3.fig_to_html(fig)

with open(r'C:\Users\Ben Smus\Learning_Programming\Web\bensmus.github.io\test.html', 'a') as f:
    f.write(html)

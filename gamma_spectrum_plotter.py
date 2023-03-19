import pandas as pd
import matplotlib.pyplot as plt

source_list = ('na_22', 'co_60')
source_dfs = {}

def get_dataset(source):

    url_path = 'https://raw.githubusercontent.com/rbartilet/gamma_spesctroscopy_plot_viewer/main/%s_spectroscopy_dataset.csv'%source
    print('Obtaining data for %s...' %source)

    return pd.read_csv(url_path, names=['x', 'y'])

for source in source_list:
    source_dfs[source] = get_dataset(source)

# Plotting Na-22 photopeaks and lead shielding x-ray
source_dfs['na_22'].plot(x='x', y='y', label='Na-22')
plt.axis([-50, 1500, 0, 1000])
plt.minorticks_on()
plt.xticks([0, 500, 1000, 1500])
plt.yticks([0])

plt.vlines(x=511, ymin=0, ymax=634, color='red', alpha=0.3, label='Photopeaks')

plt.vlines(x=1275, ymin=0, ymax=60, color='red', alpha=0.3, label='_Hidden label')
plt.text(1285, 90, '1275 keV')
plt.text(521, 680, '511 keV')

plt.axvspan(73, 85, color='yellow', alpha=0.5)
plt.text(35, 400, 'Pb x-rays', fontsize = 8, )

plt.axvspan(290, 360, color='grey', alpha=0.5, label='Compton Continuum & Compton Edge')
plt.axvspan(1000, 1125, color='grey', alpha=0.5)

plt.legend(loc = 2, fontsize =8)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")

plt.show()

# Plotting Co-60 photopeaks and lead shielding x-ray
source_dfs['co_60'].plot(x='x', y='y', label='Co-60')
plt.axis([-50, 1500, 0, 1000])
plt.minorticks_on()
plt.xticks([0, 500, 1000, 1500])
plt.yticks([0])

plt.vlines(x=1176, ymin=0, ymax=615, color='red', alpha=0.3, label='Photopeaks')
plt.vlines(x=1338, ymin=0, ymax=398, color='red', alpha=0.3, label='_Hidden label')

plt.text(1188, 635, '1173 keV', fontsize =8)
plt.text(1342, 425, '1332 keV', fontsize =8)

plt.axvspan(73, 85, color='yellow', alpha=0.5)
plt.text(35, 650, 'Pb x-rays', fontsize = 8, )

plt.axvspan(500, 1000, color='grey', alpha=0.5, label='Compton Continuum & Compton Edge')
plt.axvspan(220, 260, color='bisque', alpha=0.5, label='Compton Back-scattering')

plt.legend(loc = 2, fontsize =8)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.show()
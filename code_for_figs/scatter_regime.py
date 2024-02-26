import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

l = np.linspace(.1,100,1000)
r = np.linspace(1e-3, 1e4, 1000)
l = np.logspace(-1,2,1000)
r = np.logspace(3, 4, 1000)
fig, ax = plt.subplots()
ax.add_patch(Rectangle((.1,.1), 100, 9.9, facecolor='lightgrey'))
ax.loglog(l, 2000*l/(2*np.pi), 'k--')
ax.loglog(l, .2*l/(2*np.pi), 'k--')
ax.loglog(l, .002*l/(2*np.pi), 'k--')
ax.axvline(x = .47, color = 'b', label = 'blue')
ax.axvline(x = .64, color = 'r', label = 'red')
ax.axvline(x = .865, color = 'g', label = 'veggie')
ax.text(2,.005, 'Rayleigh Scattering',rotation=14,fontsize=12)
ax.text(2,3, 'Mie Scattering',rotation=14,fontsize=12)
plt.legend()
plt.xlabel(r'wavelength ($\mu$m)')
plt.ylabel(r'particle radius ($\mu$m)')
plt.savefig('scatter_regime.png', dpi=300)
plt.show()




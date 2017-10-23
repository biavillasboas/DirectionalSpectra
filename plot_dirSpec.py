import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def plot_dirSpec(dirSpec, freq, directions=None, vmin=0,filename=None):
    """Plots the directional spectrum

        Input: 
            dirSpec = directional spectrum with shape [directions, frequencies]
            freq = frequencies
    """
    Ndir = dirSpec.shape[0]
    if directions == None:
        azimuths = np.radians(np.linspace(0, 360, Ndir))
    else:
        azimuths = directions
    ff,dd = np.meshgrid(freq, azimuths)
    
    fig, ax = plt.subplots(figsize=(10,10),subplot_kw=dict(projection='polar'))
    cmap = cm.jet
    cmap.set_under(color='white')
    cs = ax.contourf(dd,ff,dirSpec,30,vmin=vmin)
    ax.set_rmax(.28)
    ax.set_theta_offset(np.pi/2)
    ax.set_theta_direction(-1)
    thetaticks = np.arange(0,360,30)
    thetalabels = [str(s)+'$^o$' for s in np.arange(0,360,30)]
    thetalabels[0] = '360'+'$^o$'
    ax.set_thetagrids(thetaticks, thetalabels)
    periods = np.array([20,12,8,6,4])
    rticks = 1./periods
    rlabels = [str(p)+' s' for p in periods]
    ax.set_rgrids(rticks)
    ax.set_rlabel_position(130)
    cbar = plt.colorbar(cs, orientation='horizontal',fraction=0.04, format='%0.2f')
    ax.set_yticklabels(rlabels, fontsize=12)
    cbar.set_label('Energy Density [m$^2$/Hz/rad]',fontsize=14, labelpad =14)

    if filename:
        print 'saving figure on %s' %filename
        plt.savefig(filename, dpi=150)
    plt.show()

    return




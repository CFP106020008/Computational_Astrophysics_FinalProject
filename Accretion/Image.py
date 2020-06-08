import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
from astropy.visualization import make_lupton_rgb
#I = fits.getdata(input("input file name:"))
#I = fits.getdata('Dusty_xy_total.fits')
#print(np.shape(I))

n = 20
Wavelength = 1e-2*1e5**(n/50)

def ShowIm(n):
    Data = I[n,:,:]
    mean = np.mean(Data)
    std = np.std(Data)
    plt.imshow(I[n,:,:],vmin = mean-std , vmax = mean+3*std, cmap='gray')
    plt.colorbar()
    plt.title("Wavelength = {} $\mu m$".format(Wavelength))
    plt.show()
    return 

def RGB():
    Data = fits.getdata(input('input fits file:'))
    B = Data[0,:,:]
    G = Data[1,:,:]
    R = Data[2,:,:]
    image = make_lupton_rgb(R, G, B, stretch=0.01)
    mean = np.mean(image)
    std = np.std(image)
    plt.imshow(image)#,vmin = mean-std , vmax = mean+3*std)
    plt.show()


RGB()
#ShowIm(n)

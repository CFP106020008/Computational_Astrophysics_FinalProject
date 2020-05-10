import numpy as np
import matplotlib.pyplot as plt

Dust = np.loadtxt("DustDistribution.dat")
Star = np.loadtxt("TNG100-1_star_id278.txt")
Gas = np.loadtxt("TNG100-1_gas_id278.txt")

mu = 1.4 #Mean molecular mass
m_p = 1.673e-24 #g
rho_g = 0.3 #cm^-3

GrainSize = Dust[:,0]
DustToGasRatio = Dust[:,1]#/(mu*rho_g*m_p)
#print(DustToGasRatio)
#plt.plot(DustToGasRatio)
#plt.show()
SiRatio = np.ones(np.shape(GrainSize)[0])*0.54#Dust[:,2]
Mass = Gas[:,4]
n_bins = np.shape(GrainSize)[0]
Gas[:,:4] *= 1000
#print(Gas)
 
Mass = Gas[:,4]

STR1 = '<ParticleMedium filename="DustSphere_gas_'
STR2 = '_S.txt" massFraction="1" importMetallicity="false" importTemperature="false" maxTemperature="0 K" importVelocity="false" importVariableMixParams="false"><smoothingKernel type="SmoothingKernel"><CubicSplineSmoothingKernel/></smoothingKernel><materialMix type="MaterialMix"><ConfigurableDustMix scatteringType="HenyeyGreenstein"><populations type="GrainPopulation"><GrainPopulation numSizes="1" normalizationType="DustMassPerHydrogenMass" dustMassPerHydrogenAtom="0 Msun" dustMassPerHydrogenMass="0.01" factorOnSizeDistribution="1"><composition type="GrainComposition"><DraineSilicateGrainComposition/></composition><sizeDistribution type="GrainSizeDistribution"><SingleGrainSizeDistribution size="'
STR3 = ' cm"/></sizeDistribution></GrainPopulation></populations></ConfigurableDustMix></materialMix></ParticleMedium>'

#This is for silicate
for i in range(np.shape(GrainSize)[0]):
    Data = Gas*np.ones(np.shape(Gas))
    Data[:,4] = Mass*DustToGasRatio[i]*SiRatio[i]
    np.savetxt("DustSphere_gas_{}_S.txt".format(GrainSize[i]),Data)
    print(STR1+str(GrainSize[i])+STR2+str(GrainSize[i])+STR3)

#This is for carbon dust
STR4 = '_C.txt" massFraction="1" importMetallicity="false" importTemperature="false" maxTemperature="0 K" importVelocity="false" importVariableMixParams="false"><smoothingKernel type="SmoothingKernel"><CubicSplineSmoothingKernel/></smoothingKernel><materialMix type="MaterialMix"><ConfigurableDustMix scatteringType="HenyeyGreenstein"><populations type="GrainPopulation"><GrainPopulation numSizes="1" normalizationType="DustMassPerHydrogenMass" dustMassPerHydrogenAtom="0 Msun" dustMassPerHydrogenMass="0.01" factorOnSizeDistribution="1"><composition type="GrainComposition"><DraineGraphiteGrainComposition/></composition><sizeDistribution type="GrainSizeDistribution"><SingleGrainSizeDistribution size="'

#Write in the mass of dust
for i in range(np.shape(GrainSize)[0]):
    Data = Gas*np.ones(np.shape(Gas))
    Data[:,4] = Mass*DustToGasRatio[i]*(1-SiRatio[i])
    np.savetxt("DustSphere_gas_{}_C.txt".format(GrainSize[i]),Data)
    print(STR1+str(GrainSize[i])+STR4+str(GrainSize[i])+STR3)
    #This line can produce the words that we need to copy to ski file when changing the grain size configuration

print("Dust Generated")


import astropy .units as u
from galpy import potential

# Potentials
thin_disk = potential . MiyamotoNagaiPotential (amp =1.45*10.**10.* u.Msun ,\
a=4.2*u.kpc ,\
b=0.18*u.kpc)

thick_disk = potential . MiyamotoNagaiPotential (amp =2.9*10.**10.* u.Msun ,\
a=2.7*u.kpc ,\
b=0.48*u.kpc)

halo = potential . NFWPotential (amp =4.757*10**11.* u.Msun ,\
a =12.0* u.kpc)

bar = potential . SoftenedNeedleBarPotential (amp =0.6*10.0**10.* u.Msun ,\
a=4.5*u.kpc ,\
b=0.9*u.kpc ,\
c=2.*u.kpc ,\
omegab =39.0*u.km/u.s/u.kpc ,\
pa =0.41*u.rad)

nucleus = potential . PlummerPotential (amp =1.00*10.**10* u.Msun ,\
b =300.*u.pc)

# Combined potential
potential = [thin_disk , thick_disk , halo , bar , nucleus ]

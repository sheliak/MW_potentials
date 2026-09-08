import astropy .units as u
from galpy import potential

# Example of scaling parameters .
# Distance of the Sun from the Galactic centre
RO = 8.122 * u.kpc

# Circular velocity at Sun ’s distance
VO = 233.4 * u.km/u.s

# Potentials
thin_disk = potential . MiyamotoNagaiPotential (amp =0.140 ,\
a=0.517 ,\
b =0.0222)

thick_disk = potential . MiyamotoNagaiPotential (amp =0.281 ,\
a=0.3324 ,\
b =0.0591)

halo = potential . NFWPotential (amp =4.61 ,\
a =1.477)

bar = potential . SoftenedNeedleBarPotential (amp =0.058 ,\
a=0.554 ,\
b=0.111 ,\
c=0.246 ,\
omegab =0.736 ,\
pa =0.41)

nucleus = potential . PlummerPotential (amp =0.097 ,\
b =0.036)

# Combined potential
potential = [thin_disk , thick_disk , halo , bar , nucleus]

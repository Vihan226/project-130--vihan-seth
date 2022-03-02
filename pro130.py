import csv
import pandas as pd

df= pd.read_csv('c129.csv')
print(df.shape)

del df['pl_name']
del df['hostname']
del df['default_flag']
del df['sy_snum']
del df['sy_pnum']
del df['discoverymethod']
del df['disc_year']
del df['disc_facility']
del df['soltype']
del df['pl_controv_flag']
del df['pl_refanme']
del df['pl_orbper']
del df['pl_orbpererr1']
del df['pl_orbpererr2']
del df['pl_orbperlim']
del df['pl_orbsmax']
del df['pl_orbsmaxerr1']
del df['pl_orbsmaxerr2']
del df['pl_orbsmaxlim']
del df['pl_rade']
del df['pl_radeerr1']
del df['pl_radeerr2']
del df['pl_radelim']
del df['pl_radj']
del df['pl_radjerr1']
del df['pl_radjerr2']
del df['pl_radjlim']
del df['pl_bmasse']
del df['pl_bmasseerr1']
del df['pl_bmasseerr2']
del df['pl_bmasselim']
del df['pl_bmassj']
del df['pl_bmassjerr1']
del df['pl_bmassjerr2']
del df['pl_bmassjlim']
del df['pl_bmassprov']
del df['pl_orbeccen']
del df['pl_orbeccenerr1']
del df['pl_orbeccenerr2']
del df['pl_orbeccenlim']
del df['pl_insol']
del df['pl_insolerr1']
del df['pl_insolerr2']
del df['pl_insollim']
del df['pl_eqt']
del df['pl_eqterr1']
del df['pl_eqterr2']
del df['pl_eqtlim']
del df['ttv_flag']
del df['st_refname']
del df['st_spectype']
del df['st_teff']
del df['st_tefferr1']
del df['st_tefferr2']
del df['st_tefflim']
del df['st_rad']
del df['st_raderr1']
del df['st_raderr2']


print(df.shape)

print( list(df))

df= df.rename({
    'hostname':"solar_system_name",
    'discmethod':"planet_discovery_method",
    'pl_orbincl'  :"planet_orbital_inclination",
    'pl_dens':"planet_density",
    'ra_str':"righ_ascension",
    'dec_str':'declination',
    'st_teff':'host_temperature',
    'st_mass':'host_mass',
    'st_rad':'host_radius',
            },  axis='columns')

print( list(df))

df.to_csv("pro130.csv")

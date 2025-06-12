'''
basic info
'''
origin = "ecmf"
fdir_root = "/path/to/data"
rltm_year = 2024
# for realtime data

model_version_year = 2024
# hindcast for origins with on-the-fly strategy
# we need at least 1 whole year of MVD

basic_order = {"class": "s2",      "dataset": "s2s",   "expver": "prod", 
         "model": "glob",    "origin": origin,   "grid": "1.5/1.5",  
         "stream": "enfh",   "time": "00:00:00", "format": "netcdf",  
         "area": "59.5/64.5/-3.5/159.5",  #N/W/S/E     
}


'''
vars
'''
var_name_list = ["t2m", "msl", "sp", "tp", "z", "u", "v", "q", "t"]

level_required = {
    # sfc: 0
    # pl: list of plevs in hPa
    "t2m"   : 0,
    "msl"   : 0,
    "tp"    : 0,
    "z"     : [200, 500, 700, 850],
    "u"     : [200, 500, 700, 850],
    "v"     : [500, 700, 850],
    "q"     : [500, 700, 850],
    "r"     : [500, 700, 850],
    "t"     : [500, 700, 850],
    "sp"    : 0,
    "ts"    : 0,
}

var_name_list = ["t2m", "msl", "sp", "tp", "z", "u", "v", "q", "t"]

grib_code = {
    "t2m"   : "167",
    "msl"   : "151",
    "tp"    : "228228",
    "z"     : "156",
    "u"     : "131",
    "v"     : "132",
    "q"     : "133",
    "sp"    : "134",
    "ts"    : "235",
    "t"     : "130",
}

var_type = {
    # instantaneous / daily averaged / accumulated
    "t2m"   : "ave",
    "msl"   : "inst",
    "tp"    : "accum",
    "z"     : "inst",
    "u"     : "inst",
    "v"     : "inst",
    "q"     : "inst",
    "sp"    : "inst",
    "ts"    : "ave",
    "t"     : "inst",
}

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

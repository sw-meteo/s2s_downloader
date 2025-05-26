import os
from origin_info import pf_member_hind
from var_info import grib_code, level_required, var_name_list
from order_handler import get_all_valid_mvd, get_all_valid_hdate, get_lead_str
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()


'''
basic info
'''
origin = "ecmf"
fdir_root = "/path/to/data"

order = {"class": "s2",      "dataset": "s2s",   "expver": "prod", 
         "model": "glob",    "origin": origin,   "grid": "1.5/1.5",  
         "stream": "enfh",   "time": "00:00:00", "format": "netcdf",       
         "area": "59.5/64.5/-3.5/159.5",  #N/W/S/E
}


'''
retrieve data
'''
if __name__ == "__main__":
    print(f"Downloading data from {origin}")
    for ensemble_type in ["cf", "pf"]:
        print(f"retrieving {ensemble_type}")
        order["type"] = ensemble_type
        if ensemble_type == "pf":
            order["number"] = f"1/to/{pf_member_hind[origin]}"
        
        mvd_list = list(get_all_valid_mvd(origin))
        for mvd in mvd_list:
            order["date"] = mvd.strftime("%Y-%m-%d")
            
            time_start_hdate = time()
            hdate_list = list(get_all_valid_hdate(origin, mvd))
            for hdate in hdate_list:
                order["hdate"] = hdate.strftime("%Y-%m-%d")
                
                for var_name in var_name_list:
                    fname = f"{origin}.mvd{mvd.strftime('%Y%m%d')}.sd{hdate.strftime('%Y%m%d')}.{var_name}.{ensemble_type}.nc"
                    print(f"retrieving {fname} ...")
                    fdir = os.path.join(fdir_root, origin, var_name)
                    os.makedirs(fdir, exist_ok=True)
                    if(os.path.isfile(os.path.join(fdir, fname))):
                        print(" -- already downloaded! skip this request. -- ")
                        continue
                    order["target"] = os.path.join(fdir, fname)
                    
                    order["param"] = grib_code[var_name]
                    order["step"] = get_lead_str(origin, var_name)
                    
                    if (level_required[var_name] == 0):
                        order["levtype"] = "sfc"  
                    else:
                        order["levtype"] = "pl"
                        order["levelist"] = '/'.join([str(lv) for lv in (level_required[var_name])])
                    
                    server.retrieve(order)

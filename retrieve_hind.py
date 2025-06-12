import os
from origin_info import pf_member_rltm
from var_info import grib_code
from basic_info import origin, fdir_root, basic_order, level_required, var_name_list
from order_handler import get_all_valid_mvd, get_all_valid_hdate, get_lead_str, get_var_list
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()


if __name__ == "__main__":
    order = basic_order
    
    print(f"Downloading data from {origin}")
    for ensemble_type in ["cf", "pf"]:
        print(f"retrieving {ensemble_type}")
        order["type"] = ensemble_type
        if ensemble_type == "pf":
            order["number"] = f"1/to/{pf_member_rltm[origin]}"
        
        mvd_list = list(get_all_valid_mvd(origin))
        for mvd in mvd_list:
            order["date"] = mvd.strftime("%Y-%m-%d")
            
            hdate_list = list(get_all_valid_hdate(origin, mvd))
            for hdate in hdate_list:
                order["hdate"] = hdate.strftime("%Y-%m-%d")
                
                var_name_list = get_var_list(origin)
                for var_name in var_name_list:
                    fname = f"{origin}.global.1P5.mvd{mvd.strftime('%Y%m%d')}.sd{hdate.strftime('%Y%m%d')}.{var_name}.{ensemble_type}.nc"
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

from basic_info import model_version_year

'''
1. handling the number of members
'''
pf_member_hind = {
    "ecmf": 10,
    "anso": 3,
    "egrr": 6,
    "lfpw": 9,
    "cwao": 3,
    "kwbc": 3,
    "babj": 3,
}

pf_member_rltm = {
    "ecmf": 100,
    "anso": 15,  # after 2024/8/21 it‘s 48
    "egrr": 3,
    "lfpw": 24,
    "cwao": 20,
    "kwbc": 15,
    "babj": 3,
    
}

'''
2. hindling model version date and start date of al available hindcasts
'''
model_version_strategy = {
    "ecmf": "on-the-fly",
    "babj": "on-the-fly",
    "rims": "on-the-fly",
    "egrr": "on-the-fly",
    "cwao": "on-the-fly",
    "rksl": "on-the-fly",
    "lfpw": "fixed",
    "anso": "fixed",
    "kwbc": "fixed",
    "isac": "fixed",
    "rjtd": "fixed",
}

fix_mvd = { 
    # for origins with fixed strategy
    "anso": "2019-01-01",
    "lfpw": "2019-07-01",
    "kwbc": "2011-03-01",
    "rjtd": "2022-09-30",
    "isac": "2017-06-08", 
}

fix_hind_range = {
    # for origins with fixed strategy
    # range of hindcast year must be fixed
    # the last year is included (different from python range)
    "anso": [1999, 2018],
    "lfpw": [1993, 2017],
    "kwbc": [1999, 2010],
    "isac": [1981, 2010],
    "rjtd": [1991, 2020],
}

fix_hdate_strategy = { 
    # for origins with fixed strategy
    # save the strategy of all volid hindcast date
    # use tuple rather than dict bcz dict cannot be passed to **kwargs
    # value is list of tuple, each tuple is a pair of (key, value)
    "anso": [("valid_weekdays", range(0,7)), 
             ("skip_leap_day", True)],
    "kwbc": [("valid_weekdays", range(0,7)),
             ("skip_leap_day", True)],
    "lfpw": [("valid_weekdays", [3])],
}

# Unified hindcast year configuration
# value is list of tuple, each tuple is a pair of (key, value)
# supports both "hind_year_range" and "hind_year_list" formats
hind_year_config = {
    # for origins with on-the-fly strategy
    #"ecmf": [("hind_year_range", [model_version_year - 20, model_version_year - 1]),
    #         ("leap_day_fallback", True)],
    "ecmf": [("hind_year_list", [2020]), ("leap_day_fallback", True)],
    #"babj": [("hind_year_range", [model_version_year - 15, model_version_year - 1])],
    "babj": [("hind_year_list", [2020]), ("leap_day_fallback", True)],
    #"cwao": [("hind_year_range", [2001, 2020])],
    "cwao": [("hind_year_list", [2020]), ("leap_day_fallback", True)],
    "rims": [("hind_year_range", [1991, 2015])],
    "egrr": [("hind_year_range", [1993, 2016])],
    "rksl": [("hind_year_range", [1993, 2016])],
    # for origins with fixed strategy
    "anso": [("hind_year_range", [1999, 2018])],
    "lfpw": [("hind_year_range", [1993, 2017])],
    "kwbc": [("hind_year_range", [1999, 2010])],
    "isac": [("hind_year_range", [1981, 2010])],
    "rjtd": [("hind_year_range", [1991, 2020])],
}

otf_mvd_strategy = {
    # for origins with on-the-fly strategy
    # value is list of tuple, each tuple is a pair of (key, value)
    "ecmf": [("valid_weekdays", [0, 3])],
    "babj": [("valid_weekdays", [0, 3])],
    "cwao": [("valid_weekdays", [3])],
    "rims": [("valid_weekdays", [3])],
    "egrr": [("valid_monthdays", [1, 9, 17, 25])],
    "rksl": [("valid_monthdays", [1, 9, 17, 25])],
}

rltm_strategy = {
    "ecmf":  [("valid_weekdays", range(0,7))],  # daily
    "babj":  [("valid_weekdays", [0, 3])],
    "egrr":  [("valid_weekdays", range(0,7))],  # daily
    "anso":  [("valid_weekdays", range(0,7))],  # daily
    "lfpw":  [("valid_weekdays", [3])],
    "cwao":  [("valid_weekdays", [3])],  # after 24/6/13 it's  [0, 3]
    "kwbc":  [("valid_weekdays", range(0,7))],  # daily
}
'''
3. handling other conditions
'''
max_step = {
    "ecmf": 1104,
    "babj": 1440,
    "rims": 1464,
    "anso": 1560,
    "isac": 768,
    "rjtd": 816,
    "lfpw": 1128,
    "cwao": 1056,
    "egrr": 1440,
    "rksl": 1440,
    "cwao": 768,  # after 24/6/13 it's 936
    "kwbc": 1056,
}

unavailable_var_list = {
    # "full":  ["t2m", "ts", "msl", "sp", "tp", "z", "u", "v", "q"],
    # require updating if var_name_list_full is updated!
    "ecmf":  [],
    "babj":  [],
    "rims":  [],
    "anso":  ["msl"],
    "isac":  ["ts", "sp"],
    "rjtd":  [],
    "lfpw":  [],
    "kwbc":  [],
    "egrr":  ["msl"],
    "cwao":  ["ts"],
    "rksl":  ["msl"],
}

skip_initial = {
    # skip initial time step
    "ecmf":  False,
    "babj":  False,
    "anso":  True,  # unavailable for all inst vars
    "egrr":  True,  # unavailble for inst sfc
    "lfpw":  True,  # unavailable for all inst vars
    "cwao":  True,  # unavailable for all inst vars
    "kwbc":  True,  # unavailble for inst sfc
}

# Mixed strategy configuration - for special year strategy transitions
# this will override the otf_mvd_strategy
mixed_strategy_config = {
    "ecmf": {
        2024: {
            "transition_date": "2024-11-11",
            "strategy1_params": [("valid_weekdays", [0, 3])],  # CY48R1, Mon&Thu
            "strategy2_params": [("valid_monthdays", [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]), # CY49R1, odd days
                                 ("skip_leap_day", True)],  
        }
    },
    "cwao": {
        2024: {
            "transition_date": "2024-06-13",
            "strategy1_params": [("valid_weekdays", [3])],  # GEPS 7, Thu
            "strategy2_params": [("valid_weekdays", [0, 3])],  # GEPS 8, Mon&Thu
        }
    }
}

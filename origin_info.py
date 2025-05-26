
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

pf_member_fcst = {
    "ecmf": 50,
    "anso": 15,
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

model_version_year = 2022
# for origins with on-the-fly strategy
# we need at least 1 whole year of MVD

otf_hind_range = {
    # for origins with on-the-fly strategy
    # handling sliding window range
    # the last year is included (different from python range)
    "ecmf": [model_version_year - 20, model_version_year - 1],
    "babj": [model_version_year - 15, model_version_year - 1],
    "rims": [1991, 2015],
    "egrr": [1993, 2016],
    "cwao": [2001, 2020],
    "rksl": [1993, 2016],
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
    "cwao": 768,
    "kwbc": 1056,
}

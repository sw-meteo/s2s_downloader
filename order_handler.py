from datetime import datetime
from origin_info import (model_version_strategy, otf_mvd_strategy, model_version_year,
                         fix_mvd, otf_hind_range, fix_hind_range, fix_hdate_strategy, max_step)
from var_info import var_type
from date_handler import _get_valid_date, _get_all_valid_hdate

def get_all_valid_mvd(origin):
    """
    Get all valid model version dates (MVD) for specified origin.
    
    Args:
        origin (str): Origin code
        
    Returns:
        list: List of valid model version dates
    """
    if model_version_strategy[origin] == "on-the-fly":
        aux_kwargs = dict(otf_mvd_strategy[origin])
        return _get_valid_date(model_version_year, **aux_kwargs)
    elif model_version_strategy[origin] == "fixed":
        return [datetime.strptime(fix_mvd[origin], "%Y-%m-%d")]

def get_all_valid_hdate(origin, mvd, **aux_kwargs):
    """
    Get all valid hindcast dates for specified origin and model version date.
    
    Args:
        origin (str): Origin code
        mvd (datetime): Model version date
        **aux_kwargs: Additional parameters
        
    Returns:
        list: List of valid hindcast dates
    """
    if model_version_strategy[origin] == "on-the-fly":
        return _get_all_valid_hdate("on-the-fly", otf_hind_range[origin], model_version_date=mvd, **aux_kwargs)
    elif model_version_strategy[origin] == "fixed":
        aux_kwargs_add = dict(fix_hdate_strategy[origin])
        aux_kwargs = {**aux_kwargs, **aux_kwargs_add}
        return _get_all_valid_hdate("fixed", fix_hind_range[origin], **aux_kwargs)

def get_lead_str(origin, var_name):
    """
    Generate forecast lead time string based on variable type.
    
    Args:
        origin (str): Origin code
        var_name (str): Variable name
        
    Returns:
        str: Lead time string separated by '/'
    """
    _max_step = max_step[origin]
    if var_type[var_name] == "ave":
        return '/'.join(["%s-%s"%(hr1, hr2) for hr1, hr2 in zip(range(0, _max_step, 24), range(24, (_max_step+24), 24))])
    elif (var_type[var_name] == "inst"):
        return '/'.join([str(hr) for hr in range(24, (_max_step+24), 24)])
    elif (var_type[var_name] == "accum"):
        return '/'.join([str(hr) for hr in range(6, (_max_step+6), 6)])

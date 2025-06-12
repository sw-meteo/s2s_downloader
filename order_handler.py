from datetime import datetime
from origin_info import model_version_strategy, otf_mvd_strategy, rltm_strategy, model_version_year, \
                        fix_mvd, fix_hind_range, fix_hdate_strategy, \
                        max_step, unavailable_var_list, skip_initial, mixed_strategy_config, \
                        hind_year_config
from var_info import var_type, var_name_list
from date_handler import _get_valid_date, _get_all_valid_hdate, _get_valid_date_with_mixed_strategy



def get_all_valid_rltm_date(origin, rltm_year):
    """
    Get all valid real-time model version dates (MVD) for specified origin.
    
    Args:
        origin (str): Origin code
        rltm_year (int): Real-time year
        
    Returns:
        list: List of valid real-time model version dates
    """
    aux_kwargs = dict(rltm_strategy[origin])
    mixed_config = mixed_strategy_config.get(origin, {})
    return _get_valid_date_with_mixed_strategy(rltm_year, mixed_config=mixed_config, **aux_kwargs)


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
        mixed_config = mixed_strategy_config.get(origin, {})
        return _get_valid_date_with_mixed_strategy(model_version_year, mixed_config=mixed_config, **aux_kwargs)
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
        hind_config = dict(hind_year_config[origin])
        return _get_all_valid_hdate("on-the-fly", model_version_date=mvd, **hind_config, **aux_kwargs)
    elif model_version_strategy[origin] == "fixed":
        aux_kwargs_add = dict(fix_hdate_strategy[origin])
        hind_config = dict(hind_year_config[origin])
        aux_kwargs = {**aux_kwargs, **aux_kwargs_add, **hind_config}
        return _get_all_valid_hdate("fixed", **aux_kwargs)


def get_lead_str(origin, var_name):
    """
    Generate forecast lead time string based on variable type.
    
    Args:
        origin (str): Origin code
        var_name (str): Variable name
        
    Returns:
        str: Lead time string separated by '/'
    """
    skip0 = skip_initial[origin] 
    _max_step = max_step[origin]
    if var_type[var_name] == "ave":
        return '/'.join(["%s-%s"%(hr1, hr2) for hr1, hr2 in zip(range(0, _max_step, 24), range(24, (_max_step+24), 24))])
    elif (var_type[var_name] == "inst"):
        if skip0:
            return '/'.join([str(hr) for hr in range(24, (_max_step+24), 24)])
        else:
            return '/'.join([str(hr) for hr in range(0, (_max_step+24), 24)])
    elif (var_type[var_name] == "accum"):
        return '/'.join([str(hr) for hr in range(6, (_max_step+6), 6)])


def get_var_list(origin):
    return [var for var in var_name_list if var not in unavailable_var_list[origin]]

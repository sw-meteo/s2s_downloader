from datetime import datetime, timedelta
from typing import List


def _get_valid_date(years: List[int] or int,
                  valid_weekdays : List[int] = None,
                  valid_monthdays : List[int] = None,
                  skip_leap_day: bool = False,
                  valid_DOYs: List[datetime] = None,
                  **aux_kwargs
                  ) -> list:
    """
    Select all valid dates according to certain strategy for one year or year list.
    
    Args:
        years (list or int): Year or list of years
        valid_weekdays (list, optional): List of valid weekdays (0-6, 0 is Monday)
        valid_monthdays (list, optional): List of valid days of month (1-31)
        skip_leap_day (bool, optional): Whether to skip Feb 29 in leap years. Defaults to False.
        
    Yields:
        datetime: Valid dates matching the criteria
    """
    if isinstance(years, int):
        years = [years]
    # valid_weekdays, valid_monthdays, valid_days can only be one of them
    assert (valid_weekdays is not None) ^ (valid_monthdays is not None) ^ (valid_DOYs is not None)

    for year in years:
        d = datetime(year, 1, 1)
        if (valid_weekdays is not None):
            while d.year == year:
                if d.weekday() in valid_weekdays:
                    if skip_leap_day and (d.month == 2) and (d.day == 29):
                        pass
                    else:
                        yield d
                d += timedelta(days=1)
        elif (valid_monthdays is not None):
            while d.year == year:
                if d.day in valid_monthdays:
                    if skip_leap_day and (d.month == 2) and (d.day == 29):
                        pass
                    else:
                        yield d
                d += timedelta(days=1)
        elif (valid_DOYs is not None):
            while d.year == year:
                if d.day in valid_DOYs:
                    if skip_leap_day and (d.month == 2) and (d.day == 29):
                        pass
                    else:
                        yield d
                d += timedelta(days=1)
        else:
            raise NotImplementedError


def _get_all_valid_hdate(strategy: str,
                  hind_year_range: List[int] = None,
                  hind_year_list: List[int] = None,
                  **aux_kwargs) -> list:
    """
    Get all valid hindcast dates based on strategy.
    
    Args:
        strategy (str): Strategy type ('fixed' or 'on-the-fly')
        hind_year_range (list, optional): Hindcast year range [start, end] (inclusive)
        hind_year_list (list, optional): Explicit list of hindcast years
        **aux_kwargs: Additional parameters, may include:
            - model_version_date (datetime): Model version date (required for on-the-fly strategy)
            - valid_weekdays (list): List of valid weekdays
            - valid_monthdays (list): List of valid days of month
            - skip_leap_day (bool): Whether this origin need to skip Feb 29
            - leap_day_fallback(bool): Whether to fallback to the previous day if Feb 29 is skipped
            
    Returns:
        generator or list: All valid hindcast dates
    """
    # only one of hind_year_range or hind_year_list can be provided
    assert (hind_year_range is not None) ^ (hind_year_list is not None)
    
    if hind_year_range is not None:
        years = list(range(hind_year_range[0], hind_year_range[1] + 1))
    else:
        years = hind_year_list
    
    if strategy == "on-the-fly":
        mvd = aux_kwargs["model_version_date"]
        if aux_kwargs.get("leap_day_fallback") and (mvd.month == 2) and (mvd.day == 29):
            # Fallback hind DOY to 2.18 if mvd is 2.29
            mvd = mvd - timedelta(days=1)
        return [datetime(hyear, mvd.month, mvd.day) for hyear in years]
        
    elif strategy == "fixed":
        return _get_valid_date(years, **aux_kwargs)


def _get_mixed_strategy_dates(year: int, 
                            transition_date: datetime,
                            strategy1_params: dict,
                            strategy2_params: dict) -> list:
    """
    Get valid dates for a year with mixed strategies before and after a transition date.
    
    Args:
        year (int): Target year
        transition_date (datetime): Date when strategy changes
        strategy1_params (dict): Parameters for first strategy (before transition_date)
        strategy2_params (dict): Parameters for second strategy (after transition_date)
        
    Returns:
        list: All valid dates for the year combining both strategies
    """
    all_dates = []
    
    dates1 = list(_get_valid_date([year], **strategy1_params))
    valid_dates1 = [d for d in dates1 if d < transition_date]
    all_dates.extend(valid_dates1)
    
    dates2 = list(_get_valid_date([year], **strategy2_params))
    valid_dates2 = [d for d in dates2 if d >= transition_date]
    all_dates.extend(valid_dates2)
    
    all_dates.sort()
    return all_dates


def _get_valid_date_with_mixed_strategy(years: List[int] or int,
                                       mixed_config: dict = None,
                                       **default_kwargs) -> list:
    """
    use `_get_mixed_strategy_dates` to mix or NOT
    
    Args:
        years: Year or list of years
        mixed_config: Mixed strategy configuration
        **default_kwargs: Default strategy parameters
        
    Returns:
        list: List of valid dates
    """
    try:
        len(years)
    except:
        years = [years]
    
    all_dates = []
    for year in years:
        if mixed_config and year in mixed_config:
            # Use mixed strategy
            from datetime import datetime as dt
            config = mixed_config[year]
            transition_date = dt.strptime(config["transition_date"], "%Y-%m-%d")
            strategy1_params = dict(config["strategy1_params"])
            strategy2_params = dict(config["strategy2_params"])
            
            year_dates = _get_mixed_strategy_dates(year, transition_date, 
                                                 strategy1_params, strategy2_params)
            all_dates.extend(year_dates)
        else:
            # Use default strategy
            year_dates = list(_get_valid_date([year], **default_kwargs))
            all_dates.extend(year_dates)
    
    return sorted(all_dates)

from datetime import datetime, timedelta

def _get_valid_date(years: list or int,
                  valid_weekdays : list = None,
                  valid_monthdays : list = None ,
                  skip_leap_day: bool = False) -> list:
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
    try:
        len(years)
    except:
        years = [years]
    for year in years:
        d = datetime(year, 1, 1)
        if (valid_weekdays is not None) and (valid_monthdays is None):
            while d.year == year:
                if d.weekday() in valid_weekdays:
                    if skip_leap_day and (d.month == 2) and (d.day == 29):
                        pass
                    else:
                        yield d
                d += timedelta(days=1)
        elif (valid_monthdays is not None) and (valid_weekdays is None):
            while d.year == year:
                if d.day in valid_monthdays:
                    if skip_leap_day and (d.month == 2) and (d.day == 29):
                        pass
                    else:
                        yield d
                d += timedelta(days=1)
            
def _get_all_valid_hdate(strategy: str,
                  hind_year_range: list,
                  **aux_kwargs) -> list:
    """
    Get all valid hindcast dates based on strategy.
    
    Args:
        strategy (str): Strategy type ('fixed' or 'on-the-fly')
        hind_year_range (list): Hindcast year range [start_year, end_year]
        **aux_kwargs: Additional parameters, may include:
            - model_version_date (datetime): Model version date (required for on-the-fly strategy)
            - valid_weekdays (list): List of valid weekdays
            - valid_monthdays (list): List of valid days of month
            - skip_leap_day (bool): Whether this origin need to skip Feb 29
            
    Returns:
        generator or list: All valid hindcast dates
    """
    if strategy == "on-the-fly":
        mvd = aux_kwargs["model_version_date"]
        return [datetime(hyear, mvd.month, mvd.day) \
            for hyear in range(hind_year_range[0], hind_year_range[1] + 1)]
        
    elif strategy == "fixed":
        return _get_valid_date(range(hind_year_range[0], hind_year_range[1] + 1), **aux_kwargs)

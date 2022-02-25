from datetime import datetime, timedelta, date


def generate_date_iso_from_string(date_string, delta=0,format="yyyymmdd"):
    if format == "yyyymmdd":
        year = date_string[0:4]
        month = date_string[4:6]
        day = date_string[6:8]
        d = datetime(int(year), int(month), int(day))
        d = d + timedelta(days=delta)
        return d.isoformat() + "Z"
    else:
        d = datetime.now()
        d = d + timedelta(days=delta)
        return d.isoformat() + "Z"
    return d


def get_current_date_iso():
    t = date.today()
    d = datetime(t.year, t.month, t.day)
    d = d + timedelta(days=1)
    return d.isoformat() + "Z"


def generate_date_from_string(date_string, format="yyyymmdd"):
    if format == "yyyymmdd":
        year = date_string[0:4]
        month = date_string[4:6]
        day = date_string[6:8]
        d = date(int(year), int(month), int(day))
    else:
        d = datetime.now().date()
    return d


def get_date_difference(start_date,end_date):
    end  = generate_date_from_string(end_date)
    start = generate_date_from_string(start_date)
    delta = end - start
    return delta.days
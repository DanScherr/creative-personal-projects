from datetime import datetime

def easy_datetime(type: str):
    full_date = str(datetime.today())

    if type == 'full':
        return full_date
    elif type == 'year':
        return int(full_date[:4])
    elif type == 'month':
        return int(full_date[5:7])
    elif type == 'day':
        return int(full_date[8:10])
    elif type == 'hour':
        return int(full_date[11:13])
    elif type == 'minute':
        return int(full_date[14:16])
    elif type == 'second':
        return int(full_date[17:19])
    else:
        return None
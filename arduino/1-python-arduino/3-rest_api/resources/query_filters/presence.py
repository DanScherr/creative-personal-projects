from lib.easy_date import easy_datetime

def normalize_path_params(  sensor_id = None, 
                            year_min = 0,
                            month_min = 0,
                            day_min = 0,
                            hour_min = 0,
                            minute_min = 0,
                            second_min = 0,
                            month_max = 12,
                            day_max = 31,
                            hour_max = 24,
                            minute_max = 60,
                            second_max = 60,
                            **dados ):
    if sensor_id:
        return {
            'sensor_id': sensor_id,
            'year_min': year_min,
            'year_max': easy_datetime('year'),
            'month_min': month_min,
            'month_max': month_max,
            'day_min': day_min,
            'day_max': day_max,
            'hour_min': hour_min,
            'hour_max': hour_max,
            'minute_min': minute_min,
            'minute_max': minute_max,
            'second_min': second_min,
            'second_max': second_max,
            **dados
        }
    else:
        return {
                'year_min': year_min,
                'year_max': easy_datetime('year'),
                'month_min': month_min,
                'month_max': month_max,
                'day_min': day_min,
                'day_max': day_max,
                'hour_min': hour_min,
                'hour_max': hour_max,
                'minute_min': minute_min,
                'minute_max': minute_max,
                'second_min': second_min,
                'second_max': second_max,
                **dados
            }


consulta_com_sensorid = "SELECT \
                            sensor_id, \
                            detection, \
                            date_time_sent, \
                            CAST(SUBSTR(date_time_sent, 0, 5) as INTEGER) as year, \
                            CAST(SUBSTR(date_time_sent, 6, 2) as INTEGER) AS month, \
                            CAST(SUBSTR(date_time_sent, 9, 2) as INTEGER) AS day, \
                            CAST(SUBSTR(date_time_sent, 12, 2) as INTEGER) AS hour, \
                            CAST(SUBSTR(date_time_sent, 15, 2) as INTEGER) AS minute, \
                            CAST(SUBSTR(date_time_sent, 18, 2) as INTEGER) AS second \
                        FROM  \
                            presence \
                        WHERE  \
                            sensor_id = ? AND \
                            ( year >= ? AND year <= ? ) AND \
                            ( month >= ? AND month <= ?) AND \
                            ( day >= ? AND day <= ?) AND \
                            ( hour >= ? AND hour <= ?) AND \
                            ( minute >= ? AND minute <= ?) AND \
                            ( second >= ? AND second <= ? )"

consulta_sem_sensorid = "SELECT\
                            sensor_id,\
                            detection,\
                            date_time_sent,\
                            CAST(SUBSTR(date_time_sent, 0, 5) as INTEGER) as year,\
                            CAST(SUBSTR(date_time_sent, 6, 2) as INTEGER) AS month,\
                            CAST(SUBSTR(date_time_sent, 9, 2) as INTEGER) AS day,\
                            CAST(SUBSTR(date_time_sent, 12, 2) as INTEGER) AS hour,\
                            CAST(SUBSTR(date_time_sent, 15, 2) as INTEGER) AS minute,\
                            CAST(SUBSTR(date_time_sent, 18, 2) as INTEGER) AS second\
                        FROM\
                            presence\
                        WHERE\
                            ( year >= ? AND year <= ? ) AND\
                            ( month >= ? AND month <= ?) AND\
                            ( day >= ? AND day <= ?) AND\
                            ( hour >= ? AND hour <= ?) AND\
                            ( minute >= ? AND minute <= ?) AND\
                            ( second >= ? AND second <= ? )"
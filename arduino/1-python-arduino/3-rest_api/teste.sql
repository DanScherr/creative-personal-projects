SELECT 
    sensor_id,
    detection,
    date_time_sent,
    CAST(SUBSTR(date_time_sent, 0, 5) as INTEGER) as year,
    CAST(SUBSTR(date_time_sent, 6, 2) as INTEGER) AS month,
    CAST(SUBSTR(date_time_sent, 9, 2) as INTEGER) AS day,
    CAST(SUBSTR(date_time_sent, 12, 2) as INTEGER) AS hour,
    CAST(SUBSTR(date_time_sent, 15, 2) as INTEGER) AS minute,
    CAST(SUBSTR(date_time_sent, 18, 2) as INTEGER) AS second

FROM 
    presence
WHERE 
    ( year >= -1 AND year <= 2023 ) AND 
    ( month >= -1 AND month <= 12) AND 
    ( day >= -1 AND day <= 31) AND 
    ( hour >= -1 AND hour <= 24) AND 
    ( minute >= -1 AND minute <= 60) AND 
    ( second >= -1 AND second <= 60 )
;
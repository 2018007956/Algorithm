with rank_events as (
    SELECT event_type, value, time, rank() OVER (partition by event_type order by time desc) rank
    FROM events
)
SELECT A.event_type, A.value-B.value
    FROM (SELECT * FROM rank_events where rank=1) A
    JOIN (SELECT * FROM rank_events where rank=2) B 
        on A.event_type=B.event_type
    ORDER BY A.event_type
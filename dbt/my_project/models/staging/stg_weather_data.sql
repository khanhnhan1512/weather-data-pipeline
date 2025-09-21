{{
    config(
        materialized='table',
        unique_key='id'
    )
}}

with source as(
    select * from {{source('dev', 'raw_weather_data')}}
),

de_duplicate as (
    select
        *,
        row_number() over(partition by time order by inserted_at) as rn
    from source
)
------------------------------------------------------------------------------
select 
    id,
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    time as weather_time_local,
    (inserted_at + (utc_offset || 'hours')::interval) as inserted_at_local
from de_duplicate
where rn = 1
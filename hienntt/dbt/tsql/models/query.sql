{{ config(
    materialized='view'
) }}
select *
from {{source('sales', 'stores')}}
where store_id = 1
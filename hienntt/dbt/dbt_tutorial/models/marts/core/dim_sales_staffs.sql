with staffs as (
    select * from {{ ref('staffs') }}
), stores as (
    select * from {{ ref('stg_sales_stores') }}
)
select staffs.staff_id
    , staffs.store_id
    , stores.store_name
from staffs
left join stores on staffs.store_id = stores.store_id
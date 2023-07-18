with orders as (
    select * from {{ref('stg_sales_orders')}}
)
select order_id
from orders
where order_date < '2016-01-01'

WITH orders AS (
    SELECT * FROM {{ ref('stg_sales_orders') }}
), stores AS (
    SELECT * FROM {{ ref('stg_sales_stores') }}
)
SELECT order_id
      , customer_id
      , order_status
      , order_date
      , o.store_id
      , staff_id
      , store_name
from orders o
join stores s on o.store_id = s.store_id
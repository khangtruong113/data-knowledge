SELECT order_id
      , customer_id
      , order_status
      , order_date
      , shipped_date
      , store_id
      , staff_id
      , {{ dbt_utils.generate_surrogate_key(['customer_id', 'order_date'])}} as test_order_id
from {{ source('sales', 'orders') }}
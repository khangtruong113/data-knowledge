SELECT order_id
      , item_id
      , product_id
      , quantity
      , list_price
      , discount
      , {{ dollars_to_cents('list_price') }} as list_price_cents
from {{ source('sales', 'order_items') }}
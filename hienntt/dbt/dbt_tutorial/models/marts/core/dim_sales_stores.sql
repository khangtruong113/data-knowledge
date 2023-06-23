select store_id,
       store_name,
       phone,
       email,
       zip_code
from {{ref ('stg_sales_stores') }}
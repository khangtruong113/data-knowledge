--{{ config(materialized='view')}}
select store_id,
       store_name,
       phone,
       email,
       street,
       zip_code
from {{ source('sales', 'stores') }}
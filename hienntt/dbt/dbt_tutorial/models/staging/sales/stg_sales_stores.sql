select store_id
       , store_name
       , phone
       , email
       , zip_code
from {{ source('sales', 'stores') }}
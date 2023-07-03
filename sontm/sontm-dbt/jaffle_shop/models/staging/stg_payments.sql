with payments as (
    select
    id as payment_id,
    order_id as order_id,
    payment_method as payment_method,

    -- amount is stored in cents, convert it to dollars
    {{ cents_to_dollars('amount') }} as amount,

from {{ source ('stripe', 'raw_payments')}}
)

select * from payments
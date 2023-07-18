with orders as (
select * from {{ ref('stg_sales_orders') }}
),

daily as (

    select
        order_date,
        count(*) as num_orders,

    {% for order_status in [1, 2, 3, 4] %}

        sum(case when order_status = {{ order_status }} then 1 else 0 end) as s{{ order_status }}_total {{ ',' if not loop.last }}

    {% endfor %}

    from orders
    group by order_date
)

select * from daily
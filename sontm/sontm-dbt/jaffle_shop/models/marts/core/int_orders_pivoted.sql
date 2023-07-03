with payments as (
    select * from {{ ref('stg_payments') }}
),

pivoted as (
    select
        order_id,
        
        {%- set payment_method = ['bank_transfer', 'counpon', 'credit_card', 'gift_card'] -%}

        {%- for method in payment_method -%}

        SUM(case when payment_method = '{{ method }}' then amount else 0 end) as {{method}}_amount

        {%- if not loop.last -%}

            ,

        {%- endif %}

        {% endfor -%}

    from payments
    group by 1
)

select * from pivoted
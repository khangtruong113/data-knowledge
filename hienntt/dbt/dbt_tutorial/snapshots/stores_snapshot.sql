{% snapshot stores_snapshot %}

{{
    config(
      target_schema='snapshots',
      target_database='dbt_labs',
      unique_key='store_name',

      strategy='timestamp',
      updated_at='update_at',
    )
}}

select store_name, phone, email, street, city, state, zip_code, update_at from {{ source('sales','stores') }}

{% endsnapshot %}


{% snapshot stores_snapshot_new %}

{{
    config(
      target_schema='snapshots',
      target_database='dbt_labs',
      unique_key='store_id',

      strategy='timestamp',
      updated_at='update_at',
    )
}}

select store_id, store_name, phone, email, street, city, state, zip_code, update_at from {{ source('sales','stores_new') }}

{% endsnapshot %}
with source as (
    select * from {{ source('my_dbt_db', 'raw_orders') }}
),
renamed as (
    select
        id as order_id,
        customer as customer_name,
        store_id as ordered_at_store
    from source
)
select * from renamed
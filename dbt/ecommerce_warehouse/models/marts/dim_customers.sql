SELECT
    customer_id, 
    first_name, 
    last_name, 
    email, 
    city, 
    country
FROM {{ ref('stg_customers') }}

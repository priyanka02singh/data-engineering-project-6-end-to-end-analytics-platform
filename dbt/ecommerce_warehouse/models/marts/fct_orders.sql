SELECT
    CAST(o.order_id AS TEXT) || '-' || CAST(o.product_id AS TEXT) AS order_item_id,
    o.order_id,
    o.customer_id,
    c.first_name,
    c.last_name,
    o.product_id,
    p.product_name,
    p.category,
    p.price,
    o.order_date,
    o.quantity,
    (p.price * o.quantity) AS total_amount

FROM {{ ref('stg_orders') }} o

LEFT JOIN {{ ref('stg_customers') }} c
    ON o.customer_id = c.customer_id

LEFT JOIN {{ ref('stg_products') }} p
    ON o.product_id = p.product_id

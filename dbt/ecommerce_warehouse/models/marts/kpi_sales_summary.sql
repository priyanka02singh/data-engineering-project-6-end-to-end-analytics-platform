SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_items_sold,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value
FROM {{ ref('fct_orders') }}

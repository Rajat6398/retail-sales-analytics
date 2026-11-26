SELECT order_month,
       ROUND(SUM(net_sales), 2) AS revenue,
       COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY order_month
ORDER BY order_month;

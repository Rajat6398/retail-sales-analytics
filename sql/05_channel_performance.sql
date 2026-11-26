SELECT sales_channel,
       COUNT(DISTINCT order_id) AS total_orders,
       ROUND(SUM(net_sales), 2) AS revenue,
       ROUND(AVG(net_sales), 2) AS average_order_value
FROM orders
GROUP BY sales_channel
ORDER BY revenue DESC;

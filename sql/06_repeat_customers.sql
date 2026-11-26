SELECT customer_id,
       COUNT(DISTINCT order_id) AS order_count,
       ROUND(SUM(net_sales), 2) AS lifetime_revenue
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT order_id) > 1
ORDER BY lifetime_revenue DESC
LIMIT 20;

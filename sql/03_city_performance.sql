SELECT city,
       ROUND(SUM(net_sales), 2) AS revenue,
       COUNT(DISTINCT customer_id) AS unique_customers
FROM orders
GROUP BY city
ORDER BY revenue DESC;

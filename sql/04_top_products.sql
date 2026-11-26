SELECT product_name,
       SUM(quantity) AS units_sold,
       ROUND(SUM(net_sales), 2) AS revenue
FROM orders
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

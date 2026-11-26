SELECT category,
       ROUND(SUM(net_sales), 2) AS revenue,
       SUM(quantity) AS units_sold
FROM orders
GROUP BY category
ORDER BY revenue DESC;

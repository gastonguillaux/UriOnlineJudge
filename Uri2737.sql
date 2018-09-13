SELECT l.name, MAX(l.customers_number) AS 'customers_number'
FROM lawyers l
UNION
SELECT l.name, MIN(l.customers_number) AS 'customers_number'
FROM lawyers l
UNION
SELECT 'Average', ROUND(AVG(l.customers_number)) AS 'customers_number'
FROM lawyers l

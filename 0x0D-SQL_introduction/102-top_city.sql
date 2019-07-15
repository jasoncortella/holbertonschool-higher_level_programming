-- displays the top 3 of cities temperature during July and August 

-- display the temperatures
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

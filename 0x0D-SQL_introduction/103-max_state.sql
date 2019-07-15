-- displays the max temperature of each state (ordered by State name).

-- display the temperatures
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;

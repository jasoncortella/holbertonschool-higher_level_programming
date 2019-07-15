-- lists the number of records with the same score in the table second_table

-- list the records
SELECT score, count(*) AS number FROM second_table
GROUP BY score DESC;

-- Calculate the average temperature (Fahrenheit) by city and order by temperature (descending)
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;

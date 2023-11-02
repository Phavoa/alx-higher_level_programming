-- List all records from the table second_table
-- Displaying the score and name, excluding rows without a name value
-- Sorted by descending score
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY `score` DESC;

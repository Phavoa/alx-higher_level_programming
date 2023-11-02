-- List the number of records with the same score in the table second_table
-- Displaying the score and the number of records with the label "number"
-- Sorted by the number of records in descending order
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;

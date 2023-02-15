-- max state
SELECT state, MAX(value) FROM temperatures
GROUP BY state ASC;

-- task 9
SELECT c.id, c.name, s.name
FROM cities as c
LEFT JOIN states as s
ON c.state_id = s.id
ORDER BY c.id

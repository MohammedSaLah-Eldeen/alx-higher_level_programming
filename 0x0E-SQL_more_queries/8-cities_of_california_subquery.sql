-- task 8
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id

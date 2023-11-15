-- task 12
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres as tsg 
ON ts.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title, tsg.genre_id

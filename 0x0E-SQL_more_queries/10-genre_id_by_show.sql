-- task 10
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
JOIN tv_shows_genres AS tsg
ON ts.id = tsg.show_id
ORDER ts.title, tsg.genre_id;

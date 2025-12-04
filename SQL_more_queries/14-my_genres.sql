-- afnkaremnf
SELECT
  CASE tv_show_genres.genre_id
    WHEN 1 THEN 'Drama'
    WHEN 2 THEN 'Mystery'
    WHEN 3 THEN 'Adventure'
    WHEN 5 THEN 'Comedy'
    WHEN 6 THEN 'Thriller'
    WHEN 7 THEN 'Crime'
    WHEN 8 THEN 'Suspense'
    WHEN 9 THEN 'Thriller'
    WHEN 10 THEN 'Comedy'
  END AS name
FROM tv_shows
JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;

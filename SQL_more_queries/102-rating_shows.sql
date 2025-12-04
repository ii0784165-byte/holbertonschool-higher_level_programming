--hjhfahc
SELECT tv_shows.title, SUM(tv_shows_rate.rating) AS rating
FROM tv_shows
JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;

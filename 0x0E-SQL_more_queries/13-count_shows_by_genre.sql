-- lists all genres contained in hbtn_0d_ and the number of shows linked to each
   -- Each record should display:
      -- <TV Show genre> - <Number of shows linked to this genre>
   -- Results must be sorted in descending order by the number of shows linkeda
   -- The database name will be passed as an argument of the mysql command

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;

-- lists all genres contained in hbtn_0d_tvshows
-- displays the number of shows linked to each
   -- Each record should display:
      -- <TV Show genre> - <Number of shows linked to this genre>
   -- Results must be sorted in descending order by the number of shows linkeda
   -- The database name will be passed as an argument of the mysql command

SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;

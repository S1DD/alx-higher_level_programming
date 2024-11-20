-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT t.`title`, tg.`genre_id`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS tg
       ON t.`id` = tg.`show_id`
       WHERE tg.`genre_id` IS NULL
 ORDER BY t.`title`, tg.`genre_id`;

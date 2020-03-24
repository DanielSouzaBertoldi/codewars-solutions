SELECT player_name, games, CAST(ROUND(hits*1.0/at_bats, 3) AS CHAR(5)) AS batting_average
FROM yankees
WHERE at_bats >= 100
ORDER BY batting_average DESC
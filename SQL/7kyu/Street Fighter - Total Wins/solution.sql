SELECT name, SUM(won) as won, SUM(lost) AS lost
FROM fighters, winning_moves
WHERE move_id = winning_moves.id AND move NOT IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY name 
ORDER BY won DESC 
LIMIT 6
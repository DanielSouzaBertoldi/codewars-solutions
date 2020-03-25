SELECT 
  MIN(score) AS min,
  PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY score) AS median,
  MAX(score) as max
FROM result
SELECT c.name, ROUND(((s.math*2)+(s.specific*3)+(s.project_plan*5))/10,2)
FROM candidate c, score s
WHERE s.candidate_id = c.id 
ORDER BY 2 DESC
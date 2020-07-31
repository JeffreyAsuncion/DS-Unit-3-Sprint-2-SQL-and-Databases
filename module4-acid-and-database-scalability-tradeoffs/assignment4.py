"""
-- 1. How many passengers survived, and how many died?
-- survived = 1
-- died = 0

-- total 887
-- survived 342
-- died 545
SELECT *
FROM titantic_table;

SELECT COUNT(survived) as SurvivedCount
FROM titantic_table
WHERE survived = 1;

SELECT COUNT(survived) as SurvivedCount
FROM titantic_table
WHERE survived = 0 ;
"""

"""
-- 2.How many passengers were in each class?

SELECT * 
FROM titantic_table;

SELECT 
	pclass,
	COUNT(pclass)
FROM titantic_table
GROUP BY pclass;


SELECT 
	pclass, 
	COUNT(survived),
CASE
    WHEN survived = 1 THEN 'SURVIVED'
    ELSE 'DIED'
END
FROM titantic_table
GROUP BY pclass, survived
ORDER BY pclass, survived;
"""


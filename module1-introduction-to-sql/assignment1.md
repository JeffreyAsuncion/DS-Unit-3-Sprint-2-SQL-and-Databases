--1. How many total Characters are there?
-- charactercreator_character has 898 total rows
-- total character_count 302 

SELECT
	count(DISTINCT character_id) as character_count
FROM charactercreator_character;

====================================================

2. How many of each specific subclass?
=================================================
-- 3. How many total Items?

SELECT 
	count(distinct name)
FROM armory_item;
==========================================

-- 4. How many of the Items are weapons? How many are not?

SELECT 
	count(ai.item_id) as weapon_count
FROM armory_item ai
JOIN  armory_weapon aw on ai.item_id = aw.item_ptr_id;
====================================================

-- 5. How many Items does each character have? (Return first 20 rows)
-- character_id, item_id


SELECT 
	character_id
	, item_id
FROM charactercreator_character_inventory
GROUP BY character_id;
========================================================  
--6. How many Weapons does each character have? (Return first 20 rows)

--weapons amory_weapon
--character charactercreator_character_inventory

SELECT 
	cci.character_id
	,count(aw.item_ptr_id) as num_of_weapons
FROM charactercreator_character_inventory cci
JOIN armory_weapon aw on cci.item_id = aw.item_ptr_id
GROUP BY cci.character_id
LIMIT 20;
========================================================
--7. On average, how many Items does each Character have?

SELECT AVG(num_of_items) as avg_items_per_char
FROM (
	SELECT 
		cci.character_id
		,count(ai.item_id) as num_of_items
	FROM charactercreator_character_inventory cci
	JOIN armory_item ai on cci.item_id = ai.item_id
	GROUP BY cci.character_id
	)subq
===============================================
-- 8. On average, how many Weapons does each character have?
-- first step
-- weapons
-- character

-- On Average
-- how many Weapons does each character have?
-- two columns character_id, weapon_count
-- row per characters (302)

SELECT
	c.character_id
	,c.name
	,inv.*
	,w.*
	,w.item_ptr_id as weapon_id
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id;



-- 8. On average, how many Weapons does each character have?
-- On Average
-- how many Weapons does each character have?

--- Assume: include characters that don't have any weapons

-- two columns character_id, weapon_count
-- row per characters (302)

SELECT AVG(weapon_count) as avg_weapons_per_char
FROM (
	SELECT
		c.character_id
		--,c."name"
		--,inv.*
		--,w.*
		,count(distinct w.item_ptr_id) as weapon_count
	FROM charactercreator_character c
	LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
	LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id
	GROUP BY c.character_id
) subq
	


------ Chinook.DB

SELECT
	Country,
	COUNT(DISTINCT CustomerId) as customer_count
FROM customers
GROUP BY Country 
ORDER BY customer_count DESC;
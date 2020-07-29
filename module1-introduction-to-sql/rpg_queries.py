import os
import sqlite3

#https://cdn.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf


# construct a path to wherever your database exists
# DB_FILEPATH = "module1-introduction-to-sql/chinook.db"   # / for windows \ of macOs
# DB_FILEPATH = os.path.join("module1-introduction-to-sql","chinook.db")
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db") # the .. is to go up one directory

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

"""
--1. How many total Characters are there?
-- charactercreator_character has 898 total rows
-- total character_count 302 

SELECT
	count(DISTINCT character_id) as character_count
FROM charactercreator_character;
"""

query1 = "SELECT count(DISTINCT character_id) as character_count FROM charactercreator_character;"
#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)
question1 = "1. How many total Characters are there?"
result1 = cursor.execute(query1).fetchall()
print(question1, result1[0])

"""
--2. How many of each specific subclass?

-- charactercreator_character
-- charactercreator_cleric
-- cleric_count = 75
SELECT 
	count(cc.character_Id) as cleric_count
FROM charactercreator_character cc
JOIN  charactercreator_cleric cl ON cc.character_id = cl.character_ptr_id
WHERE(cl.using_shield = 0) AND (cl.mana = 100);

-- charactercreator_character
-- charactercreator_fighter
-- fighter_count = 68 
SELECT 
	count(cc.character_Id) as fighter_count
FROM charactercreator_character cc
JOIN  charactercreator_fighter f ON cc.character_id = f.character_ptr_id
WHERE(f.using_shield = 0) AND (f.rage = 100);

-- charactercreator_character
-- charactercreator_thief
-- thief_count = 108
SELECT 
	count(cc.character_Id) as thief_count
FROM charactercreator_character cc
JOIN  charactercreator_thief t ON cc.character_id = t.character_ptr_id
WHERE(t.is_sneaking = 0) AND (t.energy = 100);

-- charactercreator_character
-- charactercreator_mage
-- mage_count = 108
SELECT 
	count(cc.character_Id) as mage_count
FROM charactercreator_character cc
JOIN  charactercreator_mage m ON cc.character_id = m.character_ptr_id
WHERE(m.has_pet = 1) AND (m.mana = 100);

-- charactercreator_character
-- charactercreator_necromancer
-- necromancer_count = 11
SELECT 
	count(cc.character_Id) as necromancer_count
FROM charactercreator_character cc
LEFT JOIN  charactercreator_mage m ON cc.character_id = m.character_ptr_id
LEFT JOIN  charactercreator_necromancer n ON m.character_ptr_id = n.mage_ptr_id
WHERE(m.has_pet = 1) AND (m.mana = 100) AND (n.talisman_charged);
"""

query = ("SELECT count(cc.character_Id) as cleric_count " + \
    "FROM charactercreator_character cc " + \
    "JOIN  charactercreator_cleric cl ON cc.character_id = cl.character_ptr_id "+ \
    "WHERE(cl.using_shield = 0) AND (cl.mana = 100);")
result2a = cursor.execute(query).fetchone()
print("2. How many of each specific subclass?")
print("\tcleric_count",  result2a)

query = ("SELECT count(cc.character_Id) as fighter_count " + \
    "FROM charactercreator_character cc " + \
    "JOIN  charactercreator_fighter f ON cc.character_id = f.character_ptr_id " + \
    "WHERE(f.using_shield = 0) AND (f.rage = 100);")
result2b = cursor.execute(query).fetchone()
print("\tfigher_count",  result2b)

query = ("SELECT count(cc.character_Id) as thief_count " + \
    "FROM charactercreator_character cc " + \
    "JOIN  charactercreator_thief t ON cc.character_id = t.character_ptr_id " + \
    "WHERE(t.is_sneaking = 0) AND (t.energy = 100);")
result2c = cursor.execute(query).fetchone()
print("\tthief_count",  result2c)

query = ("SELECT count(cc.character_Id) as mage_count " + \
    "FROM charactercreator_character cc " + \
    "JOIN  charactercreator_mage m ON cc.character_id = m.character_ptr_id " + \
    "WHERE(m.has_pet = 1) AND (m.mana = 100);")
result2d = cursor.execute(query).fetchone()
print("\tmage_count",  result2d)

query = ("SELECT count(cc.character_Id) as necromancer_count " + \
    "FROM charactercreator_character cc " + \
    "LEFT JOIN  charactercreator_mage m ON cc.character_id = m.character_ptr_id " + \
    "LEFT JOIN  charactercreator_necromancer n ON m.character_ptr_id = n.mage_ptr_id " + \
    "WHERE(m.has_pet = 1) AND (m.mana = 100) AND (n.talisman_charged);")
result2e = cursor.execute(query).fetchone()
print("\tnecromancer_count",  result2e)



"""
-- 3. How many total Items?

SELECT 
	count(distinct name)
FROM armory_item;
"""

query = ("SELECT count(*) FROM armory_item;")
result3 = cursor.execute(query).fetchone()
print("3. How many total Items?",  result3)


"""
-- 4. How many of the Items are weapons? How many are not?

-- weapon_count = 37
SELECT 
	count(ai.item_id) as weapon_count
FROM armory_item ai
JOIN  armory_weapon aw ON ai.item_id = aw.item_ptr_id;

-- nonweapon_count = 137
-- total items = 174
-- weapons = 37

SELECT 
	count(ai.item_id) as non_weapon_count
FROM armory_item ai
LEFT JOIN  armory_weapon aw ON ai.item_id = aw.item_ptr_id
WHERE aw.item_ptr_id IS NULL;
"""


query = ("SELECT count(ai.item_id) as weapon_count " + \
    "FROM armory_item ai " + \
    "JOIN  armory_weapon aw ON ai.item_id = aw.item_ptr_id;")
result4a = cursor.execute(query).fetchone()
print("4. How many of the Items are weapons?",  result4a)


query = ("SELECT count(ai.item_id) as non_weapon_count " + \
    "FROM armory_item ai " + \
    "LEFT JOIN  armory_weapon aw ON ai.item_id = aw.item_ptr_id " + \
    "WHERE aw.item_ptr_id IS NULL;")
result4b = cursor.execute(query).fetchone()
print("   How many of the Items are NOT weapons?",  result4b)


"""
-- 5. How many Items does each character have? (Return first 20 rows)
-- character_id, item_id


SELECT 
	character_id
	, item_id
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

query = ("SELECT character_id, item_id " + \
    "FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;")
result5 = cursor.execute(query).fetchmany(20)
print("5. How many Items does each character have? (Return first 20 rows)\n")
for row in result5:
    print(row)


"""
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
"""

query = ("SELECT cci.character_id ,count(aw.item_ptr_id) as num_of_weapons "+\
    "FROM charactercreator_character_inventory cci "+\
    "JOIN armory_weapon aw on cci.item_id = aw.item_ptr_id "+\
    "GROUP BY cci.character_id LIMIT 20;")
result6 = cursor.execute(query).fetchmany(20)
print("6. How many Weapons does each character have? (Return first 20 rows)\n")
for row in result6:
    print(row)


"""
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
"""

query = ("SELECT AVG(num_of_items) as avg_items_per_char " + \
    "FROM ( " + \
	"SELECT " + \
		"cci.character_id " + \
		",count(ai.item_id) as num_of_items " + \
	"FROM charactercreator_character_inventory cci " + \
	"JOIN armory_item ai on cci.item_id = ai.item_id " + \
	"GROUP BY cci.character_id)subq")
result7 = cursor.execute(query).fetchone()
print("7. On average, how many Items does each Character have?",  result7)



"""
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
"""	

query = "SELECT AVG(weapon_count) as avg_weapons_per_char " + \
    "FROM ( " + \
	"SELECT " + \
		"c.character_id " + \
		",count(distinct w.item_ptr_id) as weapon_count " + \
	"FROM charactercreator_character c " + \
	"LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id " + \
	"LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id " + \
	"GROUP BY c.character_id) subq;"

result8 = cursor.execute(query).fetchone()
print("8. On average, how many Weapons does each character have?",  result8)
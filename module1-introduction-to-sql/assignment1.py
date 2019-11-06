import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()
query = 'SELECT COUNT(*) FROM charactercreator_character;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Characters: {result}')

query = 'SELECT COUNT(*) FROM charactercreator_cleric;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Clerics: {result}')


query = 'SELECT COUNT(*) FROM charactercreator_fighter;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Fighters: {result}')

query = 'SELECT COUNT(*) FROM charactercreator_mage;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Mages: {result}')


query = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Necros: {result}')


query = 'SELECT COUNT(*) FROM charactercreator_thief;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Thieves: {result}')


query = 'SELECT COUNT(*) FROM armory_item;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Items: {result}')


query = 'SELECT COUNT(*) FROM armory_weapon;'
cur.execute(query)
result = cur.fetchone()[0]
print(f'Total Items: {result}')

print(f'Total Non-Weapon Items: {174 - 37}')

query = 'SELECT charactercreator_character_inventory.character_id, charactercreator_character.name, charactercreator_character_inventory.item_id FROM charactercreator_character, charactercreator_character_inventory WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY charactercreator_character_inventory.character_id LIMIT 20;'
cur.execute(query)
result = cur.fetchall()
print(f'Some Characters and Items: {result}')


import sqlite3

db_path = "pokemon.db"

# This function connects to the DB and returns conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return conn, conn.cursor()

# This function returns Pokemon by Pokemon type
def read_pkmn_by_pkmn_type(pkmn_type):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM pkmn WHERE pkmn_type = ?'
    values = (pkmn_type,)
    results = cur.execute(query, values).fetchall()
    conn.close()
    return results

# This function retrieves 1 Pokemon by Pokemon ID
def read_pkmn_by_pkmn_id(pkmn_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM pkmn WHERE id = ?'
    values = (pkmn_id,)
    result = cur.execute(query, values).fetchone()
    conn.close()
    return result

# This function inserts 1 Pokemon data
def insert_pet(pkmn_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO pkmn (pkmn_type, name, description, url) VALUES (?, ?, ?, ?)'
    values = (pkmn_data['pokemon_type'], pkmn_data['name'], pkmn_data['description'], pkmn_data['url'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

# This function updates a record
def update_pkmn(pkmn_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE pkmn SET pkmn_type=?, name=?, description=?, url=? WHERE id=?"
    values = (pkmn_data['pokemon_type'], pkmn_data['name'], pkmn_data['description'], pkmn_data['url'], pkmn_data['pokemon_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

# This function deletes a record
def delete_pet(pkmn_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM pkmn WHERE id = ?"
    values = (pkmn_id,)
    cur.execute(query, values)
    conn.commit()
    conn.close()
import psycopg2
import requests
import hidden
import json  

def fetch_and_store_pokemon_data():
    # Get the database connection parameters from the hidden module
    secrets = hidden.secrets()

    conn = psycopg2.connect(
        host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'],
        user=secrets['user'],
        password=secrets['pass']
    )
    cur = conn.cursor()

    default_url = 'https://pokeapi.co/api/v2/pokemon/1/'

    # Code for creating the table (if it doesn't exist)
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);
    '''
    cur.execute(sql_create_table)

    many = 0
    count = 0
    chars = 0

    while count < 100:
        if many < 1:
            conn.commit()
            sval = input('How many documents:')
            if len(sval) < 1:
                break
            many = int(sval)

        url = f'https://pokeapi.co/api/v2/pokemon/{count + 1}/'
        response = requests.get(url)
        data = response.json()
        
        # Convert the data dictionary to a JSON string
        data_json = json.dumps(data)

        sql_insert = 'INSERT INTO pokeapi (id, body) VALUES (%s, %s);'
        cur.execute(sql_insert, (count + 1, data_json))

        count += 1
        chars += len(data_json)

        many -= 1

        if count % 25 == 0:
            conn.commit()
            print(f'{count} loaded...')

    print(f'Loaded {count} documents, {chars} characters')

    # Commit and close the connection
    conn.commit()
    cur.close()

if __name__ == "__main__":
    fetch_and_store_pokemon_data()

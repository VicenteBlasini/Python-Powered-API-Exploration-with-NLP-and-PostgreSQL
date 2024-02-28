Explanation of Files:
---------------------

1. pokemon.py:
   - This Python script connects to the PokeAPI and fetches data for X Pokémon.
   - It then stores the fetched data in a PostgreSQL database.
   - The script demonstrates fetching data from an API, working with JSON data, and interacting with a PostgreSQL database.

2. hidden.py:
   - This module contains functions to retrieve sensitive information like database connection parameters.
   - It provides functions to return credentials for different environments, such as development, production, or testing.

3. myutils.py:
   - This module contains utility functions for database operations.
   - It includes functions for querying values, querying rows, and executing queries.

4. swapi.py:
   - This Python script pulls data from the swapi.py4e.com API and inserts it into a PostgreSQL table named 'swapi'.
   - It demonstrates fetching data from an external API, handling HTTP requests, and interacting with a PostgreSQL database.

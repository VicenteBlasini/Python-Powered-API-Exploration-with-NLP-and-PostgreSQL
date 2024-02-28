# Python-Powered PokeAPI Exploration with NLP and PostgreSQL

## Overview

This repository contains Python scripts for exploring the PokeAPI, performing Natural Language Processing (NLP) tasks, and storing the data in a PostgreSQL database. The project demonstrates how to fetch data from an API, analyze text using NLP techniques, and interact with a relational database.

## Files

1. **1era_Prueba.py**:
   - This Python script connects to the PokeAPI and fetches data for 100 Pokémon.
   - It then stores the fetched data in a PostgreSQL database.
   - The script demonstrates fetching data from an API, working with JSON data, and interacting with a PostgreSQL database.

2. **hidden.py**:
   - This module contains functions to retrieve sensitive information like database connection parameters.
   - It provides functions to return credentials for different environments, such as development, production, or testing.

3. **myutils.py**:
   - This module contains utility functions for database operations.
   - It includes functions for querying values, querying rows, and executing queries.

4. **swapi.py**:
   - This Python script pulls data from the swapi.py4e.com API and inserts it into a PostgreSQL table named 'swapi'.
   - It demonstrates fetching data from an external API, handling HTTP requests, and interacting with a PostgreSQL database.

5. **pokemon.py**:
   - Similar to `1era_Prueba.py`, this script connects to the PokeAPI and fetches data for 100 Pokémon.
   - It stores the fetched data in a PostgreSQL database table named 'pokeapi'.
   - The script follows a similar structure to `1era_Prueba.py` but might include slight variations or improvements.

## Usage

To use these scripts:

1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up PostgreSQL and create a database for storing the data.
4. Update the database connection parameters in `hidden.py`.
5. Run the desired Python script to fetch data from the PokeAPI or other sources and store it in the PostgreSQL database.

## Contributions

Contributions to this repository are welcome! If you have suggestions for improvements or new features related to working with APIs, NLP, or PostgreSQL, feel free to open an issue or submit a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

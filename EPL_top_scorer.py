
import os
import logging 
import requests 
import psycopg2
import pandas as pd 
from dotenv import load_dotenv
from requests.exceptions import HTTPError, RequestException, Timeout

# Load the environment variables 
load_dotenv()

API_KEY         =   os.getenv("API_KEY")
API_HOST        =   os.getenv("API_HOST")
LEAGUE_ID       =   os.getenv("LEAGUE_ID")
SEASON          =   os.getenv("SEASON")
DB_NAME         =   os.getenv("DB_NAME")
DB_USERNAME     =   os.getenv("DB_USERNAME")
DB_PASSWORD     =   os.getenv("DB_PASSWORD")
DB_HOST         =   os.getenv("DB_HOST")
DB_PORT         =   os.getenv("DB_PORT")



# Set up the logger 
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


# Instantiate the logger object
logger = logging.getLogger()


# Add the file handler to the logger
logger.addHandler(file_handler)


# Add the console handler to the logger
logger.addHandler(console_handler)


url           =   "https://api-football-beta.p.rapidapi.com/players/topscorers"
headers       =   {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}
query_string  =   {'season': SEASON,'league': LEAGUE_ID}



# response      =   requests.request("GET", url, headers=headers, params=query_string)
try:
    api_response = requests.get(url, headers=headers, params=query_string, timeout=15)
    api_response.raise_for_status() 

except HTTPError as http_err:
    logger.error(f'HTTP error occurred: {http_err}')

except Timeout:
    logger.error('Request timed out after 15 seconds')

except RequestException as request_err:
    logger.error(f'Request error occurred: {request_err}')


#where the real deal starts
scorer_data = api_response.json()['response']

# Extracting the standings information
standings = scorer_data[0]['statistics']


# List to hold our extracted data
data_list = []

# Parsing through each team's standing
for team_info in standings:
    team_name            =   team_info['team']['name']
    league_name      =  team_info['league']['name']
    appearance       =   team_info['games']['appearences']
    
    
    data_list.append([team_name, league_name ,appearance ])

# Create the dataFrame
standings_df    =   pd.DataFrame(data_list)


# Display the dataFrame
#print(standings_df.to_string(index=False))

# Set up Postgres database connection
postgres_connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Get a cursor from the database
cur = postgres_connection.cursor()

# Use SQL to create a table for the Premier League 
create_table_sql_query = """ 
    CREATE TABLE IF NOT EXISTS stat_data (
            team_name          VARCHAR(255),
            league_name        VARCHAR(255),
            appearance         INTEGER
    );
"""

# Run the SQL query 
cur.execute(create_table_sql_query)

# Commit the transaction 
postgres_connection.commit()

print('inserting file to DB..')
# Use SQL to insert data into the Premier League table 
insert_data_sql_query = """
    INSERT INTO public.stat_data (
            team_name, league_name ,appearance            
    )
    VALUES (%s, %s, %s)

    ON CONFLICT (position) DO UPDATE SET
    team_name               =   EXCLUDED.team_name, 
    league_name       =   EXCLUDED.league_name, 
    appearance              =   EXCLUDED.appearance
    
"""

# Commit the transaction 
postgres_connection.commit()

print('creating csv file..')
standings_df.to_csv(path_or_buf=f'stat/stat.csv', index=False)

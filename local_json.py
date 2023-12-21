import logging 
import pandas as pd 

#JSON Data payload
response = [
    {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'Jamie Richard', 'lastname': 'Vardy', 'age': 36, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Leicester', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 1, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
   {
        'player': {'id': 18789, 'name': 'Joachim. Wardy', 'firstname': 'Jamiu Richardie', 'lastname': 'Wardy', 'age': 28, 'birth': {'date': '1987-01-11', 'place': 'London', 'country': 'England'}, 'nationality': 'England', 'height': '170 cm', 'weight': '76 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Leicester', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 30, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
   {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'Jamiere Richardiho', 'lastname': 'Vardoy', 'age': 26, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Leicester', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 3, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
   {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'Uner Jamo', 'lastname': 'Kai', 'age': 30, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Leicester', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 22, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
   {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'Olabisi Jane', 'lastname': 'Uche', 'age': 37, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Leicester', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 5, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
   {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'Philip Duns', 'lastname': 'Kola', 'age': 38, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Leicester', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 15, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
   {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'Tunde Ednit', 'lastname': 'Tobi', 'age': 39, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Arsenal', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 30, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

},
  {
        'player': {'id': 18788, 'name': 'J', 'firstname': 'John Doe', 'lastname': 'Mike', 'age': 36, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Man United', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 15, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

}, {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': 'John Doe', 'lastname': 'Mike', 'age': 36, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Man United', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 15, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

}, {
        'player': {'id': 18788, 'name': 'Vard', 'firstname': 'John', 'lastname': 'Mike', 'age': 36, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Man United', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 15, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

}, {
        'player': {'id': 18788, 'name': 'J. Vardy', 'firstname': ' Doe', 'lastname': 'Mike', 'age': 36, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Man United', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 15, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

}, {
        'player': {'id': 18788, 'name': 'Vardy', 'firstname': 'John Doe', 'lastname': 'Mike', 'age': 36, 'birth': {'date': '1987-01-11', 'place': 'Sheffield', 'country': 'England'}, 'nationality': 'England', 'height': '179 cm', 'weight': '74 kg', 'injured': False, 'photo': 'https://media-4.api-sports.io/football/players/18788.png'},
        'statistics': [{'team': {'id': 46, 'name': 'Man United', 'logo': 'https://media-4.api-sports.io/football/teams/46.png'}, 
        'league': {'id': 39, 'name': 'Premier League', 'country': 'England', 'logo': 'https://media-4.api-sports.io/football/leagues/39.png', 'flag': 'https://media-4.api-sports.io/flags/gb.svg', 'season': 2019}, 
        'games': {'appearences': 15, 'lineups': 34, 'minutes': 3034, 'number': None, 'position': 'Attacker', 'rating': '7.257142', 'captain': False}, 'substitutes': {'in': 1, 'out': 2, 'bench': 1}, 'shots': {'total': 89, 'on': 43}, 
        'goals': {'total': 23, 'conceded': None, 'assists': 5, 'saves': None}, 'passes': {'total': 312, 'key': 32, 'accuracy': 70}, 'tackles': {'total': 15, 'blocks': 4, 'interceptions': 2}, 'duels': {'total': 260, 'won': 104}, 
        'dribbles': {'attempts': 47, 'success': 23, 'past': None}, 'fouls': {'drawn': 12, 'committed': 20}, 'cards': {'yellow': 2, 'yellowred': 0, 'red': 0}, 'penalty': {'won': 1, 'commited': None, 'scored': 4, 'missed': 1, 'saved': None}}]

}
]

# Set up the logger 
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler
file_handler = logging.FileHandler('logs')
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

logger.info('Extracting players statistics')
player_stat = []
player_bio = []

for players in response:
        f_name  =   players['player']['firstname']
        l_name  =   players['player']['lastname']
        age     = players['player']['age']
        place_of_birth = players['player']['birth']['place']

        player_bio.append([f_name,l_name, age, place_of_birth])


        stat = response[0]['statistics']        
# Parsing through each team's standing
        for team_info in stat:
                team_name        =   team_info['team']['name']
                league_name      =  team_info['league']['name']
                appearance       =   team_info['games']['appearences']
                        
                player_stat.append([team_name, league_name ,appearance ])

        
count_bio = len(player_bio)
df_bio = pd.DataFrame(player_bio, columns=['Firstname','Lastname','Age','PlaceOfBirth'])
logger.info(f'a total of {count_bio} was extracted')

count_extracted_player_stat = len(player_stat)    
logger.info(f'a total of {count_extracted_player_stat} was extracted')

# Create the dataFrame
logger.info('Converting to DataFrame')
standings_df    =   pd.DataFrame(player_stat, columns=['Club','League', 'Appearances'])

logger.info('Extracting players biography')

# Display the dataFrame
#print(standings_df.to_string(index=False))

#merging both dataFrames
df = pd.concat([df_bio , standings_df], axis=1)

logger.info("Creating a CSV file")
df.to_csv(path_or_buf=f'stat/local.csv', index=False)
logger.info("Successful")

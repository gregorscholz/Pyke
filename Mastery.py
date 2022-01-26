import requests
import Pyke

class Champion_Mastery:
    
    def __init__(self, summoner_id: str, champion_id: str) -> None:
        __json = Champion_Mastery.__champion_mastery_data(summoner_id, champion_id)
        self.champion_points_until_next_level = Champion_Mastery.__champion_points_until_next_level(__json)     # Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion
        self.chest_granted = Champion_Mastery.__chest_granted(__json)                                           # Is chest granted for this champion or not in current season
        self.champion_id = champion_id                                                              # Champion ID for this entry
        self.last_play_time = Champion_Mastery.__last_play_time(__json)                                         # Last time this champion was played by this player - in Unix milliseconds time format
        self.champion_level = Champion_Mastery.__champion_level(__json)                                         # Champion level for specified player and champion combination
        self.summoner_id = Champion_Mastery.summoner_id                                                         # Summoner ID for this entry. (Encrypted)
        self.champion_points = Champion_Mastery.__champion_points(__json)                                       # Total number of champion points for this player and champion combination - they are used to determine championLevel
        self.champion_points = Champion_Mastery.__champion_points_since_last_level(__json)                      # Number of points earned since current level has been achieved
        self.tokens_earned = Champion_Mastery.__tokens_earned(__json)                                           # The token earned for this champion at the current championLevel. When the championLevel is advanced the tokensEarned resets to 0
    
    def __champion_mastery_data(summoner_id, champion_id):
        response = requests.get(f'https://{Pyke.Pyke.region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}?api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()
    
    def __champion_points_until_next_level(__json):
        return __json['championPointsUntilNextLevel']
    
    def __chest_granted(__json):
        return __json['chestGranted']
    
    def __last_play_time(__json):
        return __json['lastPlayTime']
    
    def __champion_level(__json):
        return __json['championLevel']
    
    def __champion_points(__json):
        return __json['championPoints']
    
    def __champion_points_since_last_level(__json):
        return __json['championPointsSinceLastLevel']
    
    def __tokens_earned(__json):
        return __json['tokensEarned']
    
    
class Champion_Masteries:
    
    def __init__(self, summoner_id) -> None:
        __json = Champion_Masteries.__champion_masteries_data(summoner_id)
        self.champion_mastery_list = Champion_Masteries.__get_list(__json)                          # list of all champion masteries
        
    def __champion_masteries_data(summoner_id):
        response = requests.get(f'https://{Pyke.Pyke.region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()
    
    def __get_list(__json):
        return __json
    

class Mastery_Score:
    
    def __init__(self, id) -> None:
        __json = Mastery_Score.__mastery_score_data(id)
        self.mastery_score = Mastery_Score.__mastery_score(__json)
        
    def __mastery_score_data(id):
        response = requests.get(f'https://{Pyke.Pyke.region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{id}?api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()
    
    def __mastery_score(__json):
        return __json
import requests
import Pyke

class Match_History:
    
    def __init__(self, puuid: str, region: str = 'europe', start_time: int = None, end_time: int = None, queue: int = None, type: str = None, start: int = 0, count: int = 20) -> None:
        __json = Match_History.__match_history_data(puuid, region, start_time, end_time, queue, type, start, count)
        self.match_history = Match_History.__match_history(__json)
    
    def __match_history_data(puuid: str, region: str, start_time: int, end_time: int, queue: int, type: str, start: int, count: int):
        response = requests.get(f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={start_time}&endTime={end_time}&queue={queue}&type={type}&start={start}&count={count}&api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()
    
    def __match_history(__json):
           return __json[0]
       

class Match:
        
        def __init__(self, id: str, region: str = 'europe') -> None:
            __json = Match.__match_data()
            
            # metadata
            self.data_version = self.__data_version(__json['metadata'])                 # Match data version
            self.match_id = id                                                          # Match id
            self.participants_puuids = self.__participants_puuids(__json['metadata'])   # A list of participant PUUIDs
            
            # info
            self.game_creation = self.__game_creation(__json['info'])                   # Unix timestamp for when the game is created on the game server (i.e., the loading screen)
            self.game_duration = self.__game_duration(__json['info'])                   # Prior to patch 11.20, this field returns the game length in milliseconds calculated from gameEndTimestamp - gameStartTimestamp. Post patch 11.20, this field returns the max timePlayed of any participant in the game in seconds, which makes the behavior of this field consistent with that of match-v4. The best way to handling the change in this field is to treat the value as milliseconds if the gameEndTimestamp field isn't in the response and to treat the value as seconds if gameEndTimestamp is in the response.
            self.game_end_timestamp = self.__game_end_timestamp(__json['info'])         # Unix timestamp for when match ends on the game server. This timestamp can occasionally be significantly longer than when the match "ends". The most reliable way of determining the timestamp for the end of the match would be to add the max time played of any participant to the gameStartTimestamp. This field was added to match-v5 in patch 11.20 on Oct 5th, 2021.
            self.game_id = self.__game_id(__json['info'])                               # 
            self.game_mode = self.__game_mode(__json['info'])                           # Refer to the Game Constants documentation
            self.game_name = self.__game_name(__json['info'])                           #
            self.game_start_timestamp = self.__game_start_timestamp(__json['info'])     # Unix timestamp for when match starts on the game server
            self.game_type = self.__game_type(__json['info'])                           #
            self.game_version = self.__game_version(__json['info'])                     # The first two parts can be used to determine the patch a game was played on
            self.map_id = self.__map_id(__json['info'])                                 # Refer to the Game Constants documentation
            self.participants = self.__participants(__json['info'])                     # 
            self.platform_id = self.__platform_id(__json['info'])                       # Platform where the match was played
            self.queue_id = self.__queue_id(__json['info'])                             # Refer to the Game Constants documentation
            self.teams = self.__teams(__json['info'])                                   # 
            self.tournament_code = self.__tournament_code(__json['info'])               # Tournament code used to generate the match. This field was added to match-v5 in patch 11.13 on June 23rd, 2021
        
        def __match_data(id: str, region):
            response = requests.get(f'https://{region}.api.riotgames.com/lol/match/v5/matches/{id}?api_key={Pyke.Pyke.token}')
            response.encoding = 'ISO-8859-1'
            return response.json()
        
        # metadata
        def __data_version(__json):
            return __json['dataVersion']
        
        def __participants_puuids(__json):
            return __json['participants']
        
        # info
        def __game_creation(__json):
            return __json['gameCreation']
        
        def __game_duration(__json):
            return __json['gameDuration']
        
        def __game_end_timestamp(__json):
            return __json['gameEndTimestamp']
        
        def __game_id(__json):
            return __json['gameId']
        
        def __game_mode(__json):
            return __json['gameMode']
        
        def __game_name(__json):
            return __json['gameName']
        
        def __game_start_timestamp(__json):
            return __json['gameStartTimestamp']
        
        def __game_type(__json):
            return __json['gameType']
        
        def __game_version(__json):
            return __json['gameVersion']
        
        def __map_id(__json):
            return __json['mapId']
        
        def __participants(__json):
            return __json['participants']
        
        def __platform_id(__json):
            return __json['platformId']
        
        def __queue_id(__json):
            return __json['queueId']
        
        def __teams(__json):
            return __json['teams']
        
        def __tournament_code(__json):
            return __json['tournamentCode']
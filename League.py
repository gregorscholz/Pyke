import requests
import Pyke

class League_by_summoner():
    
    def __init__(self, id: str) -> None:
        __json = League_by_summoner.__league_data(id)
        self.league_id = League_by_summoner.__league_id(__json)
        self.queue_type = League_by_summoner.__queue_type(__json)
        self.tier = League_by_summoner.__tier(__json)
        self.rank = League_by_summoner.__rank(__json)
        self.league_points = League_by_summoner.__league_points(__json)       # The player's division within a tie
        self.wins = League_by_summoner.__wins(__json)                         # Winning team on Summoners Rift
        self.losses = League_by_summoner.__losses(__json)                     # Losing team on Summoners Rift
        self.hot_streak = League_by_summoner.__hot_streak(__json)
        self.veteran = League_by_summoner.__veteran(__json)
        self.fresh_blood = League_by_summoner.__fresh_blood(__json)
        self.inactive = League_by_summoner.__inactive(__json)
            
    def __league_data(id: str):
        response = requests.get(f'https://{Pyke.Pyke.region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()[0]
    
    def __league_id(__json):
        return __json['leagueId']
    
    def __queue_type(__json):
        return __json['queueType']
    
    def __tier(__json):
        return __json['tier']
    
    def __rank(__json):
        return __json['rank']
    
    def __league_points(__json):
        return __json['leaguePoints']
    
    def __wins(__json):
        return __json['wins']
    
    def __losses(__json):
        return __json['losses']
    
    def __veteran(__json):
        return __json['veteran']
    
    def __inactive(__json):
        return __json['inactive']
    
    def __fresh_blood(_json):
        return _json['freshBlood']
    
    def __hot_streak(__json):
        return __json['hotStreak']
    
    
class League_by_queue():
    
    def __init__(self, elo: str, queue: str) -> None:
        __json = League_by_queue.__league_data(elo=elo.lower(), queue=queue)
        self.league_id = League_by_queue.__league_id(__json)
        self.entries = League_by_queue.__entries(__json)
        self.tier = League_by_queue.__tier(__json)
        self.name = League_by_queue.__name(__json)
        self.queue = League_by_queue.__queue(__json)
        
    def __league_data(elo: str = None, queue: str = None):
        response = requests.get(f'https://{Pyke.Pyke.region}.api.riotgames.com/lol/league/v4/{elo}leagues/by-queue/{queue}?api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()
    
    def __tier(__json):
        return __json['tier']
    
    def __league_id(__json):
        return __json['leagueId']
    
    def __name(__json):
        return __json['name'] 
    
    def __entries(__json):
        return __json['entries']
    
    def __queue(__json):
        return __json['queue']
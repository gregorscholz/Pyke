import requests
import Pyke

# Represents a summoner
class Summoner():  
    
    def __init__(self, summoner_name: str) -> None:
        __json = Summoner.__summoner_data(summoner_name)
        self.account_id = Summoner.__account_id(__json)                     # Encrypted account ID. Max length 56 characters
        self.profile_icon_id = Summoner.__profile_icon_id(__json)           # ID of the summoner icon associated with the summoner
        self.revision_date = Summoner.__revision_date(__json)               # Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: summoner name change, summoner level change, or profile icon change
        self.summoner_name = summoner_name                                  # Summoner name
        self.id = Summoner.__id(__json)                                     # Encrypted summoner ID. Max length 63 characters
        self.puuid = Summoner.__puuid(__json)                               # Encrypted PUUID. Exact length of 78 characters
        self.summoner_level = Summoner.__summoner_level(__json)             # Summoner level associated with the summoner
    
    def __summoner_data(summoner_name: str):
        response = requests.get(f'https://{Pyke.Pyke.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={Pyke.Pyke.token}')
        response.encoding = 'ISO-8859-1'
        return response.json()
    
    def __account_id(__json):
        return __json['accountId']
    
    def __profile_icon_id(__json):
        return __json['profileIconId']
    
    def __revision_date(__json):
        return __json['revisionDate']
    
    def __id(__json):
        return __json['id']
    
    def __puuid(__json):
        return __json['puuid']
    
    def __summoner_level(__json):
        return __json['summonerLevel']
# Pyke
A Python framework for the Riot Games API

I am still a beginner with the Python programming language therefore don't expect the perfect code.
This is also just a side project and does not have my highest priority.



## Example
```python
from Pyke import Pyke
from Summoner import Summoner
from League import League_by_summoner


Pyke.set_token('YOUR-TOKEN')
Pyke.set_region('euw1')

summoner = Summoner('Don Noway')
print(f'name:                {summoner.summoner_name}')
print(f'level:               {str(summoner.summoner_level)}')
print()
league = League_by_summoner(summoner.id)
print(f'tier:                {league.tier}')
print(f'lp:                  {league.league_points}')

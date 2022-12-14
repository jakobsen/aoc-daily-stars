# Dagens stjerner

Du trenger pakkene listet i [`requirements.txt`](/requirements.txt):
```bash
python -m pip install -r requirements.txt
```
Du trenger også verdien til `session`-cookien din på [adventofcode.com](https://adventofcode.com) og `ID`-en til leaderboardet du vil bruke. Sistnevnte finner du i URL-en til leaderboardet:
```
https://adventofcode.com/leaderboard/private/view/[id-her]
```
Legg begge deler i en `.env`-fil i samme mappe som `api.py`:
```env
SESSION=cookie
LEADERBOARD_ID=id
```

Scriptet kjøres på vanlig måte med et valgfritt argument som er dagen du vil se tider for:
```
python api.py [dag_her]
```
f.eks.
```
python api.py 1
```
Dersom du ikke oppgir en dag bruker den dagen i dag.

Resultater caches i en lokal fil i 15 minutter før scriptet vil gjøre et nytt request. Om du vil ha nye resultater med en gang kan du slette filen.
import requests
import pandas as pd
import json

#episodes
data = pd.DataFrame()
url = "https://www.breakingbadapi.com/api/episodes"
JSONContent = requests.get(url).json()
episodes = []
for i in range(len(JSONContent)):
    episodes.append(JSONContent[i])
    episodes[i]['characters'] = ", ".join(episodes[i]['characters'])
    df = pd.DataFrame(episodes[i], index=[i+1])
    data = data.append(df)
data.to_csv('episodes.csv', index=False)

#characters
data = pd.DataFrame()
url = "https://www.breakingbadapi.com/api/characters"
JSONContent = requests.get(url).json()
characters = []
for i in range(len(JSONContent)):
    characters.append(JSONContent[i])
    characters[i]['occupation'] = ", ".join(characters[i]['occupation'])
    characters[i]['appearance'] = ", ".join(str(int) for int in characters[i]['appearance'])
    characters[i]['better_call_saul_appearance'] = ", ".join(str(int) for int in characters[i]['better_call_saul_appearance'])
    df = pd.DataFrame(characters[i], index=[i+1])
    data = data.append(df)
data.to_csv('characters.csv', index=False)

#quotes
data = pd.DataFrame()
url = "https://www.breakingbadapi.com/api/quotes"
JSONContent = requests.get(url).json()
quotes = []
for i in range(len(JSONContent)):
    quotes.append(JSONContent[i])
    df = pd.DataFrame(quotes[i], index=[i+1])
    data = data.append(df)
data.to_csv('quotes.csv', index=False)

#deaths
data = pd.DataFrame()
url = "https://www.breakingbadapi.com/api/deaths"
JSONContent = requests.get(url).json()
deaths = []
for i in range(len(JSONContent)):
    deaths.append(JSONContent[i])
    df = pd.DataFrame(deaths[i], index=[i+1])
    data = data.append(df)
    data = data.sort_values(by=['death_id'], ascending=True)
data.to_csv('deaths.csv', index=False)
import requests

def get_poke_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    if response.ok:
            data = response.json()
            poke_dict = {}
            poke_dict['Name'] = data['name']
            poke_dict['Ability 1'] = data['abilities'][0]['ability']['name']
            poke_dict['Base XP'] = data['base_experience']
            poke_dict['Shiny URL'] = data['sprites']['front_shiny']
            poke_dict['Base ATK'] = data['stats'][1]['base_stat']
            poke_dict['Base HP'] = data['stats'][0]['base_stat']
            poke_dict['Base DEF'] = data['stats'][2]['base_stat']
    # print (poke_dict)
    else:
        return f'Please input a valid search term'
    return poke_dict


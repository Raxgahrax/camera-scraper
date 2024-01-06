import os
import requests
import re
import time
from colorama import Fore, Back
from user_agent import generate_user_agent as RandomUserAgent
from concurrent.futures import ThreadPoolExecutor

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.insecam.org",
    "Upgrade-Insicure-Requests": "1",
    "User-Agent": RandomUserAgent(),
}

def scrape(url):
    request = requests.get(url, headers=headers)
    return request

def is_address_online(address):
    try:
        response = requests.get(address, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_country_codes():
    response = requests.get("http://www.insecam.org/en/jsoncountries/", headers=headers)
    if response.status_code == 200:
        countries = response.json()['countries']
        return countries
    else:
        print("Échec de la récupération des codes de pays. Nouvelle tentative dans 5 secondes...")
        time.sleep(5)
        return get_country_codes()  # Réessayer la requête après un délai de 5 secondes

def scan_country(country_code, country_name):
    result = requests.get('http://www.insecam.org/en/bycountry/' + country_code, headers=headers)

    bold, green, white, reset, back_reset, back_black = '\033[1m', Fore.LIGHTGREEN_EX, Fore.WHITE, Fore.RESET, Back.RESET, Back.BLACK
    addresses = []

    with ThreadPoolExecutor(max_workers=100) as execute:
        results = execute.map(scrape, [f'http://www.insecam.org/en/bycountry/{country_code}/?page={page}' for page in range(1, int(re.findall(r'pagenavigator\("\?page=", (\d+)', result.text)[0]) + 1)])
        for result in results:
            for IP_ADDRESS in re.findall(r"http://\d+.\d+.\d+.\d+:\d+", result.text):
                if is_address_online(IP_ADDRESS) and IP_ADDRESS not in addresses:
                    print(bold, back_black, green + '( + ) Live Stream:', IP_ADDRESS, '|', 'IP & Port:', IP_ADDRESS.split('//')[1], reset, back_reset)
                    addresses.append(IP_ADDRESS)

    country_folder = os.path.join('output_countries', str(country_name))
    os.makedirs(country_folder, exist_ok=True)

    unique_addresses = list(set(addresses))  # Filtrer les adresses uniques

    valid_addresses = []
    for link in unique_addresses:
        if is_address_online(link):
            valid_addresses.append(link)

    with open(os.path.join(country_folder, country_code + '.txt'), 'w') as file:
        file.truncate(0)
        for link in valid_addresses:
            file.write(link + '\n')
        print(bold + white + '(!) Successfully scraped and verified', len(valid_addresses), 'unique Live Streams & IP Addresses and saved them in', country_folder + '/' + country_code + '.txt.', reset)

    return valid_addresses

# Vérifier la présence du dossier output_countries
if not os.path.exists('output_countries'):
    os.makedirs('output_countries')

# Récupérer les codes et noms des pays
countries = get_country_codes()

# Récupérer la valeur de la constante Country (pays)
Country = 'FR'  # Changez cette valeur pour 'All', un ou plusieurs code de pays spécifique

if Country == 'All':
    # Scanner tous les pays
    for code, details in countries.items():
        valid_addresses = scan_country(code, details["country"])  # Utilisation de la clé "country" pour obtenir le nom du pays
        for addr in valid_addresses:
            if not is_address_online(addr):
                print(f'Suppression de {addr} car elle ne répond pas.')
                with open(os.path.join('output_countries', details["country"], f'{code}.txt'), 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        if line.strip() != addr:
                            f.write(line)
                    f.truncate()
elif Country in countries:
    # Scanner un pays spécifique ou une liste de pays
    valid_addresses = scan_country(Country, countries[Country]["country"])  # Utilisation de la clé "country" pour obtenir le nom du pays
    for addr in valid_addresses:
        if not is_address_online(addr):
            print(f'Suppression de {addr} car elle ne répond pas.')
            with open(os.path.join('output_countries', countries[Country]["country"], f'{Country}.txt'), 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if line.strip() != addr:
                        f.write(line)
                f.truncate()
else:
    print("Code de pays ou valeur 'All' non valide")

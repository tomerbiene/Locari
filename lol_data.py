import requests

# Locari - Genişletilmiş Taktiksel Overall Haritası (78 - 99 Skalası)
CUSTOM_OVERALLS = {
    "Kai'Sa": 97, "Ezreal": 96, "Jinx": 95, "Aphelios": 94, "Xayah": 94, "Draven": 93,
    "Caitlyn": 92, "Jhin": 91, "Lucian": 90, "Zeri": 90, "Varus": 89, "Ashe": 88,
    "Vayne": 88, "Miss Fortune": 87, "Tristana": 86, "Sivir": 85, "Samira": 85,
    "Kalista": 84, "Nilah": 83, "Twitch": 83, "Kog'Maw": 82, "Smolder": 81,
    "Thresh": 99, "Rakan": 97, "Lulu": 95, "Nautilus": 95, "Leona": 94, "Braum": 94,
    "Bard": 93, "Janna": 92, "Pyke": 92, "Renata Glasc": 91, "Alistar": 91, "Nami": 90,
    "Milio": 90, "Rell": 89, "Karma": 89, "Blitzcrank": 88, "Taric": 88, "Morgana": 87,
    "Senna": 87, "Soraka": 86, "Zilean": 86, "Yuumi": 84, "Zyra": 83, "Vel'Koz": 81,
    "Orianna": 98, "Azir": 97, "Ahri": 96, "Sylas": 95, "LeBlanc": 94, "Syndra": 94,
    "Viktor": 94, "Akali": 93, "Hwei": 93, "Taliyah": 92, "Twisted Fate": 91,
    "Galio": 91, "Ryze": 90, "Cassiopeia": 90, "Yasuo": 89, "Yone": 89, "Lissandra": 88,
    "Zoe": 88, "Ekko": 87, "Anivia": 87, "Vex": 87, "Zed": 86, "Veigar": 86,
    "Malzahar": 85, "Naafiri": 84, "Fizz": 84, "Katarina": 84, "Talon": 83, "Lux": 83,
    "Xerath": 82, "Brand": 82, "Swain": 82, "Seraphine": 81, "Aurelion Sol": 81,
    "Lee Sin": 99, "Viego": 97, "Jarvan IV": 96, "Xin Zhao": 95, "Sejuani": 94,
    "Vi": 94, "Lillia": 93, "Graves": 93, "Nocturne": 92, "Bel'Veth": 92, "Nidalee": 91,
    "Kindred": 91, "Kha'Zix": 90, "Zac": 90, "Maokai": 89, "Elise": 89, "Hecarim": 88,
    "Wukong": 88, "MonkeyKing": 88, "Skarner": 87, "Rengar": 87, "Evelynn": 86, "Fiddlesticks": 86,
    "Shaco": 85, "Briar": 85, "Rek'Sai": 84, "Warwick": 84, "Nunu & Willump": 83,
    "Nunu": 83, "Amumu": 83, "Master Yi": 82, "Ivern": 82, "Rammus": 81,
    "Kayn": 91, "Karthus": 80, "Olaf": 86, "Camille": 98, "Aatrox": 97, "Jax": 97,
    "Gwen": 96, "Fiora": 95, "Ornn": 94, "K'Sante": 94, "Renekton": 93, "Gnar": 92,
    "Gragas": 91, "Jayce": 91, "Gangplank": 90, "Rumble": 90, "Shen": 90, "Sett": 89,
    "Poppy": 89, "Mordekaiser": 88, "Darius": 88, "Irelia": 88, "Sion": 87, "Malphite": 87,
    "Volibear": 86, "Illaoi": 85, "Urgot": 85, "Cho'Gath": 84, "Kennen": 84, "Kled": 83,
    "Dr. Mundo": 83, "Tryndamere": 82, "Nasus": 82, "Yorick": 82, "Trundle": 81,
    "Udyr": 81, "Singed": 80, "Teemo": 79, "Garen": 79, "Quinn": 78, "Vladimir": 78,
    "Akshan": 84, "Ambessa": 86, "Annie": 83, "Aurora": 88, "Corki": 86, "Diana": 89,
    "Heimerdinger": 84, "Kassadin": 90, "Kayle": 89, "Neeko": 86, "Pantheon": 88,
    "Qiyana": 89, "Riven": 94, "Shyvana": 84, "Sona": 85, "Tahm Kench": 87, "Ziggs": 84,
    "Mel": 84, "Yunara": 86, "Zaahen": 88
}

def get_latest_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url)
    return response.json()[0] if response.status_code == 200 else "14.3.1"

def get_champions_data():
    version = get_latest_version()
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/tr_TR/champion.json"

    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()["data"]
    champions_list = []

    role_translator = {
        "Fighter": "Savaşçı", "Tank": "Tank", "Mage": "Büyücü",
        "Assassin": "Suikastçı", "Marksman": "Nişancı", "Support": "Destek"
    }

    for champ_id, champ_info in data.items():
        champ_name = champ_info["name"]

        # Şampiyon özel listede varsa o puanı alır, yoksa varsayılan 82 alır
        overall_score = CUSTOM_OVERALLS.get(
            champ_name,
            CUSTOM_OVERALLS.get(champ_id, 82)
        )

        primary_tag = champ_info["tags"][0] if "tags" in champ_info and len(champ_info["tags"]) > 0 else "Fighter"
        champ_key = champ_info["key"]

        champions_list.append({
            "id": champ_id,
            "name": champ_name,
            "class": role_translator.get(primary_tag, "Savaşçı"),
            "overall": overall_score,
            "portrait_url": f"https://cdn.communitydragon.org/latest/champion/{champ_key}/portrait"
        })

    return champions_list
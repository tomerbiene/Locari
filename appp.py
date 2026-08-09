import streamlit as st
# Oyun müziği (Streamlit yerleşik oynatıcı)
st.sidebar.audio("https://tomerbiene.github.io/Locari/audio/bgm.mp3", format="audio/mp3", autoplay=True, loop=True)
import base64
import os
import lol_data
import game_logic

# ========================================================
# BÖLGE VE SİNERJİ ANSİKLOPEDİSİ (EKSİKSİZ 160+ ULTIMATE SÜRÜM)
# ========================================================
CHAMPION_REGIONS = {
    # Zaun (Toksik Yeşil)
    "Jinx": "Zaun", "Vi": "Zaun", "Twitch": "Zaun", "Ekko": "Zaun",
    "Zac": "Zaun", "Dr. Mundo": "Zaun", "DrMundo": "Zaun", "Urgot": "Zaun",
    "Zeri": "Zaun", "Warwick": "Zaun", "Singed": "Zaun", "Renata Glasc": "Zaun",
    "Renata": "Zaun", "Viktor": "Zaun", "Blitzcrank": "Zaun", "Janna": "Zaun",

    # Piltover (Hextech Mavisi)
    "Caitlyn": "Piltover", "Ezreal": "Piltover", "Jayce": "Piltover",
    "Heimerdinger": "Piltover", "Orianna": "Piltover", "Camille": "Piltover",
    "Seraphine": "Piltover",

    # Ionia (Ruhani Pembe)
    "Yasuo": "Ionia", "Ahri": "Ionia", "Lillia": "Ionia", "Akali": "Ionia",
    "Irelia": "Ionia", "Karma": "Ionia", "Lee Sin": "Ionia", "LeeSin": "Ionia",
    "Zed": "Ionia", "Syndra": "Ionia", "Shen": "Ionia", "Kennen": "Ionia",
    "Jhin": "Ionia", "Kayn": "Ionia", "Master Yi": "Ionia", "MasterYi": "Ionia",
    "Wukong": "Ionia", "MonkeyKing": "Ionia", "Xayah": "Ionia", "Rakan": "Ionia",
    "Yone": "Ionia", "Varus": "Ionia", "Sett": "Ionia", "Ivern": "Ionia", "Hwei": "Ionia",

    # Noxus (Kan Kırmızı)
    "Darius": "Noxus", "Swain": "Noxus", "Samira": "Noxus", "Katarina": "Noxus",
    "Draven": "Noxus", "Sion": "Noxus", "Talon": "Noxus", "Kled": "Noxus",
    "LeBlanc": "Noxus", "Leblanc": "Noxus", "Riven": "Noxus", "Vladimir": "Noxus",
    "Cassiopeia": "Noxus", "Mordekaiser": "Noxus", "Briar": "Noxus",

    # Demacia (Altın Sarısı)
    "Garen": "Demacia", "Lux": "Demacia", "Sylas": "Demacia", "Fiora": "Demacia",
    "Jarvan IV": "Demacia", "JarvanIV": "Demacia", "Lucian": "Demacia",
    "Xin Zhao": "Demacia", "XinZhao": "Demacia", "Vayne": "Demacia", "Sona": "Demacia",
    "Quinn": "Demacia", "Galio": "Demacia", "Poppy": "Demacia", "Shyvana": "Demacia",
    "Kayle": "Demacia", "Morgana": "Demacia",

    # Bandle City (Büyülü Turuncu/Mor)
    "Teemo": "Bandle City", "Tristana": "Bandle City", "Lulu": "Bandle City",
    "Veigar": "Bandle City", "Corki": "Bandle City", "Yuumi": "Bandle City",
    "Gnar": "Bandle City", "Rumble": "Bandle City", "Fizz": "Bandle City", "Vex": "Bandle City",

    # Shadow Isles (Hayalet Yeşili)
    "Thresh": "Shadow Isles", "Viego": "Shadow Isles", "Hecarim": "Shadow Isles",
    "Gwen": "Shadow Isles", "Kalista": "Shadow Isles", "Karthus": "Shadow Isles",
    "Senna": "Shadow Isles", "Yorick": "Shadow Isles", "Maokai": "Shadow Isles",
    "Elise": "Shadow Isles",

    # Freljord (Buz Mavisi)
    "Ashe": "Freljord", "Sejuani": "Freljord", "Lissandra": "Freljord",
    "Braum": "Freljord", "Nunu & Willump": "Freljord", "Nunu": "Freljord",
    "NUNUVEWILLUMP": "Freljord", "Tryndamere": "Freljord", "Volibear": "Freljord",
    "Ornn": "Freljord", "Anivia": "Freljord", "Olaf": "Freljord", "Trundle": "Freljord",
    "Udyr": "Freljord", "Gragas": "Freljord",

    # Shurima (Kum Sarısı)
    "Azir": "Shurima", "Nasus": "Shurima", "Renekton": "Shurima",
    "Sivir": "Shurima", "Taliyah": "Shurima", "Xerath": "Shurima", "Amumu": "Shurima",
    "Akshan": "Shurima", "K'Sante": "Shurima", "KSante": "Shurima", "Rammus": "Shurima",
    "Naafiri": "Shurima",

    # Bilgewater (Okyanus Yeşili/Mavisi)
    "Miss Fortune": "Bilgewater", "MissFortune": "Bilgewater", "Gangplank": "Bilgewater",
    "Graves": "Bilgewater", "Twisted Fate": "Bilgewater", "TwistedFate": "Bilgewater",
    "Illaoi": "Bilgewater", "Pyke": "Bilgewater", "Tahm Kench": "Bilgewater",
    "TahmKench": "Bilgewater", "Nilah": "Bilgewater", "Nautilus": "Bilgewater",

    # Targon (Kozmik Mor)
    "Leona": "Targon", "Diana": "Targon", "Pantheon": "Targon",
    "Zoe": "Targon", "Taric": "Targon", "Aphelios": "Targon", "Soraka": "Targon",
    "Aurelion Sol": "Targon", "AurelionSol": "Targon",

    # The Void / Hiçlik (Derin Mor)
    "Kai'Sa": "The Void", "Kaisa": "The Void", "Kog'Maw": "The Void", "KogMaw": "The Void",
    "Kha'Zix": "The Void", "Khazix": "The Void", "Cho'Gath": "The Void", "Chogath": "The Void",
    "Bel'Veth": "The Void", "Belveth": "The Void", "Vel'Koz": "The Void", "Velkoz": "The Void",
    "Kassadin": "The Void", "Malzahar": "The Void", "Rek'Sai": "The Void", "RekSai": "The Void",

    # Ixtal (Element Ormanı - Zümrüt Yeşili)
    "Qiyana": "Ixtal", "Rengar": "Ixtal", "Nidalee": "Ixtal",
    "Neeko": "Ixtal", "Malphite": "Ixtal", "Zyra": "Ixtal", "Milio": "Ixtal",

    # Runeterra / Gezginler (Parlak Gümüş)
    "Ryze": "Runeterra", "Jax": "Runeterra", "Aatrox": "Runeterra",
    "Bard": "Runeterra", "Fiddlesticks": "Runeterra", "Shaco": "Runeterra",
    "Kindred": "Runeterra", "Alistar": "Runeterra", "Brand": "Runeterra",
    "Evelynn": "Runeterra", "Nocturne": "Runeterra", "Smolder": "Runeterra"
}


# Yan yana duran iki kartın sinerjisini kontrol eden beyin fonksiyonu
def check_synergy(card1_name, card2_name):
    # Eğer kartlardan biri yoksa veya isimleri sözlükte tanımlı değilse boş dön
    region1 = CHAMPION_REGIONS.get(card1_name)
    region2 = CHAMPION_REGIONS.get(card2_name)

    # İki kartın da bölgesi varsa ve birbiriyle aynıysa, bölge adını ateşle!
    if region1 and region2 and region1 == region2:
        return region1
    return None


def get_synergy_svg(region_name):
    synergy_colors = {
        "Zaun": "#39ff14", "Piltover": "#0ac8b9", "Ionia": "#ff66cc",
        "Noxus": "#ff0000", "Demacia": "#ffd700", "Bandle City": "#ff8c00",
        "Shadow Isles": "#00ff7f", "Freljord": "#00bfff", "Shurima": "#f4a460",
        "Bilgewater": "#20b2aa", "Targon": "#8a2be2", "The Void": "#9932cc",
        "Ixtal": "#50c878", "Runeterra": "#e0e0e0"
    }
    color = synergy_colors.get(region_name, "#ffffff")

    # height değerini % yerine "180px" olarak sabitliyoruz ki sistem bunu sıfıra indirmesin!
    return f"""<div style="position: absolute; top: 15%; right: -55%; width: 110%; height: 180px; z-index: 0; pointer-events: none;">
<svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none" style="overflow: visible;">
<path d="M0,15 C35,-5 65,35 100,15" fill="none" stroke="{color}" stroke-width="1.5" stroke-dasharray="6 4" opacity="0.6" style="filter: drop-shadow(0 0 4px {color}); animation: flowEnergyFast 1s linear infinite;" />
<path d="M0,50 C35,30 65,70 100,50" fill="none" stroke="{color}" stroke-width="3.5" stroke-dasharray="15 10" style="filter: drop-shadow(0 0 12px {color}); animation: flowEnergy 1.5s linear infinite;" />
<path d="M0,85 C35,65 65,105 100,85" fill="none" stroke="{color}" stroke-width="1.5" stroke-dasharray="8 6" opacity="0.6" style="filter: drop-shadow(0 0 4px {color}); animation: flowEnergySlow 2s linear infinite;" />
</svg>
<style>
@keyframes flowEnergyFast {{ to {{ stroke-dashoffset: -40; }} }}
@keyframes flowEnergy {{ to {{ stroke-dashoffset: -50; }} }}
@keyframes flowEnergySlow {{ to {{ stroke-dashoffset: -30; }} }}
</style>
</div>"""


# ---------------------------------------------------------
# 1. YARDIMCI FONKSİYONLAR VE KART ARKASI
# ---------------------------------------------------------
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""


img_base64 = get_base64_of_bin_file('card_back.png')

# --- Turnuva Sistemi (3 Aşama) ---
TOURNAMENT_STAGES = {
    1: {"title": "STAGE 1: ENTERING THE RIFT", "bot": "ZED (Shadow Master)", "diff": "easy", "splash": "Zed"},
    2: {"title": "STAGE 2: PATH OF CHAMPIONS", "bot": "SWAIN (The Grand General)", "diff": "medium", "splash": "Swain"},
    3: {"title": "STAGE 3: THE APEX SHOWDOWN", "bot": "AATROX (The World Ender)", "diff": "hard", "splash": "Aatrox"}
}


def get_safe_name(name):
    name = str(name).strip()
    name_lower = name.lower()
    if "nunu" in name_lower:
        return "Nunu"
    exceptions = {
        "aurelion sol": "AurelionSol", "bel'veth": "Belveth", "cho'gath": "Chogath",
        "dr. mundo": "DrMundo", "jarvan iv": "JarvanIV", "k'sante": "KSante",
        "kai'sa": "Kaisa", "kha'zix": "Khazix", "kog'maw": "KogMaw",
        "leblanc": "Leblanc", "lee sin": "LeeSin", "master yi": "MasterYi",
        "miss fortune": "MissFortune", "nunu & willump": "Nunu", "nunu": "Nunu",
        "nunuvewillump": "Nunu", "rek'sai": "RekSai", "renata glasc": "Renata",
        "tahm kench": "TahmKench", "twisted fate": "TwistedFate", "vel'koz": "Velkoz",
        "wukong": "MonkeyKing", "xin zhao": "XinZhao", "NUNUVEWILLUMP": "Nunu"
    }
    if name_lower in exceptions:
        return exceptions[name_lower]
    clean = name.replace("'", "").replace(" ", "").replace(".", "")
    return clean.capitalize()


def get_splash_url(champ_name):
    clean_name = get_safe_name(champ_name)
    return f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{clean_name}_0.jpg"


def play_champion_voice(champ_name):
    if not os.path.exists("audio"):
        return

    # Hedef şampiyonun adını tertemiz yapıyoruz
    target_name = get_safe_name(champ_name).replace("'", "").replace(" ", "").lower()
    found_file = None

    for file in os.listdir("audio"):
        # Dosyanın uzantısını (.mp3) ve ismini ayırıyoruz
        name_part, ext = os.path.splitext(file)

        # Eğer uzantı geçerli bir ses dosyası değilse hiç uğraşmadan atla
        if ext.lower() not in ['.mp3', '.wav', '.ogg']:
            continue

        # Sadece dosya ismini (mp3'süz halini) tertemiz yapıyoruz
        file_clean = name_part.replace("'", "").replace(" ", "").lower()

        # TAM EŞLEŞME: Viego ve Vi artık birbirine karışamaz!
        if file_clean == target_name:
            found_file = os.path.join("audio", file)
            break

    if found_file:
        with open(found_file, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        audio_html = f"""
            <audio autoplay style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)


# --- Sayfa Yapılandırması ---
st.set_page_config(page_title="Locari: League of Cards", layout="wide", initial_sidebar_state="collapsed")

# ---------------------------------------------------------
# 2. CSS STİLLERİ (Premium 3D Tasarım)
# ---------------------------------------------------------
st.markdown(f"""
    <style>
    .empty-slot {{ 
        width: 110px; height: 170px; margin: 0 auto;
        border: 2px solid #1f2c45; border-radius: 6px; 
        background: linear-gradient(180deg, #0a0f18 0%, #121a28 100%);
        box-shadow: inset 0px 10px 20px rgba(0, 0, 0, 0.8), 0 1px 3px rgba(255, 255, 255, 0.05);
        display: flex; align-items: center; justify-content: center; 
    }}
    .empty-slot span {{ color: #4b6287 !important; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; font-size: 11px; }}

    @keyframes slideInFromTop {{ 0% {{ transform: translateY(-100px) scale(0.8); opacity: 0; }} 100% {{ transform: translateY(0) scale(1); opacity: 1; }} }}
    @keyframes slideInFromBottom {{ 0% {{ transform: translateY(100px) scale(0.8); opacity: 0; }} 100% {{ transform: translateY(0) scale(1); opacity: 1; }} }}
    .deal-bot-card {{ animation: slideInFromTop 0.8s ease-out forwards; opacity: 0; }}
    .deal-player-card {{ animation: slideInFromBottom 0.8s ease-out forwards; opacity: 0; }}
    .deck-stack, .score-stack {{ 
        width: 100px; height: 180px; margin: 0 auto; 
        background-color: transparent !important; 
        background-image: url("data:image/png;base64,{img_base64}") !important; 
        background-size: cover; background-position: center; background-repeat: no-repeat; 
        border-radius: 8px; border: none !important; 
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.75), inset 0 1px 0 rgba(255,255,255,0.15); 
        display: flex; align-items: center; justify-content: center; 
    }}

    @keyframes pulse-gold {{ 0% {{ box-shadow: 0 0 10px #ffd700; }} 50% {{ box-shadow: 0 0 25px #ffd700, 0 0 10px rgba(255, 215, 0, 0.5) inset; }} 100% {{ box-shadow: 0 0 10px #ffd700; }} }}
    @keyframes pulse-epic {{ 0% {{ box-shadow: 0 0 8px #0ac8b9; }} 50% {{ box-shadow: 0 0 20px #0ac8b9, 0 0 8px rgba(10, 200, 185, 0.5) inset; }} 100% {{ box-shadow: 0 0 8px #0ac8b9; }} }}
    @keyframes text-shine {{ to {{ background-position: 200% center; }} }}

    header[data-testid="stHeader"] {{ display: none !important; }}
    footer {{ display: none !important; }}
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="ScrollToBottomContainer"] {{ overflow-y: auto !important; min-height: 100vh; }}
    .stApp {{ 
        background-color: #121926 !important; 
        background-image: radial-gradient(circle at 50% 45%, rgba(50, 75, 110, 0.45) 0%, transparent 65%), radial-gradient(circle at 50% 100%, rgba(200, 170, 110, 0.08) 0%, transparent 70%), url("data:image/svg+xml,%3Csvg width='60' height='103.92' viewBox='0 0 60 103.92' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='%230ac8b9' stroke-width='1' stroke-opacity='0.05'%3E%3Cpath d='M30 17.32L0 34.64v34.64l30 17.32 30-17.32V34.64L30 17.32z'/%3E%3Cpath d='M0 86.6l30 17.32 30-17.32V69.28L30 51.96 0 69.28v17.32z'/%3E%3Cpath d='M30 0l30 17.32v17.32L30 17.32 0 34.64V17.32L30 0z'/%3E%3C/g%3E%3C/svg%3E");
        background-attachment: fixed; color: #f0e6d2; 
    }}

    .block-container {{ max-width: 1300px !important; padding-top: 0rem !important; padding-bottom: 0rem !important; margin: 0 auto; }}
    div[data-testid="stVerticalBlock"] {{ gap: 0.4rem; }}
    div[data-testid="column"] {{ position: relative; }} 

    .locari-title {{ text-align: center; font-size: 3rem; font-weight: 900; background: -webkit-linear-gradient(45deg, #c8aa6e, #f0e6d2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px; padding-bottom: 0px; text-transform: uppercase; letter-spacing: 2px; }}
    .locari-subtitle {{ text-align: center; color: #c8aa6e; font-size: 1.1rem; font-weight: bold; margin-top: -10px; margin-bottom: 20px; letter-spacing: 5px; opacity: 0.9; }}

    .banner {{ text-align: center; font-weight: 900; font-size: 1rem; padding: 10px; margin: 10px 0; border-radius: 4px; letter-spacing: 1px; text-transform: uppercase; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }}
    .banner-win {{ background: linear-gradient(90deg, transparent, rgba(46, 125, 50, 0.9), transparent); color: #fff; border-top: 2px solid #81c784; border-bottom: 2px solid #81c784; }}
    .banner-lose {{ background: linear-gradient(90deg, transparent, rgba(198, 40, 40, 0.9), transparent); color: #fff; border-top: 2px solid #e57373; border-bottom: 2px solid #e57373; }}
    .banner-draw {{ background: linear-gradient(90deg, transparent, rgba(85, 85, 85, 0.9), transparent); color: #fff; border-top: 2px solid #aaa; border-bottom: 2px solid #aaa; }}
    .banner-info {{ background: linear-gradient(90deg, transparent, rgba(200, 170, 110, 0.9), transparent); color: #000; border-top: 2px solid #f0e6d2; border-bottom: 2px solid #f0e6d2; }}

    .red-side-line {{ border-bottom: 2px solid #e57373; margin: 10px 0; box-shadow: 0 2px 10px rgba(229, 115, 115, 0.4); }}
    .blue-side-line {{ border-top: 2px solid #64b5f6; margin: 10px 0; box-shadow: 0 -2px 10px rgba(100, 181, 246, 0.4); }}

    

    /* 4. BOT KARTLARI (Kullanıcıyla Birebir Aynı Boyut, Sadece Geriye İtilmiş) */
    .bot-hidden {{ 
        width: 110px;  
        height: 170px; 
        margin: -65px auto 0 auto; /* Senin bulduğun o mükemmel hiza! */
        position: relative; 
        z-index: 10 !important; /* SİHİR BURADA: Kartlar artık EN ÖNDE */
        background-color: transparent !important; 
        background-image: url("data:image/png;base64,{img_base64}") !important; 
        background-size: cover; 
        background-position: center; 
        background-repeat: no-repeat; 
        border-radius: 8px; 
        border: none !important; 
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.75), inset 0 1px 0 rgba(255,255,255,0.15); 
        clip-path: inset(45px 0 0 0);
    }}

    div.element-container:has(span[id^="card-btn-"]) + div.element-container button, div[data-testid="stElementContainer"]:has(span[id^="card-btn-"]) + div[data-testid="stElementContainer"] button {{ background: transparent !important; color: transparent !important; border: none !important; box-shadow: none !important; width: 110px !important; height: 195px !important; position: absolute !important; margin-top: -193px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 99 !important; cursor: pointer !important; }}
    div.element-container:has(span[id^="card-btn-"]) + div.element-container button:hover, div[data-testid="stElementContainer"]:has(span[id^="card-btn-"]) + div[data-testid="stElementContainer"] button:hover {{ background: rgba(255, 255, 255, 0.1) !important; border: 2px solid rgba(255, 215, 0, 0.4) !important; border-radius: 6px !important; }}
    /* ========================================= */
    /* HEXTECH VIP KART TEPSİSİ TASARIMI         */
    /* ========================================= */
    .hextech-dock {{
        position: absolute;
        top: -30px;
        left: 50%;
        transform: translateX(-50%);
        width: 95vw;
        max-width: 1200px;
        height: 320px; /* SİHİRLİ DOKUNUŞ: 330px olan değeri 250px yaptık */
        background: 
            radial-gradient(circle at 50% 110%, rgba(10, 200, 185, 0.25) 0%, transparent 60%),
            linear-gradient(180deg, rgba(12, 18, 28, 0.85) 0%, rgba(5, 8, 12, 0.98) 100%);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px 20px 0 0;
        border-top: 2px solid rgba(200, 170, 110, 0.85);
        border-left: 1px solid rgba(10, 200, 185, 0.4);
        border-right: 1px solid rgba(10, 200, 185, 0.4);
        box-shadow: 0 -15px 40px rgba(10, 200, 185, 0.15), inset 0 10px 30px rgba(200, 170, 110, 0.1);
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }}

    /* Tepsinin içindeki fütüristik grid (ızgara) deseni */
    .hextech-dock::after {{
        content: '';
        position: absolute;
        inset: 0;
        background-image: 
            linear-gradient(rgba(10, 200, 185, 0.07) 1px, transparent 1px),
            linear-gradient(90deg, rgba(10, 200, 185, 0.07) 1px, transparent 1px);
        background-size: 25px 25px;
        /* Sadece üst kısımlarda görünen, aşağı doğru kaybolan desen efekti */
        -webkit-mask-image: linear-gradient(180deg, rgba(0,0,0,1) 0%, transparent 70%);
        mask-image: linear-gradient(180deg, rgba(0,0,0,1) 0%, transparent 70%);
    }}

    /* Tepe merkezdeki yoğun parlayan altın çekirdek çizgisi */
    .hextech-core {{
        position: absolute;
        top: -2px;
        left: 50%;
        transform: translateX(-50%);
        width: 35%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #ffd700, #fff, #ffd700, transparent);
        box-shadow: 0 0 25px #ffd700, 0 0 10px #c8aa6e;
        z-index: 1;
    }}
    /* ========================================= */
    /* DÜŞMAN (RAKİP) KART TEPSİSİ TASARIMI      */
    /* ========================================= */
    /* DÜŞMAN TEPSİSİ (Yukarı çekilerek kartların üstten fırlamasını engeller) */
    .enemy-dock {{
        position: absolute;
        top: -10px; 
        left: 50%;
        transform: translateX(-50%);
        width: 95vw;
        max-width: 1200px;
        height: 140px; 
        background: 
            radial-gradient(circle at 50% -10%, rgba(229, 115, 115, 0.15) 0%, transparent 60%),
            linear-gradient(0deg, rgba(20, 10, 10, 0.85) 0%, rgba(10, 5, 5, 0.95) 100%);
        backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
        border-radius: 0 0 24px 24px; 
        border-bottom: 2px solid rgba(229, 115, 115, 0.7);
        border-left: 1px solid rgba(229, 115, 115, 0.2); border-right: 1px solid rgba(229, 115, 115, 0.2);
        box-shadow: 0 15px 40px rgba(229, 115, 115, 0.1), inset 0 -10px 30px rgba(229, 115, 115, 0.05);
        pointer-events: none; overflow: hidden; 
        z-index: 0 !important; /* SİHİR BURADA: Tepsi artık arkada */
    }}

    /* Düşman tepsisine özel kırmızı grid ızgarası */
    .enemy-dock::after {{
        content: '';
        position: absolute;
        inset: 0;
        background-image: 
            linear-gradient(rgba(229, 115, 115, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(229, 115, 115, 0.05) 1px, transparent 1px);
        background-size: 25px 25px;
        /* Maske efekti bu sefer aşağıdan yukarıya doğru siliniyor */
        -webkit-mask-image: linear-gradient(0deg, rgba(0,0,0,1) 0%, transparent 70%);
        mask-image: linear-gradient(0deg, rgba(0,0,0,1) 0%, transparent 70%);
    }}

    /* Çekirdek ışık hüzmesi (Alt sınırın ortasında kıpkırmızı parlıyor) */
    .enemy-core {{
        position: absolute;
        bottom: -2px; /* Çizgi bu sefer en altta */
        left: 50%;
        transform: translateX(-50%);
        width: 35%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #ff4b4b, #ffcccc, #ff4b4b, transparent);
        box-shadow: 0 0 25px #ff4b4b, 0 0 10px #e57373;
        z-index: 1;
    }}
    /* ========================================= */
    /* KUSURSUZ SEÇİM EFEKTİ (İLK SEFERKİ YÜKSEKLİK) */
    /* ========================================= */

    /* 1. Kartı tam o sevdiğin seviyeye kaldır ve parlat */
    .selected-card {{
        transform: translateY(-20px) scale(1.05) !important;
        box-shadow: 0 15px 35px rgba(10, 200, 185, 0.6), inset 0 0 15px rgba(10, 200, 185, 0.4) !important;
        border: 2px solid #0ac8b9 !important;
        transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        /* Kartın z-index'i 1: Diğer kartların üstünde ama butonun altında kalacak */
        z-index: 1 !important; 
    }}

    /* 2. Oyun İçindeki Gizli Tıklama Butonlarını En Üst Katmana Çek (Tıklama Asla Bozulmaz) */
    div.stButton {{
        z-index: 99 !important;
        position: relative; 
    }}

    /* 3. Tıklama Anındaki O Çirkin Sarı Çerçeveyi (Focus Ring) Oyundan Komple Sil */
    div.stButton > button:focus, 
    div.stButton > button:active {{
        box-shadow: none !important;
        outline: none !important;
        border-color: transparent !important;
    }}

    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# OYUN MANTIĞI VE YÖNETİMİ
# ---------------------------------------------------------
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.tour_stage = 1
if "synergy_charges" not in st.session_state:
    st.session_state.synergy_charges = 0


def init_game(is_next_stage=False):
    with st.spinner("Setting up the Arena..."):
        champs = lol_data.get_champions_data()
        if not champs: return
        if not is_next_stage:
            st.session_state.tour_stage = 1
        stage_info = TOURNAMENT_STAGES[st.session_state.tour_stage]
        st.session_state.opponent_name = stage_info["bot"]
        st.session_state.bot_difficulty = stage_info["diff"]
        st.session_state.stage_title = stage_info["title"]
        st.session_state.p_deck, st.session_state.b_deck = game_logic.initialize_game(champs, total_cards=50)
        st.session_state.p_set_wins = 0
        st.session_state.b_set_wins = 0
        st.session_state.current_set = 1
        st.session_state.synergy_charges = 0
        start_new_set()
        st.session_state.game_started = True


def start_new_set():
    st.session_state.p_played_cards = []
    st.session_state.p_deck, st.session_state.p_hand = game_logic.draw_cards(st.session_state.p_deck, target_size=5)
    st.session_state.b_deck, st.session_state.b_hand = game_logic.draw_cards(st.session_state.b_deck, target_size=5)
    st.session_state.p_round_score = 0
    st.session_state.b_round_score = 0
    st.session_state.turn = "player"
    st.session_state.phase = "player_attack"
    st.session_state.arena_p_card = st.session_state.arena_b_card = None
    st.session_state.combat_log = f"SET {st.session_state.current_set} STARTED"
    st.session_state.turn_count = 0
    if "selected_card_idx" not in st.session_state:
        st.session_state.selected_card_idx = None


def evaluate_set_end():
    if st.session_state.p_round_score > st.session_state.b_round_score:
        st.session_state.p_set_wins += 1
        st.session_state.combat_log = f"SET {st.session_state.current_set} WON!"
    elif st.session_state.b_round_score > st.session_state.p_round_score:
        st.session_state.b_set_wins += 1
        st.session_state.combat_log = f"SET {st.session_state.current_set} LOST!"
    else:
        st.session_state.combat_log = f"SET {st.session_state.current_set} DRAW!"
    st.session_state.phase = "set_end"
    if st.session_state.p_set_wins == 3 or st.session_state.b_set_wins == 3 or st.session_state.current_set == 5:
        st.session_state.phase = "game_over"


def handle_card_click(clicked_idx):
    # DURUM 1: Hiçbir kart seçili değilse -> Tıklananı havaya kaldır (Seç)
    if st.session_state.selected_card_idx is None:
        st.session_state.selected_card_idx = clicked_idx

    # DURUM 2: Seçili karta BİR DAHA tıklandıysa -> Kartı sahaya at (Oyna)
    elif st.session_state.selected_card_idx == clicked_idx:
        # Eski kart oynama fonksiyonunu buraya bağlayacağız (Örn: play_card(clicked_idx))
        st.session_state.selected_card_idx = None  # Oynadıktan sonra hafızayı temizle

    # DURUM 3: Başka bir karta tıklandıysa -> İki kartı YER DEĞİŞTİR (Swap)
    else:
        prev_idx = st.session_state.selected_card_idx

        # Listedeki iki kartın yerini pürüzsüzce takas et
        st.session_state.p_hand[prev_idx], st.session_state.p_hand[clicked_idx] = \
            st.session_state.p_hand[clicked_idx], st.session_state.p_hand[prev_idx]

        # Yer değiştirme işlemi bitince seçimi sıfırla ki yenisini seçebil
        st.session_state.selected_card_idx = None


def handle_combat(card_idx, is_player_attacking):
    p_card = st.session_state.p_hand.pop(card_idx)
    if 'p_played_cards' not in st.session_state: st.session_state.p_played_cards = []
    st.session_state.p_played_cards.append(p_card)

    if is_player_attacking:
        b_card = game_logic.bot_choose_card(st.session_state.b_hand, player_card=p_card,
                                            difficulty=st.session_state.get('bot_difficulty', 'medium'))
        st.session_state.b_hand.remove(b_card)
    else:
        b_card = st.session_state.arena_b_card

    st.session_state.arena_p_card = p_card
    st.session_state.arena_b_card = b_card
    winner, p_val, b_val, _, _ = game_logic.evaluate_round(p_card, b_card)

    if winner == "player":
        st.session_state.p_round_score += 1
        st.session_state.combat_log = f"ROUND WON! ({int(p_val)} vs {int(b_val)})"
        st.session_state.turn = "player"
    elif winner == "bot":
        st.session_state.b_round_score += 1
        st.session_state.combat_log = f"ROUND LOST! ({int(p_val)} vs {int(b_val)})"
        st.session_state.turn = "bot"
    else:
        st.session_state.combat_log = f"DRAW! ({int(p_val)} vs {int(b_val)})"

    st.session_state.turn_count += 1
    st.session_state.phase = "resolve"


def next_round():
    if len(st.session_state.p_hand) == 0:
        evaluate_set_end()
    else:
        st.session_state.phase = "player_attack" if st.session_state.turn == "player" else "bot_attack_prep"


def start_next_set_action():
    st.session_state.p_played_cards = []
    st.session_state.current_set += 1
    start_new_set()


# ---------------------------------------------------------
# GÖRSEL ÇİZİM FONKSİYONLARI
# ---------------------------------------------------------
def render_view_card(card, is_arena=False, anim_class="", delay=0):
    is_mythic = card['overall'] >= 95
    is_epic = 90 <= card['overall'] < 95
    safe_name = get_safe_name(card['name'])
    b_color = "#ffd700" if is_mythic else ("#0ac8b9" if is_epic else "#c8aa6e")
    b_shadow = "0 0 20px #ffd700" if is_mythic else ("0 0 15px #0ac8b9" if is_epic else "0 0 0 transparent")
    anim = "pulse-gold 2s infinite" if is_mythic else ("pulse-epic 3s infinite" if is_epic else "none")
    badge_bg = "linear-gradient(135deg, #ffd700, #ff8c00)" if is_mythic else (
        "linear-gradient(135deg, #0ac8b9, #067a71)" if is_epic else "linear-gradient(135deg, #c8aa6e, #7a5c29)")
    badge_color = "#000" if is_mythic else "#fff"
    np_bg = "linear-gradient(90deg, #b8860b, #ffd700, #b8860b)" if is_mythic else (
        "linear-gradient(90deg, #067a71, #0ac8b9, #067a71)" if is_epic else "#010a13")
    np_color = "#000" if is_mythic else ("#fff" if is_epic else "#f0e6d2")
    np_anim = "text-shine 2s linear infinite" if (is_mythic or is_epic) else "none"

    # SABİT KUTU HİLESİ: is_arena ise kartı 230 piksellik kilitli bir çerçevenin içine alıyoruz
    wrapper_style = "position: relative; width: 110px; height: 230px; margin: 0 auto; display: flex; flex-direction: column; justify-content: center;" if is_arena else "position: relative; width: 110px; margin: 0 auto;"

    html = f"""
    <div class="{anim_class}" style="{wrapper_style} animation-delay: {delay}s;">
        <div style="position: relative; width: 110px;">
            <div style="position: absolute; z-index: 10; top: 2px; left: 2px; background: {badge_bg}; color: {badge_color}; font-weight: 900; font-size: 11px; padding: 2px 5px; border-radius: 8px; border: 1px solid #fff;">{card['overall']}</div>
            <div style="width: 110px; height: 170px; border: 2px solid {b_color}; border-bottom: none; border-radius: 6px 6px 0 0; box-shadow: 0 2px 2px rgba(0,0,0,0.35), 0 10px 18px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.25), {b_shadow}; animation: {anim}; position: relative; overflow: hidden;">
                <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{safe_name}_0.jpg" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
                <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.22) 0%, rgba(255,255,255,0.04) 30%, transparent 55%, rgba(0,0,0,0.3) 100%); pointer-events: none;"></div>
            </div>
            <div style="background: {np_bg}; color: {np_color}; text-align: center; font-weight: 900; font-size: 10px; padding: 4px 0; border: 2px solid {b_color}; border-top: none; border-radius: 0 0 6px 6px; text-transform: uppercase; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; background-size: 200% auto; animation: {np_anim}; box-shadow: 0 4px 6px rgba(0,0,0,0.4);">{safe_name}</div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_empty_slot(text="BOŞ YUVA", is_arena=False):
    # SABİT KUTU HİLESİ: Gerçek kartla milimetrik aynı boyutta (230px) kilitli çerçeve
    wrapper_style = "width: 110px; height: 230px; margin: 0 auto; display: flex; flex-direction: column; justify-content: center;" if is_arena else "width: 110px; margin: 0 auto;"

    html = f"""
    <div style="{wrapper_style}">
        <div class="empty-slot"><span>{text}</span></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_playable_card(card, card_idx, action_type, anim_class="", delay=0):
    # 1. GÖRSEL DOKUNUŞ: Eğer bu kart o an seçiliyse, CSS sınıfına parlama efektini ekle
    if st.session_state.get("selected_card_idx") == card_idx:
        anim_class += " selected-card"

    # Kartı ekrana çiz (seçiliyse bizim CSS sınıfıyla birlikte havaya kalkacak)
    render_view_card(card, is_arena=False, anim_class=anim_class, delay=delay)

    st.markdown(f'<span id="card-btn-{card_idx}"></span>', unsafe_allow_html=True)

    # 2. MEKANİK DOKUNUŞ: Butona tıklandığında ne olacak?
    if st.button(" ", key=f"act_{st.session_state.current_set}_{st.session_state.turn_count}_{card_idx}",
                 use_container_width=True):

        # DURUM 1: Hiçbir kart seçili değilse -> Bu kartı HAVAYA KALDIR (Seç)
        if st.session_state.get("selected_card_idx") is None:
            st.session_state.selected_card_idx = card_idx

        # DURUM 2: Seçili karta TEKRAR tıklandıysa -> SAHAYA AT (Oyna)
        elif st.session_state.selected_card_idx == card_idx:
            # --- YENİ: SİNERJİ ŞARJ KONTROLÜ ---
            is_synergized = False
            curr_name = st.session_state.p_hand[card_idx].get("name")

            # Solundaki kartla neon bağı var mı?
            if card_idx > 0:
                if check_synergy(curr_name, st.session_state.p_hand[card_idx - 1].get("name")):
                    is_synergized = True

            # Sağındaki kartla neon bağı var mı?
            if card_idx < len(st.session_state.p_hand) - 1:
                if check_synergy(curr_name, st.session_state.p_hand[card_idx + 1].get("name")):
                    is_synergized = True

            # Sinerjili kart sahaya sürüldüyse Ulti Barını doldur (Maks 3)
            if is_synergized:
                st.session_state.synergy_charges = min(3, st.session_state.get("synergy_charges", 0) + 1)
            # -----------------------------------

            st.session_state.selected_card_idx = None
            handle_combat(card_idx, action_type == "player_attack")

        # DURUM 3: Başka bir kart seçiliyken BUNA tıklandıysa -> YER DEĞİŞTİR (Swap)
        else:
            prev_idx = st.session_state.selected_card_idx

            # İki kartın listedeki indekslerini birbiriyle takas et
            st.session_state.p_hand[prev_idx], st.session_state.p_hand[card_idx] = \
                st.session_state.p_hand[card_idx], st.session_state.p_hand[prev_idx]

            # Yer değiştirme bitince havada kart kalmasın diye hafızayı sıfırla
            st.session_state.selected_card_idx = None

        # Ekranın güncellenmesi için sayfayı yenile
        st.rerun()


def render_empty_slot(text="BOŞ YUVA", is_arena=False):
    wrapper_style = "width: 110px; margin: 5px auto;" if is_arena else "width: 110px; margin: 0 auto;"
    html = f"""
    <div style="{wrapper_style}">
        <div class="empty-slot"><span>{text}</span></div>
        <div style="height: 22px;"></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


# ---------------------------------------------------------
# ANA EKRAN / SAYFA AKIŞI
# ---------------------------------------------------------
if not st.session_state.game_started:
    st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 50vw; height: 100vh; z-index: 0; pointer-events: none; background-image: url('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aphelios_0.jpg'); background-size: cover; background-position: center right; opacity: 0.45; -webkit-mask-image: -webkit-linear-gradient(left, rgba(0,0,0,1) 40%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(to right, rgba(0,0,0,1) 40%, rgba(0,0,0,0) 100%);"></div>
        <div style="position: fixed; top: 0; right: 0; width: 60vw; height: 100vh; z-index: 0; pointer-events: none; background-image: url('https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lucian_25.jpg'); background-size: cover; background-position: center ; opacity: 0.45; -webkit-mask-image: -webkit-linear-gradient(right, rgba(0,0,0,1) 40%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(to left, rgba(0,0,0,1) 40%, rgba(0,0,0,0) 100%);"></div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><div style='position: relative; z-index: 1;'>", unsafe_allow_html=True)
    st.markdown(
        "<h1 class='locari-title' style='text-shadow: 0 0 20px rgba(200, 170, 110, 0.6); margin-top: 20px;'>LOCARI</h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<div class='locari-subtitle' style='text-shadow: 0 0 10px rgba(200, 170, 110, 0.4);'>LOL CARD BATTLE</div>",
        unsafe_allow_html=True)

    html_rozetler = (
        "<div style='display: flex; justify-content: center; gap: 20px; max-width: 850px; margin: 40px auto; position: relative; z-index: 1;'>"

        # 1. KART: BO5 FORMAT (Aynen korundu - Camgöbeği)
        "<div style='flex: 1; background: rgba(15, 22, 35, 0.55); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(10, 200, 185, 0.3); border-top: 2px solid #0ac8b9; border-radius: 12px; padding: 25px 15px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), inset 0 2px 10px rgba(10, 200, 185, 0.1); text-align: center;'>"
        "<div style='font-size: 26px; margin-bottom: 12px; text-shadow: 0 0 15px rgba(10,200,185,0.9);'>⚔️</div>"
        "<div style='color: #0ac8b9; font-weight: 900; font-size: 14px; letter-spacing: 1px; margin-bottom: 10px;'>BO5 FORMAT</div>"
        "<div style='color: #c8aa6e; font-size: 12px; opacity: 0.9; line-height: 1.5;'>Played over 5 sets.<br>First to win 3 sets becomes the Champion.</div>"
        "</div>"

        # 2. KART: OVERALL POWER (Ortaya alındı - Yukarı kalkık efekt korundu - Altın Sarısı)
        "<div style='flex: 1; background: rgba(15, 22, 35, 0.55); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255, 215, 0, 0.3); border-top: 2px solid #ffd700; border-radius: 12px; padding: 25px 15px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), inset 0 2px 10px rgba(255, 215, 0, 0.1); text-align: center; transform: translateY(-15px);'>"
        "<div style='font-size: 26px; margin-bottom: 12px; text-shadow: 0 0 15px rgba(255,215,0,0.9);'>👑</div>"
        "<div style='color: #ffd700; font-weight: 900; font-size: 14px; letter-spacing: 1px; margin-bottom: 10px;'>OVERALL POWER</div>"
        "<div style='color: #c8aa6e; font-size: 12px; opacity: 0.9; line-height: 1.5;'>Card power (Overall) determines the round.<br>Don't waste your Mythic cards.</div>"
        "</div>"

        # 3. KART: REGIONAL SYNERGY (Yeni eklendi - Mistik Mor / Hextech)
        "<div style='flex: 1; background: rgba(15, 22, 35, 0.55); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(179, 102, 255, 0.3); border-top: 2px solid #b366ff; border-radius: 12px; padding: 25px 15px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), inset 0 2px 10px rgba(179, 102, 255, 0.1); text-align: center;'>"
        "<div style='font-size: 26px; margin-bottom: 12px; text-shadow: 0 0 15px rgba(179,102,255,0.9);'>💠</div>"
        "<div style='color: #b366ff; font-weight: 900; font-size: 14px; letter-spacing: 1px; margin-bottom: 10px;'>REGIONAL SYNERGY</div>"
        "<div style='color: #c8aa6e; font-size: 12px; opacity: 0.9; line-height: 1.5;'>Match champions from the same region to charge the crystal.<br>Reach 3 charges to reroll any card.</div>"
        "</div>"

        "</div>"
    )
    st.markdown(html_rozetler, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.2, 1, 1.2])
    with c2:
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        if st.button("DRAW CARDS & START MATCH", type="primary", use_container_width=True):
            init_game()
            st.rerun()

    st.markdown("""
    <div style='text-align: center; margin-top: 60px; margin-bottom: 20px; font-size: 11px; color: rgba(240, 230, 210, 0.4); max-width: 750px; margin-left: auto; margin-right: auto; line-height: 1.6; letter-spacing: 0.5px;'>
        <i>Locari: League of Cards</i> was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games. Riot Games does not endorse or sponsor this project.<br>
        League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
    </div>
    """, unsafe_allow_html=True)

else:
    if st.session_state.phase == "resolve" and st.session_state.arena_p_card and st.session_state.arena_b_card:
        p_splash = get_splash_url(st.session_state.arena_p_card['name'])
        b_splash = get_splash_url(st.session_state.arena_b_card['name'])
        st.markdown(f"""
            <div style="position: fixed; top: 0; left: 0; width: 55vw; height: 100vh; z-index: 0; pointer-events: none; background-image: url('{p_splash}'); background-size: cover; background-position: center; opacity: 0.35; -webkit-mask-image: linear-gradient(to right, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(to right, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 100%);"></div>
            <div style="position: fixed; top: 0; right: 0; width: 55vw; height: 100vh; z-index: 0; pointer-events: none; background-image: url('{b_splash}'); background-size: cover; background-position: center; opacity: 0.35; -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 100%); mask-image: linear-gradient(to left, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 100%);"></div>
        """, unsafe_allow_html=True)

    opponent = st.session_state.get('opponent_name', 'OPPONENT COACH').upper()
    hud_html = f"""
            <div style='display: flex; justify-content: space-between; align-items: center; padding: 0px 20px; margin-bottom: 5px; position: relative; z-index: 100;'>
                <div style='flex: 1; text-align: left; font-weight: 900; font-size: 1.1rem; color: #a5d6a7; text-shadow: 0 0 10px rgba(102, 187, 106, 0.4); letter-spacing: 1px;'>YOU: {st.session_state.p_set_wins}</div>
                <div style='flex: 1; text-align: center; font-weight: 900; font-size: 1.2rem; color: #c8aa6e; text-shadow: 0 0 15px rgba(200, 170, 110, 0.5); letter-spacing: 3px;'>SET {st.session_state.current_set} / 5</div>
                <div style='flex: 1; text-align: right; font-weight: 900; font-size: 1.1rem; color: #ef9a9a; text-shadow: 0 0 10px rgba(239, 83, 80, 0.4); letter-spacing: 1px;'>{opponent}: {st.session_state.b_set_wins}</div>
            </div>
            """
    st.markdown(hud_html, unsafe_allow_html=True)

    # ========================================================
    # RAKİP (BOT) KARTLARI (KIRMIZI ENEMY DOCK İLE)
    # ========================================================
    if st.session_state.phase not in ["game_over", "set_end"]:

        # 1. Düşman Tepsisi Yukarıdan Aşağıya Sarkıyor (Z-INDEX 50 YAPILDI)
        st.markdown("""
                        <div style="position: relative; z-index: 0;">
                            <div class="enemy-dock">
                                <div class="enemy-core"></div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

        # 2. Sağ Üste Hizalı Düşman Skoru (TEPSİNİN ALTINDA KALMAMASI İÇİN Z-INDEX 60 YAPILDI)
        st.markdown(
            f"<div style='position: relative; top: 113px; right: -35px; margin-bottom: 5px; position: relative; z-index: 60; text-align: right; font-size: 11px; color: #ef9a9a; font-weight: bold; letter-spacing: 1.5px; padding-right: 20px; opacity: 0.9;'>ROUND SCORE: {st.session_state.b_round_score}</div>",
            unsafe_allow_html=True)

        # 3. Rakip Kartları
        bot_cols = st.columns(5)
        for i in range(5):
            with bot_cols[i]:
                if i < len(st.session_state.b_hand):
                    anim_class = "deal-bot-card" if st.session_state.turn_count == 0 else ""
                    delay = i * 0.2
                    st.markdown(f"<div class='bot-hidden {anim_class}' style='animation-delay: {delay}s;'></div>",
                                unsafe_allow_html=True)
                else:
                    # EKRANI TİTRETEN ANA SUÇLU BURASIYDI! Artık boş yuva da -65px margin alıyor.
                    st.markdown("<div style='width:110px; height:170px; margin: -65px auto 0 auto;'></div>",
                                unsafe_allow_html=True)

    if st.session_state.phase == "bot_attack_prep":
        b_card = game_logic.bot_choose_card(st.session_state.b_hand,
                                            difficulty=st.session_state.get('bot_difficulty', 'medium'))
        st.session_state.b_hand.remove(b_card)
        st.session_state.arena_b_card = b_card
        st.session_state.phase = "player_defense"
        st.rerun()

    st.markdown("<div style='height: 60px; clear: both;'></div>", unsafe_allow_html=True)
    arena_left, arena_mid, arena_right = st.columns([1.8, 2.6, 1.8])

    # MAVİ ETİKET (Normal haline döndü, negatif margin kaldırıldı)
    label_style_blue = "width: fit-content; margin: 0 auto 10px auto; position: relative; z-index: 5; background-color: rgba(15, 25, 35, 0.85); border: 1px solid rgba(200, 170, 110, 0.6); border-radius: 20px; text-align: center; font-size: 10px; font-weight: 900; color: #c8aa6e; padding: 5px 18px; letter-spacing: 1.5px; box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 0 8px rgba(200,170,110,0.15);"

    # KIRMIZI ETİKET (Normal haline döndü, negatif margin kaldırıldı)
    label_style_red = "width: fit-content; margin: 0 auto 10px auto; position: relative; z-index: 5; background-color: rgba(40, 15, 15, 0.85); border: 1px solid rgba(229, 115, 115, 0.6); border-radius: 20px; text-align: center; font-size: 10px; font-weight: 900; color: #ef9a9a; padding: 5px 18px; letter-spacing: 1.5px; box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 0 8px rgba(229,115,115,0.15);"

    with arena_left:
        if st.session_state.phase not in ["game_over", "set_end"]:
            total_played = (st.session_state.p_round_score + st.session_state.b_round_score) * 2
            st.markdown(f"<div style='{label_style_blue}'>BOARD POWER: {total_played}</div>", unsafe_allow_html=True)
            if total_played > 0: st.markdown("<div class='score-stack'></div>", unsafe_allow_html=True)
        elif st.session_state.phase == "set_end":
            played_cards = st.session_state.get('p_played_cards', [])
            mvp_card = max(played_cards, key=lambda x: x['overall']) if played_cards else None
            if mvp_card:
                mvp_name = get_safe_name(mvp_card['name'])
                st.markdown(f"""
                    <div style='background: rgba(20, 25, 35, 0.85); border: 1px solid #ffd700; border-radius: 12px; padding: 25px 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.5);'>
                        <h4 style='color: #ffd700; margin: 0 0 20px 0; letter-spacing: 2px;'>🌟 SET MVP 🌟</h4>
                        <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{mvp_name}_0.jpg" style="width: 140px; height: 210px; object-fit: cover; border-radius: 8px; border: 2px solid #ffd700; box-shadow: 0 0 25px rgba(255, 215, 0, 0.3); margin-bottom: 20px;">
                        <div style='color: #f0e6d2; font-weight: 900; font-size: 22px; letter-spacing: 1px;'>{mvp_name.upper()}</div>
                        <div style='color: #0ac8b9; font-size: 15px; margin-top: 8px;'>Power Contribution: <b style='font-size: 18px;'>{mvp_card['overall']}</b></div>
                    </div>
                    """, unsafe_allow_html=True)

    with arena_mid:
        if st.session_state.phase not in ["game_over", "set_end"]:
            m_p1, m_vs, m_b1 = st.columns([1, 0.4, 1])
            if st.session_state.phase == "player_attack":
                with m_p1:
                    st.markdown(f"<div style='{label_style_blue}'>YOUR CARD</div>", unsafe_allow_html=True)
                    render_empty_slot("Make a Move", is_arena=True)
                with m_vs:
                    st.markdown(
                        "<div style='height: 270px; display: flex; align-items: center; justify-content: center;'><h3 style='margin: 0; color:#c8aa6e !important;'>VS</h3></div>",
                        unsafe_allow_html=True)
                with m_b1:
                    st.markdown(f"<div style='{label_style_red}'>OPPONENT CARD</div>", unsafe_allow_html=True)
                    render_empty_slot("Waiting...", is_arena=True)
            elif st.session_state.phase == "player_defense":
                with m_p1:
                    st.markdown(f"<div style='{label_style_blue}'>YOUR CARD</div>", unsafe_allow_html=True)
                    render_empty_slot("Choose Defense", is_arena=True)
                with m_vs:
                    st.markdown(
                        "<div style='height: 270px; display: flex; align-items: center; justify-content: center;'><h3 style='margin: 0; color:#c8aa6e !important;'>VS</h3></div>",
                        unsafe_allow_html=True)
                with m_b1:
                    st.markdown(f"<div style='{label_style_red}'>OPPONENT ATTACKED!</div>",
                                unsafe_allow_html=True)
                    render_view_card(st.session_state.arena_b_card, is_arena=True)
            elif st.session_state.phase == "resolve":
                with m_p1:
                    # EKRAN ÇÖKMESİN DİYE ETİKETLER BURADA DA KALIYOR
                    st.markdown(f"<div style='{label_style_blue}'>YOUR CARD</div>", unsafe_allow_html=True)
                    render_view_card(st.session_state.arena_p_card, is_arena=True)
                with m_vs:
                    st.markdown(
                        "<div style='height: 270px; display: flex; align-items: center; justify-content: center;'><h3 style='margin: 0; color:#c8aa6e !important;'>VS</h3></div>",
                        unsafe_allow_html=True)
                with m_b1:
                    st.markdown(f"<div style='{label_style_red}'>OPPONENT CARD</div>", unsafe_allow_html=True)
                    render_view_card(st.session_state.arena_b_card, is_arena=True)

            st.markdown("<div style='height: 2px;'></div>", unsafe_allow_html=True)
            # ... Altındaki kodlar (Next round butonu vs.) aynı kalıyor ...
            _, b_col, _ = st.columns([0.2, 1, 0.2])
            with b_col:
                if st.session_state.phase == "resolve":
                    banner_class = "banner-info"
                    winner_card = None
                    if "WON" in st.session_state.combat_log:
                        banner_class = "banner-win"
                        winner_card = st.session_state.arena_p_card
                    elif "LOST" in st.session_state.combat_log:
                        banner_class = "banner-lose"
                        winner_card = st.session_state.arena_b_card
                    elif "DRAW" in st.session_state.combat_log:
                        banner_class = "banner-draw"

                    if winner_card:
                        play_champion_voice(winner_card['name'])

                    st.markdown(
                        f"<div class='banner {banner_class}' style='margin: 2px 0; padding: 6px;'>{st.session_state.combat_log}</div>",
                        unsafe_allow_html=True)
                    if st.button("Next Round", type="primary", use_container_width=True):
                        next_round()
                        st.rerun()

        elif st.session_state.phase == "set_end":
            current_stage_data = TOURNAMENT_STAGES[st.session_state.tour_stage]
            current_boss_splash = get_splash_url(current_stage_data['splash'])
            st.markdown(
                f"<style>.stApp {{ background-image: linear-gradient(rgba(15,22,35,0.85), rgba(15,22,35,0.95)), url('{current_boss_splash}'); background-size: cover; background-position: center top; background-attachment: fixed !important; }}</style>",
                unsafe_allow_html=True)
            is_set_won = "WON" in st.session_state.combat_log
            box_color = "rgba(10, 200, 185, 0.15)" if is_set_won else "rgba(229, 115, 115, 0.15)"
            border_color = "#0ac8b9" if is_set_won else "#e57373"

            st.markdown(f"""
                <div style='background: {box_color}; backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px); border: 1px solid {border_color}; border-radius: 12px; padding: 30px 25px; text-align: center; margin-top: 15px; box-shadow: 0 8px 32px 0 rgba(0,0,0,0.6);'>
                    <h2 style='color: {border_color}; margin: 0; text-shadow: 0 0 15px {border_color}; letter-spacing: 2px;'>{st.session_state.combat_log}</h2>
                    <div style='width: 60%; height: 1px; background: {border_color}; margin: 20px auto; opacity: 0.5;'></div>
                    <h5 style='color: #c8aa6e; margin: 0 0 10px 0; letter-spacing: 1px;'>SET SCORE</h5>
                    <p style='color: #f0e6d2; font-size: 26px; margin: 0; font-weight: 900;'>YOU {st.session_state.p_round_score} - {st.session_state.b_round_score} OPPONENT</p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
            if st.button("Proceed to Next Set", type="primary", use_container_width=True):
                start_next_set_action()
                st.rerun()

        elif st.session_state.phase == "game_over":
            is_player_won = st.session_state.p_set_wins > st.session_state.b_set_wins
            if is_player_won and st.session_state.tour_stage < 3:
                next_stage_data = TOURNAMENT_STAGES[st.session_state.tour_stage + 1]
                next_boss = next_stage_data['bot']
                next_boss_splash = get_splash_url(next_stage_data['splash'])
                st.markdown(
                    f"<style>.stApp {{ background-image: linear-gradient(rgba(10, 15, 25, 0.75), rgba(10, 15, 25, 0.95)), url('{next_boss_splash}'); background-size: cover; background-position: center top; background-attachment: fixed !important; }}</style>",
                    unsafe_allow_html=True)
                st.markdown(f"""
                        <div style='position: relative; border: 2px solid #0ac8b9; border-radius: 12px; margin-top: 50px; overflow: hidden; box-shadow: 0 0 50px rgba(10, 200, 185, 0.4); max-width: 800px; margin-left: auto; margin-right: auto;'>
                            <div style='position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: url("{next_boss_splash}"); background-size: cover; background-position: center 20%; opacity: 0.5; z-index: 0; filter: blur(3px) brightness(1.2);'></div>
                            <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(15,22,35,0.4) 0%, rgba(15,22,35,0.95) 100%); z-index: 1;"></div>
                            <div style='position: relative; z-index: 2; padding: 60px 30px; text-align: center;'>
                                <h1 style='color: #0ac8b9; margin: 0; font-size: 3.5rem; text-shadow: 0 0 30px #0ac8b9; letter-spacing: 5px; text-transform: uppercase;'>STAGE CLEARED!</h1>
                                <div style='width: 50%; height: 2px; background: #0ac8b9; margin: 25px auto; opacity: 0.7; box-shadow: 0 0 15px #0ac8b9;'></div>
                                <p style='color: #c8aa6e; margin: 0 0 10px 0; font-size: 16px; letter-spacing: 6px; font-weight: bold;'>NEXT CHALLENGER AWAKENS</p>
                                <h2 style='color: #f0e6d2; margin: 0; font-size: 2.5rem; font-style: italic; text-shadow: 0 0 20px rgba(240, 230, 210, 0.5);'>{next_boss}</h2>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([1.5, 1, 1.5])
                with c2:
                    if st.button("Enter Next Stage", type="primary", use_container_width=True):
                        st.session_state.tour_stage += 1
                        init_game(is_next_stage=True)
                        st.rerun()
            else:
                if is_player_won:
                    # AZIR: Altın Shurima İmparatorluğu Zaferi
                    bg_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Azir_0.jpg"
                    box_color, border_color = "rgba(10, 15, 20, 0.75)", "#ffd700"
                    final_title = "GRAND CHAMPION"
                    glow_anim = "gold-pulse"
                    bg_overlay = "linear-gradient(rgba(10, 15, 5, 0.55), rgba(5, 5, 5, 0.85))"
                else:
                    # AMUMU: Yalnızlık ve Yenilgi Hüznü
                    bg_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Amumu_0.jpg"
                    box_color, border_color = "rgba(20, 5, 5, 0.75)", "#e57373"
                    final_title = "ELIMINATED"
                    glow_anim = "red-pulse"
                    bg_overlay = "linear-gradient(rgba(25, 5, 5, 0.55), rgba(10, 2, 2, 0.85))"

                bg_css = f"<style>.stApp {{ background-image: {bg_overlay}, url('{bg_url}'); background-size: cover; background-position: center; background-attachment: fixed !important; }}</style>"

                # 1. Premium CSS: Sadece Temiz Cam Kutu (Rozet tamamen silindi)
                st.markdown(bg_css, unsafe_allow_html=True)
                st.markdown(f"""
                            <style>
                                @keyframes {glow_anim} {{
                                    0% {{ box-shadow: 0 0 15px {border_color}4d, inset 0 0 15px {border_color}33; border-color: {border_color}80; }}
                                    50% {{ box-shadow: 0 0 40px {border_color}cc, inset 0 0 25px {border_color}66; border-color: {border_color}; }}
                                    100% {{ box-shadow: 0 0 15px {border_color}4d, inset 0 0 15px {border_color}33; border-color: {border_color}80; }}
                                }}
                                .endgame-box {{
                                    background: {box_color};
                                    backdrop-filter: blur(20px);
                                    -webkit-backdrop-filter: blur(20px);
                                    border: 2px solid {border_color};
                                    border-radius: 16px;
                                    padding: 45px 20px; /* Üstteki ekstra rozet boşluğunu tıraşladık */
                                    text-align: center;
                                    margin-top: 40px; /* Kutuyu ekranın merkezine daha uyumlu hizaladık */
                                    max-width: 650px;
                                    margin-left: auto;
                                    margin-right: auto;
                                    animation: {glow_anim} 3s infinite;
                                    position: relative;
                                }}
                            </style>
                            """, unsafe_allow_html=True)

                # 2. HTML: Rozetsiz, Sadece Yazı ve Cam Efekti
                st.markdown(f"""
                                    <div class='endgame-box'>
                                        <h1 style='color: {border_color}; margin: 0; font-size: 3rem; text-shadow: 0 0 30px {border_color}; letter-spacing: 5px; text-transform: uppercase;'>{final_title}</h1>
                                        <div style='width: 50%; height: 2px; background: linear-gradient(90deg, transparent, {border_color}, transparent); margin: 20px auto; opacity: 0.8;'></div>
                                        <h4 style='color: #c8aa6e; margin: 0 0 10px 0; font-size: 1rem; letter-spacing: 4px; text-transform: uppercase;'>FINAL TOURNAMENT RESULT</h4>
                                        <p style='color: #f0e6d2; font-size: 28px; margin: 0; font-weight: 900; text-shadow: 0 0 15px rgba(240, 230, 210, 0.4); letter-spacing: 2px;'>
                                            <span style='color: #0ac8b9;'>YOU {st.session_state.p_set_wins}</span> 
                                            <span style='color: rgba(240,230,210,0.4);'>-</span> 
                                            <span style='color: #e57373;'>{st.session_state.b_set_wins} OPPONENT</span>
                                        </p>
                                    </div>
                                    """, unsafe_allow_html=True)

                # 3. Yeniden Başlatma Butonu
                st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([1.5, 1, 1.5])
                with c2:
                    if st.button("Start New Tournament", type="primary", use_container_width=True):
                        st.session_state.game_started = False
                        st.session_state.synergy_charges = 0
                        st.rerun()

    with arena_right:
        if st.session_state.phase not in ["game_over", "set_end"]:
            total_deck = len(st.session_state.p_deck) * 2
            st.markdown(f"<div style='{label_style_blue}'>MAIN DECK: {total_deck}</div>", unsafe_allow_html=True)
            if total_deck > 0: st.markdown("<div class='deck-stack'></div>", unsafe_allow_html=True)
        elif st.session_state.phase == "set_end":
            st.markdown(
                "<div style='color: #c8aa6e; font-weight: 900; font-size: 14px; letter-spacing: 2px; margin-bottom: 20px;'>TOURNAMENT PROGRESS</div>",
                unsafe_allow_html=True)
            stages_html = ""
            for i in range(1, 4):
                stage_data = TOURNAMENT_STAGES[i]
                boss_name = stage_data['bot'].split(" ")[0]
                splash_url = get_splash_url(stage_data['splash'])
                if i < st.session_state.tour_stage:
                    border, overlay, text, filter_style = "#0ac8b9", "rgba(10, 200, 185, 0.2)", "✅ CLEARED", "grayscale(50%)"
                elif i == st.session_state.tour_stage:
                    border, overlay, text, filter_style = "#ffd700", "rgba(255, 215, 0, 0.3)", "⚔️ CURRENT TARGET", "none"
                else:
                    border, overlay, text, filter_style = "#7a5c29", "rgba(15, 22, 35, 0.7)", "🔒 LOCKED", "grayscale(100%) blur(2px)"

                stages_html += f"""
                            <div style='position: relative; height: 180px; border-radius: 8px; margin-bottom: 15px; overflow: hidden; border: 2px solid {border}; box-shadow: 0 0 10px rgba(0,0,0,0.5);'>
                                <div style="position: absolute; inset: 0; background-image: url('{splash_url}'); background-size: cover; background-position: center 20%; filter: {filter_style}; z-index: 0;"></div>
                                <div style="position: absolute; inset: 0; background: {overlay}; z-index: 1;"></div>
                                <div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0.9) 100%); z-index: 2;"></div>
                                <div style="position: relative; z-index: 3; display: flex; justify-content: space-between; align-items: center; height: 100%; padding: 0 20px;">
                                    <div style="color: {border}; font-weight: 900; font-size: 18px; text-shadow: 0 2px 4px rgba(0,0,0,0.9);">STAGE {i}<br><span style="color: #f0e6d2; font-size: 14px; letter-spacing: 1px;">{boss_name}</span></div>
                                    <div style="color: {border}; font-size: 13px; font-weight: bold; letter-spacing: 1.5px; text-shadow: 0 2px 4px rgba(0,0,0,0.9);">{text}</div>
                                </div>
                            </div>
                            """
            st.markdown(stages_html + "</div>", unsafe_allow_html=True)

            # ========================================================
            # OYUNCU KARTLARI (VIP HEXTECH TEPSİSİ İLE)
            # ========================================================
        # ========================================================
        # OYUNCU KARTLARI (YENİ NESİL HEXTECH TEPSİSİ İLE)
        # ========================================================
    if st.session_state.phase not in ["game_over", "set_end"]:

        # 1. CSS'ten Gelen Efsanevi Tepsi
        st.markdown("""
            <div style="position: relative; z-index: 0;">
                <div class="hextech-dock">
                    <div class="hextech-core"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 2. Zarif Skor Yazısı (Tepsiye Uyumlu)
        st.markdown(
            f"<div style='margin-top: -10px; position: relative; z-index: 1; text-align: left; font-size: 11px; color: #c8aa6e; font-weight: bold; letter-spacing: 1.5px; padding-left: 20px; opacity: 0.9;'>ROUND SCORE: {st.session_state.p_round_score}</div>",
            unsafe_allow_html=True)

        st.markdown("<div style='min-height: 30px;'></div>", unsafe_allow_html=True)

    # ========================================================
    # 3. KARTLAR VE GİZEMLİ YETENEK KARTI (6 KOLONLU SİSTEM)
    # ========================================================
    # Ekranı 6 parçaya bölüyoruz: İlk 5'i normal kartlar, 6.sı Joker Kart
    player_cols = st.columns([1, 1, 1, 1, 1, 1.5])

    # A) KARTLARI ÇİZ (İlk 5 Kolon)
    for i in range(5):
        with player_cols[i]:
            if i < len(st.session_state.p_hand):

                # Sinerji Kontrolü (Görsel Bağlar)
                if i < len(st.session_state.p_hand) - 1:
                    current_card_name = st.session_state.p_hand[i].get("name")
                    next_card_name = st.session_state.p_hand[i + 1].get("name")
                    synergy = check_synergy(current_card_name, next_card_name)
                    if synergy:
                        st.markdown(get_synergy_svg(synergy), unsafe_allow_html=True)

                card = st.session_state.p_hand[i]
                anim_class = "deal-player-card" if st.session_state.turn_count == 0 else ""
                delay = i * 0.2

                if st.session_state.phase in ["player_attack", "player_defense"]:
                    render_playable_card(card, i, st.session_state.phase, anim_class, delay)
                else:
                    render_view_card(card, False, anim_class, delay)
            else:
                st.markdown("<div style='width:110px; height: 195px; margin: 0 auto;'></div>", unsafe_allow_html=True)

    # B) GİZEMLİ JOKER KARTI (6. Kolon)
    # B) GİZEMLİ HEXTECH KARTI (6. Kolon)
    # B) GİZEMLİ HEXTECH KAPSÜLÜ (6. Kolon - Premium Tasarım)
    with player_cols[5]:
        # Şarj durumunu ve maksimum limiti alıyoruz
        charge = st.session_state.get('synergy_charges', 0)
        max_charge = 3

        if charge == 0:
            # 0. ŞARJ: Boş
            crystal_bg = "linear-gradient(180deg, #2a353c 0%, #1a252c 100%)"
            glow = "none"
            border = "#33414a"
            anim = "none"
            text_color = "#7a8c99"
            status_text = "DEPLETED"
        elif charge == 1:
            # 1. ŞARJ: Zümrüt Yeşili (Uyanış)
            crystal_bg = "linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(57,255,20,1) 40%, rgba(10,80,15,1) 100%)"
            glow = "0 0 15px rgba(57, 255, 20, 0.6)"
            border = "#39ff14"
            anim = "none"
            text_color = "#39ff14"
            status_text = "CHARGING (1/3)"
        elif charge == 2:
            # 2. ŞARJ: Hextech Mavisi (Güçlenme)
            crystal_bg = "linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(10,200,185,1) 40%, rgba(5,100,90,1) 100%)"
            glow = "0 0 25px rgba(10, 200, 185, 0.8)"
            border = "#0ac8b9"
            anim = "none"
            text_color = "#0ac8b9"
            status_text = "CHARGING (2/3)"
        else:
            # 3. ŞARJ: Tam Dolu (Altın)
            crystal_bg = "linear-gradient(180deg, #ffffff 0%, #0ac8b9 30%, #ffd700 100%)"
            glow = "0 0 25px #0ac8b9, 0 0 40px #ffd700"
            border = "#ffd700"
            anim = "hex-pulse 1.5s infinite"
            text_color = "#ffd700"
            status_text = "ULTIMATE READY"

        # İŞTE PYCHARM'I AĞLATAN TEK SATIRLIK KOD:
        hextech_html = f"""<style>@keyframes hex-pulse {{ 0% {{ transform: scale(1); filter: brightness(1); box-shadow: {glow}; }} 50% {{ transform: scale(1.08); filter: brightness(1.2); box-shadow: 0 0 40px #ffd700, 0 0 20px #0ac8b9; }} 100% {{ transform: scale(1); filter: brightness(1); box-shadow: {glow}; }} }} .hex-slot {{ width: 100%; height: 190px; background: linear-gradient(135deg, #0a1015, #121a20); border: 2px solid {border}; border-radius: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.6), inset 0 0 20px rgba(0,0,0,0.8); position: relative; overflow: hidden; transition: all 0.4s ease; }} .hex-crystal {{ width: 55px; height: 65px; background: {crystal_bg}; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); box-shadow: {glow}; animation: {anim}; transition: all 0.5s ease; z-index: 2; }} .hex-text {{ margin-top: 15px; color: {text_color}; font-weight: 900; letter-spacing: 2px; font-size: 13px; font-family: 'Arial', sans-serif; text-shadow: 0 0 10px {text_color}; z-index: 2; }} .hex-charge-count {{ color: white; font-size: 22px; font-weight: bold; margin-top: 5px; text-shadow: 0 0 5px rgba(255,255,255,0.5); }} </style><div class="hex-slot"><div class="hex-crystal"></div><div class="hex-text">{status_text}</div><div class="hex-charge-count">{charge} / {max_charge}</div></div>"""

        st.markdown(hextech_html, unsafe_allow_html=True)

        if charge >= max_charge:
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            if st.button("⚡ REROLL", key="mulligan_btn", use_container_width=True):
                target_idx = st.session_state.get("selected_card_idx")
                if target_idx is not None:
                    import random

                    all_champs = lol_data.get_champions_data()

                    exclude_names = set()
                    exclude_names.update([c['name'] for c in st.session_state.p_hand])
                    exclude_names.update([c['name'] for c in st.session_state.b_hand])
                    exclude_names.update([c['name'] for c in st.session_state.p_deck])
                    exclude_names.update([c['name'] for c in st.session_state.b_deck])
                    if 'p_played_cards' in st.session_state:
                        exclude_names.update([c['name'] for c in st.session_state.p_played_cards])
                    if st.session_state.arena_p_card:
                        exclude_names.add(st.session_state.arena_p_card['name'])
                    if st.session_state.arena_b_card:
                        exclude_names.add(st.session_state.arena_b_card['name'])

                    premium_pool = [c for c in all_champs if
                                    c['name'] not in exclude_names and c.get('overall', 0) >= 85]
                    if not premium_pool:
                        premium_pool = [c for c in all_champs if c['name'] not in exclude_names]

                    if premium_pool:
                        yeni_kart = random.choice(premium_pool)
                        st.session_state.p_hand[target_idx] = yeni_kart
                        st.session_state.synergy_charges = 0
                        st.session_state.selected_card_idx = None
                        st.rerun()
                    else:
                        st.warning("No unique champions left!")
                else:
                    st.warning("Please select a card to reroll first!")
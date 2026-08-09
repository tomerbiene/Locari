import random


def initialize_game(all_champions, total_cards=70):
    """
    Tüm LoL şampiyonları arasından maça özel rastgele 70 şampiyon seçer.
    Aynı şampiyonun iki kere gelmesini engellemek için isim bazlı filtre (unique) uygular.
    """
    # Benzersiz (unique) şampiyonları garantiye alıyoruz
    unique_champs = {champ["name"]: champ for champ in all_champions}.values()
    shuffled = list(unique_champs)
    random.shuffle(shuffled)

    # 170+ havuzdan sadece 70 tanesini bu maç için kilitliyoruz
    selected_pool = shuffled[:total_cards]

    half_point = total_cards // 2
    p_deck = selected_pool[:half_point]
    b_deck = selected_pool[half_point:]

    return p_deck, b_deck


def draw_cards(deck, target_size=7):
    """
    Yeni set başladığında desteden tam 7 kart çeker.
    """
    drawn = deck[:target_size]
    remaining = deck[target_size:]
    return remaining, drawn


import random


def bot_choose_card(hand, player_card=None, difficulty="medium"):
    """
    Botun zorluk seviyesine (turnuva aşamasına) göre karar verme mekanizması.
    - easy (1. Aşama): %65 ihtimalle hata yapar, rastgele kart atar. (Çaylak)
    - medium (2. Aşama): %30 ihtimalle hata yapar. (Standart)
    - hard (3. Aşama): %0 hata yapar. Tamamen matematiksel ve kusursuz oynar. (Şampiyon)
    """
    error_rates = {
        "easy": 0.65,
        "medium": 0.30,
        "hard": 0.0
    }

    # Zorluk seviyesini çek, bulamazsa varsayılan olarak 'medium' al
    error_chance = error_rates.get(difficulty, 0.30)

    # --- 1. HATA YAPMA İHTİMALİ (Zeka zayıfsa veya şansı yaver gitmezse) ---
    if random.random() < error_chance:
        return random.choice(hand)  # Hiç hesaplamadan tamamen rastgele bir kart oynar

    # --- 2. KUSURSUZ AKILLI HAMLE (Zirve Kapışması veya Hata Yapmadığı Anlar) ---
    if player_card:
        # DURUM A: Savunma (Oyuncu saldırmış, bot cevap veriyor)
        # Taktik: Oyuncunun kartını yenebilecek en düşük gücü harca (İsraf yapma)
        winning_cards = [c for c in hand if c['overall'] > player_card['overall']]
        if winning_cards:
            return min(winning_cards, key=lambda x: x['overall'])
        else:
            # Taktik: Yenecek kartı yoksa, boşuna güçlü kart kurban etme, elindeki en zayıf kartı at.
            return min(hand, key=lambda x: x['overall'])
    else:
        # DURUM B: Saldırı (Bot ilk hamleyi yapıyor)
        # Taktik: Eli domine etmek ve oyuncuyu zorlamak için elindeki en güçlü ilk 2 karttan birini atar
        sorted_hand = sorted(hand, key=lambda x: x['overall'], reverse=True)
        if len(sorted_hand) == 1:
            return sorted_hand[0]

        return random.choice(sorted_hand[:2])


def evaluate_round(player_card, bot_card):
    """
    Saf güç karşılaştırması.
    """
    p_val = player_card["overall"]
    b_val = bot_card["overall"]

    if p_val > b_val:
        winner = "player"
    elif b_val > p_val:
        winner = "bot"
    else:
        winner = "draw"

    return winner, p_val, b_val, False, False
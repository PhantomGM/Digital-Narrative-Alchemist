import random

# --- NPC Generator ---
def generate_npc_dna():
    """Generates a Personality DNA code for an NPC."""
    lnc_traits = [
        ("B", "C"), ("R", "O"), ("L", "T"), ("F", "I"), ("S", "X"),
        ("P", "M"), ("D", "U"), ("G", "H"), ("Y", "W"), ("E", "A"),
        ("N", "V"), ("K", "Q"), ("Z", "B"), ("O", "P"), ("C", "H"),
        ("R", "L"), ("A", "S"), ("D", "A"), ("A", "H"), ("I", "C")
    ]
    gne_traits = [
        "H", "C", "K", "G", "L", "J", "M", "F", "E", "B", "U", "S", "I", "R", "T", "A", "D", "V", "Y", "X"
    ]
    lnc_dna = []
    lnc_scores = []
    for pair in lnc_traits:
        chosen_trait = random.choice(pair)
        lnc_score = random.randint(1, 9)
        intensity = random.randint(1, 5)
        lnc_scores.append(lnc_score)
        lnc_dna.append(f"{lnc_score}{chosen_trait[0]}{intensity}")
    gne_dna = []
    gne_scores = []
    for trait in gne_traits:
        gne_score = random.randint(1, 9)
        gne_scores.append(gne_score)
        gne_dna.append(f"{trait[0]}{gne_score}")
    lnc_average = round(sum(lnc_scores) / len(lnc_scores))
    gne_average = round(sum(gne_scores) / len(gne_scores))
    return f"({lnc_average}/{gne_average}) {','.join(lnc_dna)} - {','.join(gne_dna)}"

# --- Faction Generator ---
def generate_faction_dna():
    """Generates a DNA string for a Faction."""
    DNA_TRAITS = {
        "T": ["T1", "T2", "T3", "T4", "T5", "T6", "T7"],
        "G": [f"G{i:02}" for i in range(1, 13)],
        "M": [f"M{i}" for i in range(1, 9)],
        "P": [f"P{i}" for i in range(1, 9)],
        "S": [f"S{i}" for i in range(1, 7)],
        "O": [f"O{i}" for i in range(1, 8)],
        "N": ["N74", "N78", "N84", "N90", "N92", "N99"],
        "L": [f"L{i:02}" for i in range(1, 11)],
        "F": [f"F{i}" for i in range(1, 7)],
        "D": [f"D{i}" for i in range(1, 7)],
        "A": [f"A{i}" for i in range(1, 10)],
        "SC": [f"SC{i}" for i in range(1, 6)],
        "MZ": [f"MZ{i}" for i in range(1, 7)],
        "X": [f"X{i}" for i in range(1, 7)]
    }
    dna_segments = [random.choice(DNA_TRAITS[key]) for key in DNA_TRAITS]
    return "-".join(dna_segments)

# --- Quest Generator ---
def generate_quest_dna():
    """Generates a DNA string for a Quest."""
    difficulty = random.randint(1, 9)
    complexity = random.randint(1, 9)
    reward = random.randint(1, 9)
    quest_type = random.choice(["fetch", "rescue", "escort", "eliminate", "explore", "deliver", "investigate", "protect", "infiltrate"])
    goal = {k: random.randint(10, 99) for k in "CRESTPLH"}
    obs = {k: random.randint(10, 99) for k in "CMETP SGN"}
    rew = {k: random.randint(10, 99) for k in "MIKR SPLA"}
    narr = {k: random.randint(10, 99) for k in "TCP MHRIA"}
    motiv = {k: random.randint(10, 99) for k in "GRDSPVFJ"}
    engage = {k: random.randint(10, 99) for k in ["COMBAT", "SOCIAL", "EXPLORE", "PUZZLE"]}
    chains = {"OBS": "P>M>G", "REWARD": "K>I>A", "MOTIV": "D>J>P"}
    evo_d = sorted([random.randint(50, 99) for _ in range(4)])
    evo_c = sorted([random.randint(50, 99) for _ in range(4)])
    evo_r = sorted([random.randint(50, 99) for _ in range(4)])
    evo_types = ["RISING", "STABLE", "ACCELERATING", "DESCENDING", "FLUCTUATING", "CLIMACTIC"]
    d_type, c_type, r_type = [random.choice(evo_types) for _ in range(3)]
    
    return (f"QUEST{{v1.0[{difficulty}/{complexity}/{reward}]}}"
            f"<DI:{round(random.uniform(0.1, 2.0), 1)},CR:{round(random.uniform(0.1, 2.0), 1)},DR:{round(random.uniform(0.1, 2.0), 1)}>#{quest_type}\n"
            f"GOAL{{{','.join([k+str(v) for k, v in goal.items()])}}}\n"
            f"OBS{{{','.join([k+str(v) for k, v in obs.items()])}}}\n"
            f"REWARD{{{','.join([k+str(v) for k, v in rew.items()])}}}\n"
            f"NARR{{{','.join([k+str(v) for k, v in narr.items()])}}}\n"
            f"MOTIV{{{','.join([k+str(v) for k, v in motiv.items()])}}}\n"
            f"CHAIN{{OBS:{chains['OBS']};REWARD:{chains['REWARD']};MOTIV:{chains['MOTIV']}}}\n"
            f"ENGAGE{{{','.join([k+':'+str(v) for k, v in engage.items()])}}}\n"
            f"EVO{{D:{d_type}{evo_d};C:{c_type}{evo_c};R:{r_type}{evo_r}}}")

# --- Item Generator ---
def generate_item_dna():
    """Generates a DNA string for a Magic Item."""
    power_level = random.randint(1, 9)
    magical_complexity = random.randint(1, 9)
    rarity = random.randint(1, 9)
    item_type = random.choice(["weapon", "armor", "wand", "staff", "ring", "amulet", "potion", "scroll", "book", "relic"])
    phy = {k: random.randint(10, 99) for k in "MSADCWFT"}
    mag = {k: random.randint(10, 99) for k in "PEDCSART"}
    his = {k: random.randint(10, 99) for k in "OCARLFDS"}
    lor = {k: random.randint(10, 99) for k in "KFNCREIS"}
    attune = {k: random.randint(10, 99) for k in "UWCMSVPR"}
    chains = {"USE": "P>E>C", "MAG": "D>S>R", "ATT": "S>C>W"}
    p_values = sorted([random.randint(50, 99) for _ in range(4)])
    m_values = sorted([random.randint(50, 99) for _ in range(4)])
    evo_types = ["STABLE", "UNSTABLE", "ACCELERATING", "DECAYING", "FLUCTUATING", "DORMANT"]
    p_type, m_type = random.choice(evo_types), random.choice(evo_types)
    
    return (f"ITEM{{v1.0[{power_level}/{magical_complexity}/{rarity}]}}"
            f"<AP:{round(random.uniform(0.1, 2.0), 1)},MR:{round(random.uniform(0.1, 2.0), 1)},RE:{round(random.uniform(0.1, 2.0), 1)}>#{item_type}\n"
            f"PHY{{{','.join([k+str(v) for k, v in phy.items()])}}}\n"
            f"MAG{{{','.join([k+str(v) for k, v in mag.items()])}}}\n"
            f"HIS{{{','.join([k+str(v) for k, v in his.items()])}}}\n"
            f"LOR{{{','.join([k+str(v) for k, v in lor.items()])}}}\n"
            f"ATTUNE{{{','.join([k+str(v) for k, v in attune.items()])}}}\n"
            f"CHAIN{{USE:{chains['USE']};MAG:{chains['MAG']};ATT:{chains['ATT']}}}\n"
            f"EVO{{P:{p_type}{p_values};M:{m_type}{m_values}}}")

# --- Location (Settlement) Generator ---
def generate_location_dna():
    """Generates a DNA string for a Location/Settlement."""
    size = random.randint(1, 9)
    population = random.randint(1, 9)
    importance = random.randint(1, 9)
    settlement_type = random.choice(["village", "town", "city", "outpost", "port-city", "fortress", "capital", "hamlet", "metropolis"])
    struct = {k: random.randint(10, 99) for k in "SDWAFUPQ"}
    pop = {k: random.randint(10, 99) for k in "SDACLHCM"}
    econ = {k: random.randint(10, 99) for k in "MTRPSGIL"}
    pol = {k: random.randint(10, 99) for k in "GCRFSCLI"}
    poi = {k: random.randint(10, 99) for k in "ISRDHAMC"}
    proxi = {k: random.randint(10, 99) for k in ["WILD", "TOWN", "CITY", "RUIN"]}
    chains = {"POP": "D>A>H", "ECON": "R>T>G", "POL": "G>R>S"}
    s_values = sorted([random.randint(50, 99) for _ in range(4)])
    p_values = sorted([random.randint(50, 99) for _ in range(4)])
    i_values = sorted([random.randint(50, 99) for _ in range(4)])
    evo_types = ["STABLE", "RISING", "DECLINING", "FLUCTUATING", "TRANSFORMING", "STAGNANT"]
    s_type, p_type, i_type = [random.choice(evo_types) for _ in range(3)]

    return (f"SETTLEMENT{{v1.0[{size}/{population}/{importance}]}}"
            f"<SP:{round(random.uniform(0.1, 2.0), 1)},PI:{round(random.uniform(0.1, 2.0), 1)},SI:{round(random.uniform(0.1, 2.0), 1)}>#{settlement_type}\n"
            f"STRUCT{{{','.join([k+str(v) for k, v in struct.items()])}}}\n"
            f"POP{{{','.join([k+str(v) for k, v in pop.items()])}}}\n"
            f"ECON{{{','.join([k+str(v) for k, v in econ.items()])}}}\n"
            f"POL{{{','.join([k+str(v) for k, v in pol.items()])}}}\n"
            f"POI{{{','.join([k+str(v) for k, v in poi.items()])}}}\n"
            f"CHAIN{{POP:{chains['POP']};ECON:{chains['ECON']};POL:{chains['POL']}}}\n"
            f"PROXI{{{','.join([k+':'+str(v) for k, v in proxi.items()])}}}\n"
            f"EVO{{S:{s_type}{s_values};P:{p_type}{p_values};I:{i_type}{i_values}}}")


# --- Travel Generator ---
def generate_travel_dna():
    """Generates a DNA string for a Travel Scenario."""
    danger = random.randint(1, 5)
    discovery = random.randint(1, 6)
    special_factor = random.randint(0, 5)
    return f"TRAVEL{{{danger}-{discovery}-{special_factor}}}"


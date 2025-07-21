# Digital Narrative Alchemist: Master Generator System
# Full System Code with all Generators integrated (Version 2.2)
# This script contains functions to generate procedural DNA strings for various TTRPG elements.

import random

# --- CORE GENERATOR FUNCTIONS ---

def generate_npc_dna():
    """Generates a detailed Personality DNA code for an NPC."""
    lnc_traits = [
        ("B", "C"), ("R", "O"), ("L", "T"), ("F", "I"), ("S", "X"),
        ("P", "M"), ("D", "U"), ("G", "H"), ("Y", "W"), ("E", "A"),
        ("N", "V"), ("K", "Q"), ("Z", "B"), ("O", "P"), ("C", "H"),
        ("R", "L"), ("A", "S"), ("D", "A"), ("A", "H"), ("I", "C")
    ]
    gne_traits = "HCKGLJMFBUSIRTADVYX"
    
    lnc_dna_parts = []
    lnc_scores = []
    for pair in lnc_traits:
        chosen_trait = random.choice(pair)
        lnc_score = random.randint(1, 9)
        intensity = random.randint(1, 5)
        lnc_scores.append(lnc_score)
        lnc_dna_parts.append(f"{lnc_score}{chosen_trait[0]}{intensity}")

    gne_dna_parts = []
    gne_scores = []
    for trait in gne_traits:
        gne_score = random.randint(1, 9)
        gne_scores.append(gne_score)
        gne_dna_parts.append(f"{trait[0]}{gne_score}")

    lnc_average = round(sum(lnc_scores) / len(lnc_scores)) if lnc_scores else 5
    gne_average = round(sum(gne_scores) / len(gne_scores)) if gne_scores else 5
    
    return f"({lnc_average}/{gne_average}) {','.join(lnc_dna_parts)} - {','.join(gne_dna_parts)}"

def generate_faction_dna():
    """Generates a DNA string for a Faction."""
    dna_traits = {
        "T": [f"T{i}" for i in range(1, 8)],
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
    dna_segments = [random.choice(dna_traits[key]) for key in dna_traits]
    return "-".join(dna_segments)

def generate_quest_dna():
    """Generates a detailed, multi-line DNA string for a Quest."""
    difficulty, complexity, reward = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
    quest_type = random.choice(["fetch", "rescue", "escort", "eliminate", "explore", "deliver", "investigate", "protect", "infiltrate"])
    
    goal = {k: random.randint(10, 99) for k in "CRESTPLH"}
    obs = {k: random.randint(10, 99) for k in "CMETPSGN"}
    rew = {k: random.randint(10, 99) for k in "MIKRSPLA"}
    narr = {k: random.randint(10, 99) for k in "TCPMHRIA"}
    motiv = {k: random.randint(10, 99) for k in "GRDSPVFJ"}
    engage = {k: random.randint(10, 99) for k in ["COMBAT", "SOCIAL", "EXPLORE", "PUZZLE"]}
    
    chains = {"OBS": "P>M>G", "REWARD": "K>I>A", "MOTIV": "D>J>P"}
    evo_types = ["RISING", "STABLE", "ACCELERATING", "DESCENDING", "FLUCTUATING", "CLIMACTIC"]
    
    evo = {
        'D': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'C': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'R': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}"
    }

    return (f"QUEST{{v1.0[{difficulty}/{complexity}/{reward}]}}"
            f"<DI:{round(random.uniform(0.1, 2.0), 1)},CR:{round(random.uniform(0.1, 2.0), 1)},DR:{round(random.uniform(0.1, 2.0), 1)}>#{quest_type}\n"
            f"GOAL{{{','.join([k+str(v) for k, v in goal.items()])}}}\n"
            f"OBS{{{','.join([k+str(v) for k, v in obs.items()])}}}\n"
            f"REWARD{{{','.join([k+str(v) for k, v in rew.items()])}}}\n"
            f"NARR{{{','.join([k+str(v) for k, v in narr.items()])}}}\n"
            f"MOTIV{{{','.join([k+str(v) for k, v in motiv.items()])}}}\n"
            f"CHAIN{{OBS:{chains['OBS']};REWARD:{chains['REWARD']};MOTIV:{chains['MOTIV']}}}\n"
            f"ENGAGE{{{','.join([k+':'+str(v) for k, v in engage.items()])}}}\n"
            f"EVO{{D:{evo['D']};C:{evo['C']};R:{evo['R']}}}")

def generate_item_dna():
    """Generates a detailed, multi-line DNA string for a Magic Item."""
    power, complexity, rarity = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
    item_type = random.choice(["weapon", "armor", "wand", "staff", "ring", "amulet", "potion", "scroll", "book", "relic"])
    
    phy = {k: random.randint(10, 99) for k in "MSADCWFT"}
    mag = {k: random.randint(10, 99) for k in "PEDCSART"}
    his = {k: random.randint(10, 99) for k in "OCARLFDS"}
    lor = {k: random.randint(10, 99) for k in "KFNCREIS"}
    attune = {k: random.randint(10, 99) for k in "UWCMSVPR"}
    
    chains = {"USE": "P>E>C", "MAG": "D>S>R", "ATT": "S>C>W"}
    evo_types = ["STABLE", "UNSTABLE", "ACCELERATING", "DECAYING", "FLUCTUATING", "DORMANT"]
    
    evo = {
        'P': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'M': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}"
    }

    return (f"ITEM{{v1.0[{power}/{complexity}/{rarity}]}}"
            f"<AP:{round(random.uniform(0.1, 2.0), 1)},MR:{round(random.uniform(0.1, 2.0), 1)},RE:{round(random.uniform(0.1, 2.0), 1)}>#{item_type}\n"
            f"PHY{{{','.join([k+str(v) for k, v in phy.items()])}}}\n"
            f"MAG{{{','.join([k+str(v) for k, v in mag.items()])}}}\n"
            f"HIS{{{','.join([k+str(v) for k, v in his.items()])}}}\n"
            f"LOR{{{','.join([k+str(v) for k, v in lor.items()])}}}\n"
            f"ATTUNE{{{','.join([k+str(v) for k, v in attune.items()])}}}\n"
            f"CHAIN{{USE:{chains['USE']};MAG:{chains['MAG']};ATT:{chains['ATT']}}}\n"
            f"EVO{{P:{evo['P']};M:{evo['M']}}}")

def generate_location_dna():
    """Generates a detailed, multi-line DNA string for a Location/Settlement."""
    size, population, importance = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
    settlement_type = random.choice(["village", "town", "city", "outpost", "port-city", "fortress", "capital", "hamlet", "metropolis"])
    
    struct = {k: random.randint(10, 99) for k in "SDWAFUPQ"}
    pop = {k: random.randint(10, 99) for k in "SDACLHCM"}
    econ = {k: random.randint(10, 99) for k in "MTRPSGIL"}
    pol = {k: random.randint(10, 99) for k in "GCRFSCLI"}
    poi = {k: random.randint(10, 99) for k in "ISRDHAMC"}
    proxi = {k: random.randint(10, 99) for k in ["WILD", "TOWN", "CITY", "RUIN"]}
    
    arch = {'MAT': random.randint(1, 8), 'ROOF': random.randint(1, 8), 'CONST': random.randint(1, 4), 'DECOR': random.randint(1, 6)}
    culture = {'CUSTOM': random.randint(1, 20), 'LAW': random.randint(1, 20), 'PUNISH': random.randint(1, 20), 'CUISINE': random.randint(1, 100)}
    
    chains = {"POP": "D>A>H", "ECON": "R>T>G", "POL": "G>R>S"}
    evo_types = ["STABLE", "RISING", "DECLINING", "FLUCTUATING", "TRANSFORMING", "STAGNANT"]

    evo = {
        'S': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'P': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'I': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}"
    }

    return (f"SETTLEMENT{{v1.1[{size}/{population}/{importance}]}}"
            f"<SP:{round(random.uniform(0.1, 2.0), 1)},PI:{round(random.uniform(0.1, 2.0), 1)},SI:{round(random.uniform(0.1, 2.0), 1)}>#{settlement_type}\n"
            f"STRUCT{{{','.join([k+str(v) for k, v in struct.items()])}}}\n"
            f"POP{{{','.join([k+str(v) for k, v in pop.items()])}}}\n"
            f"ECON{{{','.join([k+str(v) for k, v in econ.items()])}}}\n"
            f"POL{{{','.join([k+str(v) for k, v in pol.items()])}}}\n"
            f"POI{{{','.join([k+str(v) for k, v in poi.items()])}}}\n"
            f"ARCH{{{';'.join([f'{k}:{v}' for k,v in arch.items()])}}}\n"
            f"CULTURE{{{';'.join([f'{k}:{v}' for k,v in culture.items()])}}}\n"
            f"CHAIN{{POP:{chains['POP']};ECON:{chains['ECON']};POL:{chains['POL']}}}\n"
            f"PROXI{{{','.join([k+':'+str(v) for k, v in proxi.items()])}}}\n"
            f"EVO{{S:{evo['S']};P:{evo['P']};I:{evo['I']}}}")

def generate_travel_dna():
    """Generates a simple DNA string for a Travel Scenario."""
    return f"TRAVEL{{{random.randint(1, 5)}-{random.randint(1, 6)}-{random.randint(0, 5)}}}"

def generate_region_dna():
    """Generates a DNA string for a Region in numeric format."""
    region_genes = ["RT", "TF", "CU", "PO", "WA", "EN", "HI", "TH", "IC", "LMK"]
    return ",".join(f"{gene}{random.randint(1, 10)}" for gene in region_genes)

def generate_realm_dna():
    """Generates a DNA string for a political Realm."""
    conf = random.randint(1, 10)
    country_counts = {1: 6, 2: 6, 3: 10, 4: 4, 5: 6, 6: 5, 7: 8, 8: 1, 9: 5, 10: 5}
    num_countries = country_counts.get(conf, 6)
    status = [random.randint(1, 6) for _ in range(num_countries)]
    conflict = random.randint(1, 6)
    return f"REALM[CONF:{conf};STATUS:[{','.join(map(str, status))}];CONFLICT:{conflict}]"

def generate_agency_dna():
    """Generates a DNA string for a Government Agency."""
    agency_type = random.randint(1, 6)
    spec = random.randint(1, 12)
    reputation = random.choice(["Trusted", "Feared", "Incompetent", "Secretive", "Respected", "Corrupt"])
    return f"AGENCY[TYPE:{agency_type};SPEC:{spec};REP:{reputation}]"

def generate_trap_dna():
    """Generates a detailed, multi-line DNA string for a Trap."""
    difficulty, complexity, severity = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
    trap_type = random.choice(["mechanical", "magical", "environmental", "puzzle", "natural", "psychological"])
    
    mods = {
        'D_M': round(random.uniform(0.1, 2.0), 1),
        'C_M': round(random.uniform(0.1, 2.0), 1),
        'T_M': round(random.uniform(0.1, 2.0), 1)
    }

    mech_traits = {"TRG": random.randint(1, 8), "RST": random.randint(1, 5), "DIS": random.randint(1, 6), "BYP": random.randint(1, 7)}
    eff_traits = {"DAM": random.randint(1, 13), "CON": random.randint(1, 13), "DUR": random.randint(1, 7), "TAR": random.randint(1, 6)}
    cont_traits = {"LOC": random.randint(1, 10), "CRE": random.randint(1, 10), "PUR": random.randint(1, 9)}
    
    chains = {"MECH": "TRG>RST>DIS", "EFF": "DAM>CON>DUR", "CONT": "LOC>CRE>PUR"}
    evo_types = ["RISING", "STABLE", "ACCELERATING", "DESCENDING", "FLUCTUATING", "CLIMACTIC"]

    evo = {
        'D': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'E': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}",
        'C': f"{random.choice(evo_types)}{sorted([random.randint(50, 99) for _ in range(4)])}"
    }

    return (f"TRAP{{v1.0[{difficulty}/{complexity}/{severity}]}}"
            f"<D_M:{mods['D_M']},C_M:{mods['C_M']},T_M:{mods['T_M']}>#{trap_type}\n"
            f"MECH{{{';'.join([f'{k}:{v}' for k, v in mech_traits.items()])}}}\n"
            f"EFF{{{';'.join([f'{k}:{v}' for k, v in eff_traits.items()])}}}\n"
            f"CONT{{{';'.join([f'{k}:{v}' for k, v in cont_traits.items()])}}}\n"
            f"CHAIN{{MECH:{chains['MECH']};EFF:{chains['EFF']};CONT:{chains['CONT']}}}\n"
            f"EVO{{D:{evo['D']};E:{evo['E']};C:{evo['C']}}}")

def generate_world_wonder_dna(seed=None, compact=False):
    """Generates a DNA string for a World Wonder."""
    rng = random.Random(seed)
    r = rng.randint
    
    size, age, impact = r(1, 9), r(1, 9), r(1, 9)
    wonder_type = rng.choice(["natural", "structure", "magical", "ruin", "celestial", "living"])

    nature = {"TYP": r(1, 6), "FRM": r(1, 8), "CON": r(1, 6), "VIS": r(1, 4)}
    origin = {"ERA": r(1, 5), "CRT": r(1, 6), "DSC": r(1, 4), "LEG": r(1, 6)}
    effect = {"ENV": r(1, 6), "MAG": r(1, 6), "CUL": r(1, 6), "POL": r(1, 4), "ACC": r(1, 4), "SYNC": r(1, 4)}
    secret = {"KND": r(1, 8), "IMP": r(1, 6), "PRX": r(1, 4), "GDN": r(0, 5)}

    blocks = [
        f"WONDER{{v1.1[{size}/{age}/{impact}]}}#{wonder_type}",
        f"NTR{{{','.join(k+str(v) for k,v in nature.items())}}}",
        f"ORG{{{','.join(k+str(v) for k,v in origin.items())}}}",
        f"EFF{{{','.join(k+str(v) for k,v in effect.items())}}}",
        f"SCR{{{','.join(k+str(v) for k,v in secret.items())}}}"
    ]
    dna = "\n".join(blocks)
    return dna.replace("\n", ";") if compact else dna

def generate_establishment_dna(seed=None, compact=False):
    """Generates a DNA string for an Establishment (Tavern, Shop, etc.)."""
    rng = random.Random(seed)
    r = rng.randint

    atmosphere = {"ATM": r(1, 8), "SND": r(1, 4), "CRO": r(1, 6)}
    offerings = {"GDS": r(1, 6), "SRV": r(1, 6), "LGL": r(1, 4), "CST": r(1, 4)}
    personnel = {"STA": r(1, 6), "OWN": r(1, 6), "CLT": r(1, 6), "POW": r(1, 6)}
    secrets = {"HID": r(1, 6), "SEC": r(1, 6), "TRP": r(0, 5), "BLK": r(1, 4)}
    evolution = {"HIS": r(1, 4), "EVO": r(1, 6), "INT": r(1, 4)}
    chain = {"CH1": r(0, 4), "CH2": r(0, 4), "CH3": r(0, 4)}

    blocks = [
        f"ATMOS{{{','.join(k+str(v) for k,v in atmosphere.items())}}}",
        f"OFFERINGS{{{','.join(k+str(v) for k,v in offerings.items())}}}",
        f"PERSONNEL{{{','.join(k+str(v) for k,v in personnel.items())}}}",
        f"SECRETS{{{','.join(k+str(v) for k,v in secrets.items())}}}",
        f"EVO{{{','.join(k+str(v) for k,v in evolution.items())}}}",
        f"CHAIN{{{','.join(k+str(v) for k,v in chain.items())}}}"
    ]
    dna = "\n".join(blocks)
    return dna.replace("\n", ";") if compact else dna

def generate_regional_poi_dna():
    """Generates an enhanced, detailed DNA string for a Regionally Significant POI."""
    size, complexity, significance = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
    poi_type = random.choice(["dungeon", "ruin", "tower", "anomaly", "landmark", "lair"])

    ntr = {
        "TYP": random.randint(1, 5),    # Nature Type
        "FRM": random.randint(1, 8),    # Form
        "CON": random.randint(1, 6),    # Condition
        "VIS": random.randint(1, 4),    # Visibility
        "MAT": random.randint(1, 8)     # Material
    }
    org = {
        "CRT": random.randint(1, 7),    # Creator
        "AGE": random.randint(1, 4),    # Age
        "PUR": random.randint(1, 8),    # Original Purpose
        "LGC": random.randint(1, 5)     # Legacy
    }
    eff = {
        "ENV": random.randint(1, 6),    # Environmental Effect
        "REP": random.randint(1, 6),    # Reputation
        "ACC": random.randint(1, 4)     # Accessibility
    }
    intr = {
        "INH": random.randint(1, 7),    # Inhabitants
        "THR": random.randint(1, 6),    # Primary Threat
        "TRS": random.randint(1, 6),    # Treasure/Reward
        "IC": random.randint(1, 10)     # Internal Conflict
    }
    sec = {
        "KND": random.randint(1, 6)     # Kind of Secret
    }
    evo = {
        "TRT": random.randint(1, 5),    # Evolving Trait
        "PTN": random.randint(1, 4)     # Pattern
    }

    return (f"REG_POI{{v1.1[{size}/{complexity}/{significance}]}}#{poi_type}\n"
            f"NTR{{{','.join([k+str(v) for k, v in ntr.items()])}}}\n"
            f"ORG{{{','.join([k+str(v) for k, v in org.items()])}}}\n"
            f"EFF{{{','.join([k+str(v) for k, v in eff.items()])}}}\n"
            f"INTR{{{','.join([k+str(v) for k, v in intr.items()])}}}\n"
            f"SEC{{{','.join([k+str(v) for k, v in sec.items()])}}}\n"
            f"EVO{{{','.join([k+str(v) for k, v in evo.items()])}}}")

# --- WORLD GENERATOR CLASS ---

class WorldDNAGenerator:
    """Generates a random World DNA string based on the World DNA Decoding Key v3.2."""
    def __init__(self):
        self.version = "3.2-enhanced"
        self.scales_def = {'T': (1, 10), 'M': (1, 10), 'A': (1, 10), 'R': (2, 5)}
        self.blocks_def = {
            'COSMO': {'CM': (1, 5), 'MD': (1, 5), 'AL': (1, 5), 'FF': (1, 5)},
            'ECON': {'PS': (1, 5), 'WD': (1, 4), 'TN': (1, 4), 'TM': (1, 5)},
            'MAG': {'SRC': (1, 5), 'PRN': (1, 4), 'CST': (1, 5), 'LMT': (1, 5), 'ACQ': (1, 5), 'LAW': (1, 5)},
            'ENV': {'GEO': (1, 7), 'CLM': (1, 5), 'RES': (1, 4), 'ANO': (1, 5)},
            'SOC': {'GOV': (1, 6), 'CLS': (1, 5), 'VAL': (1, 6), 'LIF': (1, 5), 'TEC': (1, 5), 'MAG': (1, 5), 'ART': (1, 5), 'REL': (1, 5), 'FAM': (1, 5), 'GEN': (1, 5), 'MOR': (1, 5), 'LAW': (1, 5)},
            'CON': {'TYP': (1, 5), 'SCL': (1, 4), 'AGE': (1, 3)},
            'HIS': {'EVT': (1, 6), 'KNG': (1, 4), 'LGC': (1, 5)},
            'ORIGIN': {'MAG_SRC': (1, 4), 'MAG_DET': (1, 6), 'MAG_STAT': (1, 8)}
        }
        self.dynamic_blocks_def = {
            'REG': {'TER': (1, 7), 'SOC': (1, 6), 'ECO': (1, 5), 'LMK': (1, 5)},
            'CRIT': {'DOM': (1, 5), 'NAT': (1, 6), 'IMM': (1, 4)},
            'CHAIN': {'TRG': (1, 6), 'ACT': (1, 5), 'CNS': (1, 5)},
            'EVO': {'TRT': (1, 50), 'PTN': (1, 4)},
            'TREND': {'TRT': (1, 50), 'DIR': (1, 3)}
        }

    def _generate_block(self, block_name, definition):
        parts = [f"{gene}:{random.randint(*value_range)}" for gene, value_range in definition.items()]
        return f"{block_name}{{{';'.join(parts)}}}"

    def _generate_factions(self):
        factions = []
        for _ in range(random.randint(2, 4)):
            values = random.sample(range(1, 7), 3)
            highest_value = values[0]
            flaw_map = {1: 1, 2: 6, 3: 2, 4: 4, 5: 3, 6: 5}
            fact = {
                'TY': random.randint(1, 6), 'SC': random.randint(1, 5), 'GL': random.randint(1, 5),
                'VL': f"[{','.join(map(str, values))}]", 'FL': flaw_map.get(highest_value, 1),
                'LM': f"[{','.join(map(str, random.sample(range(1, 6), random.randint(1, 3))))}]"
            }
            factions.append(f"{{{' ; '.join(f'{k}:{v}' for k, v in fact.items())}}}")
        return f"FACT[{','.join(factions)}]"

    def _generate_pantheon(self):
        deities = []
        for _ in range(random.randint(2, 6)):
            deity = {
                'ALIGN': random.randint(1, 10),
                'DOM': f"[{','.join(map(str, random.sample(range(1, 9), random.randint(1, 3))))}]",
                'STATUS': random.randint(1, 20)
            }
            deities.append(f"{{{' ; '.join(f'{k}:{v}' for k, v in deity.items())}}}")
        return f"PANTHEON[{','.join(deities)}]"

    def _generate_shadow_societies(self):
        societies = []
        for _ in range(random.randint(1, 3)):
            society = {
                'TYPE': random.randint(1, 6),
                'SPEC': random.randint(1, 10),
                'GOAL': random.randint(1, 10)
            }
            societies.append(f"{{{' ; '.join(f'{k}:{v}' for k, v in society.items())}}}")
        return f"SHADOW[{','.join(societies)}]"

    def generate_dna(self):
        """Generates and assembles the complete World DNA string."""
        dna_parts = []
        scales = {s: random.randint(*r) for s, r in self.scales_def.items()}
        dna_parts.extend([f"{s}:{v}" for s, v in scales.items()])
        num_regions = scales['R']
        
        for name, defn in self.blocks_def.items():
            dna_parts.append(self._generate_block(name, defn))
        
        dna_parts.append(self._generate_factions())
        dna_parts.append(self._generate_pantheon())
        dna_parts.append(self._generate_shadow_societies())
        
        regions = [self._generate_block('', self.dynamic_blocks_def['REG']) for _ in range(num_regions)]
        dna_parts.append(f"REG[{','.join(regions)}]")
        
        for name in ['CRIT', 'CHAIN', 'EVO', 'TREND']:
            dna_parts.append(self._generate_block(name, self.dynamic_blocks_def[name]))
            
        return " ".join(dna_parts)

# --- MASTER DISPATCHER ---

def generate_dna(generator_type):
    """Master dispatcher function to call the correct generator based on type."""
    generators = {
        "npc": generate_npc_dna,
        "faction": generate_faction_dna,
        "quest": generate_quest_dna,
        "item": generate_item_dna,
        "location": generate_location_dna,
        "travel": generate_travel_dna,
        "region": generate_region_dna,
        "world": WorldDNAGenerator().generate_dna,
        "realm": generate_realm_dna,
        "agency": generate_agency_dna,
        "trap": generate_trap_dna,
        "wonder": generate_world_wonder_dna,
        "establishment": generate_establishment_dna,
        "regional_poi": generate_regional_poi_dna, # New generator
    }
    
    if generator_type in generators:
        return generators[generator_type]()
    else:
        raise ValueError(f"Unknown generator type: '{generator_type}'")

# --- EXAMPLE USAGE ---
if __name__ == '__main__':
    print("--- NPC DNA ---")
    print(generate_dna("npc"))
    print("\n--- Faction DNA ---")
    print(generate_dna("faction"))
    print("\n--- Quest DNA ---")
    print(generate_dna("quest"))
    print("\n--- Regional POI DNA ---")
    print(generate_dna("regional_poi"))
    print("\n--- World DNA ---")
    print(generate_dna("world"))

# Digital Narrative Alchemist: Master Generator System
# Full System Code with all Generators integrated

import random

# --- NPC Generator ---
def generate_npc_dna():
    """Generates a Personality DNA code for an NPC."""
    # LNC (Light/Nuanced Core) Traits: 20 pairs representing nuanced personality facets.
    # A trait is chosen from each pair, assigned a score (1-9) and intensity (1-5).
    lnc_traits = [
        ("B", "C"), ("R", "O"), ("L", "T"), ("F", "I"), ("S", "X"),
        ("P", "M"), ("D", "U"), ("G", "H"), ("Y", "W"), ("E", "A"),
        ("N", "V"), ("K", "Q"), ("Z", "B"), ("O", "P"), ("C", "H"),
        ("R", "L"), ("A", "S"), ("D", "A"), ("A", "H"), ("I", "C")
    ]
    # GNE (General/Noticeable Engine) Traits: 20 traits representing more overt behaviors.
    # Each is assigned a score (1-9).
    gne_traits = [
        "H", "C", "K", "G", "L", "J", "M", "F", "E", "B", "U", "S", "I", "R", "T", "A", "D", "V", "Y", "X"
    ]
    
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
        
    # Calculate average scores for a high-level summary.
    lnc_average = round(sum(lnc_scores) / len(lnc_scores))
    gne_average = round(sum(gne_scores) / len(gne_scores))
    
    # Assemble the final DNA string.
    return f"({lnc_average}/{gne_average}) {','.join(lnc_dna_parts)} - {','.join(gne_dna_parts)}"

# --- Faction Generator ---
def generate_faction_dna():
    """Generates a DNA string for a Faction."""
    # Each key represents a facet of the faction (Type, Goal, Method, etc.).
    # A random value is chosen for each facet.
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
    """Generates a detailed, multi-line DNA string for a Quest."""
    # Core stats
    difficulty = random.randint(1, 9)
    complexity = random.randint(1, 9)
    reward = random.randint(1, 9)
    quest_type = random.choice(["fetch", "rescue", "escort", "eliminate", "explore", "deliver", "investigate", "protect", "infiltrate"])
    
    # Gene blocks with random values
    goal = {k: random.randint(10, 99) for k in "CRESTPLH"}
    obs = {k: random.randint(10, 99) for k in "CMETPSGN"}
    rew = {k: random.randint(10, 99) for k in "MIKRSPLA"}
    narr = {k: random.randint(10, 99) for k in "TCPMHRIA"}
    motiv = {k: random.randint(10, 99) for k in "GRDSPVFJ"}
    engage = {k: random.randint(10, 99) for k in ["COMBAT", "SOCIAL", "EXPLORE", "PUZZLE"]}
    
    # Pre-defined narrative chains and evolution patterns
    chains = {"OBS": "P>M>G", "REWARD": "K>I>A", "MOTIV": "D>J>P"}
    evo_d = sorted([random.randint(50, 99) for _ in range(4)])
    evo_c = sorted([random.randint(50, 99) for _ in range(4)])
    evo_r = sorted([random.randint(50, 99) for _ in range(4)])
    evo_types = ["RISING", "STABLE", "ACCELERATING", "DESCENDING", "FLUCTUATING", "CLIMACTIC"]
    d_type, c_type, r_type = [random.choice(evo_types) for _ in range(3)]
    
    # Assemble the multi-line DNA string
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
    """Generates a detailed, multi-line DNA string for a Magic Item."""
    power_level = random.randint(1, 9)
    magical_complexity = random.randint(1, 9)
    rarity = random.randint(1, 9)
    item_type = random.choice(["weapon", "armor", "wand", "staff", "ring", "amulet", "potion", "scroll", "book", "relic"])
    
    # Gene blocks
    phy = {k: random.randint(10, 99) for k in "MSADCWFT"}
    mag = {k: random.randint(10, 99) for k in "PEDCSART"}
    his = {k: random.randint(10, 99) for k in "OCARLFDS"}
    lor = {k: random.randint(10, 99) for k in "KFNCREIS"}
    attune = {k: random.randint(10, 99) for k in "UWCMSVPR"}
    
    # Chains and evolution
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
    """Generates a detailed, multi-line DNA string for a Location/Settlement."""
    size = random.randint(1, 9)
    population = random.randint(1, 9)
    importance = random.randint(1, 9)
    settlement_type = random.choice(["village", "town", "city", "outpost", "port-city", "fortress", "capital", "hamlet", "metropolis"])
    
    # Gene blocks
    struct = {k: random.randint(10, 99) for k in "SDWAFUPQ"}
    pop = {k: random.randint(10, 99) for k in "SDACLHCM"}
    econ = {k: random.randint(10, 99) for k in "MTRPSGIL"}
    pol = {k: random.randint(10, 99) for k in "GCRFSCLI"}
    poi = {k: random.randint(10, 99) for k in "ISRDHAMC"}
    proxi = {k: random.randint(10, 99) for k in ["WILD", "TOWN", "CITY", "RUIN"]}
    
    # Chains and evolution
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
    """Generates a simple DNA string for a Travel Scenario."""
    return f"TRAVEL{{{random.randint(1,5)}-{random.randint(1,6)}-{random.randint(0,5)}}}"

# --- Region Generator (NEW) ---
def generate_region_dna():
    """Generates a DNA string for a Region in numeric format."""
    region_genes = ["RT", "TF", "CU", "PO", "WA", "EN", "HI", "TH", "IC", "LM"]
    return ",".join(f"{gene}{random.randint(1, 10)}" for gene in region_genes)

# --- World Generator Class ---
class WorldDNAGenerator:
    """Generates a random World DNA string based on the World DNA Decoding Key v3.2."""
    def __init__(self):
        """Initializes the generator with all the possible gene values from the key."""
        self.version = "3.2"
        self.scales_def = {'T': (1,10), 'M': (1,10), 'A': (1,10), 'R': (2,5)}
        self.blocks_def = {
            'COSMO': {'CM': (1,5), 'MD': (1,5), 'AL': (1,5), 'FF': (1,5)},
            'ECON': {'PS': (1,5), 'WD': (1,4), 'TN': (1,4), 'TM': (1,5)},
            'MAG': {'SRC': (1,5), 'PRN': (1,4), 'CST': (1,5), 'LMT': (1,5), 'ACQ': (1,5), 'LAW': (1,5)},
            'ENV': {'GEO': (1,7), 'CLM': (1,5), 'RES': (1,4), 'ANO': (1,5)},
            'SOC': {'GOV': (1,6), 'CLS': (1,5), 'VAL': (1,6), 'LIF': (1,5), 'TEC': (1,5), 'MAG': (1,5), 'ART': (1,5), 'REL': (1,5), 'FAM': (1,5), 'GEN': (1,5), 'MOR': (1,5), 'LAW': (1,5)},
            'CON': {'TYP': (1,5), 'SCL': (1,4), 'AGE': (1,3)},
            'HIS': {'EVT': (1,6), 'KNG': (1,4), 'LGC': (1,5)}
        }
        self.dynamic_blocks_def = {
            'REG': {'TER': (1,7), 'SOC': (1,6), 'ECO': (1,5), 'LMK': (1,5)},
            'CRIT': {'DOM': (1,5), 'NAT': (1,6), 'IMM': (1,4)},
            'CHAIN': {'TRG': (1,6), 'ACT': (1,5), 'CNS': (1,5)},
            'EVO': {'TRT': (1,50), 'PTN': (1,4)},
            'TREND': {'TRT': (1,50), 'DIR': (1,3)}
        }

    def _generate_block(self, block_name, definition):
        """Helper function to generate a single key-value block like 'COSMO{...}'."""
        parts = [f"{gene}:{random.randint(*value_range)}" for gene, value_range in definition.items()]
        return f"{block_name}{{{';'.join(parts)}}}"

    def _generate_factions(self):
        """Generates the FACT block, which is an array of faction objects."""
        factions = []
        for _ in range(random.randint(2, 4)): # Generate 2 to 4 factions
            # Generate unique values for the 'Values' (VL) gene
            values = random.sample(range(1, 7), 3)
            highest_value = values[0]
            # The flaw (FL) is logically derived from the highest value
            flaw_map = {1:1, 2:6, 3:2, 4:4, 5:3, 6:5}
            
            fact = {
                'TY': random.randint(1,6),
                'SC': random.randint(1,5),
                'GL': random.randint(1,5),
                'VL': f"[{','.join(map(str,values))}]",
                'FL': flaw_map.get(highest_value, 1), # Default to 1 if somehow not found
                'LM': f"[{','.join(map(str, random.sample(range(1,6), random.randint(1,3))))}]"
            }
            factions.append(f"{{{' ; '.join(f'{k}:{v}' for k,v in fact.items())}}}")
        return f"FACT[{','.join(factions)}]"

    def generate_dna(self):
        """Generates and assembles the complete World DNA string."""
        dna_parts = []

        # 1. Generate Top-Level Scales robustly.
        scales = {s: random.randint(*r) for s, r in self.scales_def.items()}
        dna_parts.extend([f"{s}:{v}" for s, v in scales.items()])
        num_regions = scales['R']

        # 2. Generate Foundational and State Blocks.
        for name, defn in self.blocks_def.items():
            dna_parts.append(self._generate_block(name, defn))
            
        # 3. Generate Factions Block.
        dna_parts.append(self._generate_factions())
        
        # 4. Generate Dynamic Blocks, including the array of Regions.
        regions = [self._generate_block('', self.dynamic_blocks_def['REG']) for _ in range(num_regions)]
        dna_parts.append(f"REG[{','.join(regions)}]")

        for name in ['CRIT', 'CHAIN', 'EVO', 'TREND']:
            dna_parts.append(self._generate_block(name, self.dynamic_blocks_def[name]))
            
        return " ".join(dna_parts)

# --- Dispatcher ---
def generate_dna(generator_type):
    """
    Master dispatcher function to call the correct generator based on type.
    """
    if generator_type == "npc": return generate_npc_dna()
    elif generator_type == "faction": return generate_faction_dna()
    elif generator_type == "quest": return generate_quest_dna()
    elif generator_type == "item": return generate_item_dna()
    elif generator_type == "location": return generate_location_dna()
    elif generator_type == "travel": return generate_travel_dna()
    elif generator_type == "region": return generate_region_dna()
    elif generator_type == "world": return WorldDNAGenerator().generate_dna()
    else: raise ValueError("Unknown generator type. Valid options: npc, faction, quest, item, location, travel, region, world")

# --- Example Usage ---
# This block will only run when the script is executed directly.
if __name__ == '__main__':
    print("--- NPC DNA ---")
    print(generate_dna("npc"))
    print("\n--- Faction DNA ---")
    print(generate_dna("faction"))
    print("\n--- Quest DNA ---")
    print(generate_dna("quest"))
    print("\n--- Item DNA ---")
    print(generate_dna("item"))
    print("\n--- Location DNA ---")
    print(generate_dna("location"))
    print("\n--- Travel DNA ---")
    print(generate_dna("travel"))
    print("\n--- Region DNA ---")
    print(generate_dna("region"))
    print("\n--- World DNA ---")
    print(generate_dna("world"))

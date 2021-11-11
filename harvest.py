############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []
    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    Casaba = MelonType("cas", 2003,"orange", False,False,"Casaba",)
    Casaba.add_pairing("mint")
    Casaba.add_pairing("strawberry")
    all_melon_types.append(Casaba)

    Crenshaw = MelonType("cren",1996,"orange",False,False,"Crenshaw",)
    Crenshaw.add_pairing("prosciutto")
    all_melon_types.append(Crenshaw)

    yw = MelonType("yw",2013,"orange",False,True,"Yellow Watermelon",)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pair in melon.pairings:
            print(f"- {pair}")
        print("")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    return melon_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self, Melon_Type, shape_rate, color_rate, harvest_from, harvest_by):
        self.melontype = Melon_Type
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.harvest_from = harvest_from
        self.harvest_by = harvest_by
        self.sellable = False

    def is_sellable(self):
        if self.shape_rate > 5 and self.color_rate > 5 and self.harvest_from != 3:
            self.sellable = True
            return True
        else:
            self.sellable = False
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_list = []
    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_list.append(melon_1)
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_list.append(melon_2)
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_list.append(melon_3)
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_list.append(melon_4)
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_list.append(melon_5)
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_list.append(melon_6)
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_list.append(melon_7)
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_list.append(melon_8)
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    melon_list.append(melon_9)
    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellable = "(CAN BE SOLD)"
        if not melon.is_sellable():
            sellable = '(NOT SELLABLE)'

        print(f"Harvested by {melon.harvest_by} from Field {melon.harvest_from} {sellable}")

m = make_melon_types()
print_pairing_info(m)
melons = make_melons(m)
get_sellability_report(melons)

# Further Studies 

def make_melons_txt(melon_types, filename):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_list = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip().split()
            melon = Melon(melons_by_id[line[5]], int(line[1]), int(line[3]), line[-1], line[-4])
            melon_list.append(melon)
        
    return melon_list

melons = make_melons_txt(m, "harvest_log.txt")
get_sellability_report(melons)
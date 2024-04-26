############
# Part 1   #
############


class MelonType: #class name 
    """A species of melon at a melon farm."""
    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller,
    ):
        """Initialize a melon."""
        self.pairings = []
        self.code = code 
        self.name = name 
        self.first_harvest =first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        
         

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's of the Melon type pairings list."""

        self.pairings.append(pairing)

    

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        


def make_melon_types():
    """Returns a list of current melon types."""
    
    all_melon_types = []
    musk = MelonType ("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType ("cas", "Casaba", 2003, "orange", False, False)
    cas.add_pairing("strawberries")
    all_melon_types.append(cas)

    cren = MelonType ("cren", "Crenshaw", 1996, "green", False, False)
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType ("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")
        print("--------------------")
    


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_code = {}
    for melon in melon_types:
        if melon.code not in melons_by_code:
            #adding new entry to the dictionaryn. melon.code is the key and melon is the value
            melons_by_code[melon.code] = melon

    return melons_by_code
        



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, from_field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvester = harvester 

    def is_sellable(self): 
        if self.shape_rating > 5 and self.color_rating > 5 and self.from_field != 3:
            return True
        else: 
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""



    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9
    ]

    return melons



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            is_sellable = "CAN BE SOLD"
        else: 
            is_sellable = "NOT SELLABLE"

        print(f"Harvested by {melon.harvester} from {melon.from_field} ({is_sellable}) ")


#list of current melon type objects stored in variabla "melon_types"
melon_types = make_melon_types()

#list of melon objects stored in variable "melons"
melons = make_melons(melon_types)
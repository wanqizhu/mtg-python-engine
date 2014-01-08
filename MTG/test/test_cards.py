from ..card import Card
from ..card_type import *

def get_basic_land_class(name):
    class BasicLand(Card):
        def __init__(self, owner):
            super.__init__(self, owner)
            self.name = name
            self.types = {CardType.LAND}
            self.supertypes = {Supertype.BASIC}
            self.subtypes = [name]
    return BasicLand
    
Plains = get_basic_land_class("Plains")
Island = get_basic_land_class("Island")
Swamp = get_basic_land_class("Swamp")
Mountain = get_basic_land_class("Mountain")
Forest = get_basic_land_class("Forest")

BASIC_LANDS = (Plains, Island, Swamp, Mountain, Forest)
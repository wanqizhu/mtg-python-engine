from ..player import Player

class TestPlayer(Player):
    def choose_action(self, game):
        if self.hand and self.can_play_land():
            print("Your hand is:", str(self.hand))
            print("Your permanents are:", str(self.permanents))
            index = self.choose_hand_card()
            return self.play_card(index)
    
    def choose_mulligan(self):
        return False
        
    def declare_attackers(self):
        return {}
    
    def declare_blockers(self):
        return {}
        
    def choose_hand_card(self):
        index = -1
        while not (0 < index <= len(self.hand)):
            index = int(raw_input("Choose hand index from 0 to {}:".format(self.hand)))
        return index
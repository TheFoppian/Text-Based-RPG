import main
from utils import *

class Item:
    def __init__(self, oneTime=True, key=False):
        self.oneTime = oneTime
        self.key = False
        self.msg = ""
    
    def use(self):
        print("Unusable item. Please report to developer and he'll try to get it fixed :).")
        pass
    
    def get(self):
        p(self.msg)
        main.player.inventory.append(self)

class GuildCard(Item):
    def __init__(self):
        super().__init__(False, True)
        self.msg = "It's a guild card. You can use it to check your status."
    
    def use(self):
        main.player.dispStats()
    
    
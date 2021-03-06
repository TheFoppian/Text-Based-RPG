import utils
import playa
import random

class Enemy:
    def __init__(self, hp, mp, sp, spd, defse, atk, typ, accur, exp, name="enemy_01"):
        self.hp = hp
        self.mp = mp
        self.sp = sp
        self.spd = spd
        self.defse = defse
        self.atk = atk #generally between 10 and 100 based on difficulty
        self.typ = typ #1 - fight, 2 - magic
        self.accur = accur #MAX 256
        self.name = name
        self.exp = exp
    
    def attack(self, turn):
        agi = random.randint(1, 50)
        temptype = self.typ
        '''if agi > 49:
            if self.typ == 1:
                temptype = 2
            else:
                temptype = 1'''
        
        if temptype == 1:
            move = random.randint(1, 5)
            if self.sp >= 10 and move > 3:
                accur = random.randint(0, 256)
                utils.p("The %s attempts to strike you with a powerful blow!" % self.name)
                if accur < self.accur:
                    damage = (self.atk + 1) * random.randint(1, round(self.atk / 4))
                    playa.player.hp -= damage
                    utils.p("It hits you for %s damage!" %damage)
                else:
                    utils.p("It strikes the air next to you instead!")
                self.sp -= 10
                turn = 1

            else:
                accur = random.randint(0, 256)
                utils.p("The %s attempts to hit you!" %self.name)
                if accur < self.accur:
                    damage = (self.atk + 1)
                    playa.player.hp -= (self.atk + 1)
                    utils.p("It hits you for %s damage" %damage)
                else:
                    utils.p("It strikes the air next to you instead!")
                turn = 1
        '''elif temptype == 2:
            move = random.randint(1, 5)
            if self.sp > 0 and move > 3:
                accur = random.randint(0, 256)
                if accur < self.accur:
                    playa.player.hp -= (self.atk + 1) * random.randint(round(self.atk / 4))
                self.sp -= 10
                turn = 1
            else:
                accur = random.randint(0, 256)
                if accur < self.accur:
                    playa.player.hp -= (self.atk + 1)
                turn = 1'''
            

class Zombie(Enemy):
    def __init__(self):
        super().__init__(50, 10, 50, 3, 5, 15, 1, 125, 25, "Zombie")
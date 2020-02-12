class Person:

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class Monk(Person):

    def __init__(self, hasCrane, name):
        self.name = name
        self.crane = {
            "name": "Crane",
            "cooldown": 180,
            "status": 0, 
            "hasSpell": hasCrane, 
            "talentCooldown": False, 
            "type": "aoe",
            "owner": self
        }
        self.revival = {
            "name": "Revival",
            "cooldown": 180,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.cocoon = {
            "name": "Cocoon",
            "cooldown": 120,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "single",
            "owner": self
        }
        self.spellList = [self.crane, self.revival, self.cocoon]
        super().__init__(name)

class Druid(Person):
    def __init__(self, hasTree, hasShortTranq, hasFlourish, name):
        self.name = name
        self.tree = {
            "name": "Tree",
            "cooldown": 180,
            "status": 0,
            "hasSpell": hasTree,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.tranq = {
            "name": "Tranquility",
            "cooldown": 180,
            "status": 0,
            "hasSpell": hasTree,
            "talentCooldown": hasShortTranq,
            "shortCooldown": 120,
            "type": "aoe",
            "owner": self
        }
        self.flourish = {
            "name": "Flourish",
            "cooldown": 90,
            "status": 0,
            "hasSpell": hasFlourish,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.spellList = [self.tree, self.tranq, self.flourish]
        super().__init__(name)

class Priest(Person):
    def __init__(self, hasTalent, name, spec):
        self.name = name
        self.painSup = {
            "name": "Pain Suppression",
            "cooldown": 120,
            "status": 0, 
            "hasSpell": True, 
            "talentCooldown": False, 
            "type": "single",
            "owner": self
        }
        self.evangelism = {
            "name": "Evangelism",
            "cooldown": 90,
            "status": 0,
            "hasSpell": hasTalent,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.pwBarrier = {
            "name": "Power Word: Barrier",
            "cooldown": 180,
            "status": 0,
            "hasSpell": hasTalent,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.lumBarrier = {
            "name": "Luminous Barrier",
            "cooldown": 180,
            "status": 0,
            "hasSpell": not hasTalent,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.hymn = {
            "name": "Divine Hymn",
            "cooldown": 180,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.guardianSpirit = {
            "name": "Guardian Spirit",
            "cooldown": 180,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "single",
            "owner": self
        }
        self.salv = {
            "name": "Holy Word Salvation",
            "cooldown": 360,
            "status": 0,
            "hasSpell": hasTalent,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        if spec == "disc":
            self.spellList = [self.painSup, self.evangelism, self.pwBarrier, self.lumBarrier]
        if spec == "holy":
            self.spellList = [self.hymn, self.guardianSpirit, self.salv]
        super().__init__(name)

class Shaman(Person):
    def __init__(self, hasTotem, hasAscend, name):
        self.name = name
        self.tide = {
            "name": "Healing Tide Totem",
            "cooldown": 180,
            "status": 0, 
            "hasSpell": True, 
            "talentCooldown": False, 
            "type": "aoe",
            "owner": self
        }
        self.link = {
            "name": "Spirit Link Totem",
            "cooldown": 180,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.earthenWall = {
            "name": "Earthen Wall Totem",
            "cooldown": 60,
            "status": 0,
            "hasSpell": hasTotem,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.ascendance = {
            "name": "Ascendance",
            "cooldown": 180,
            "status": 0,
            "hasSpell": hasAscend,
            "talentCooldown": False,
            "type": "aoe",
            "owner": self
        }
        self.spellList = [self.tide, self.link, self.earthenWall, self.ascendance]
        super().__init__(name)

class Paladin(Person):
    def __init__(self, hasAvenger, name):
        self.auraMastery = {
            "name": "Aura Mastery",
            "cooldown": 180,
            "status": 0, 
            "hasSpell": True, 
            "talentCooldown": False, 
            "type": "aoe",
            "owner": self
        }     
        self.loh = {
            "name": "Lay on Hands",
            "cooldown": 600,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "single",
            "owner": self
        }
        self.wings = {
            "name": "Avenging Wrath",
            "cooldown": 120,
            "status": 0,
            "hasSpell": True,
            "talentCooldown": False,
            "type": "single",
            "owner": self
        }
        self.avenger = {
            "name": "Holy Avenger",
            "cooldown": 120,
            "status": 0,
            "hasSpell": hasAvenger,
            "talentCooldown": False,
            "type": "single",
            "owner": self
        }
        self.spellList = [self.auraMastery, self.loh, self.wings, self.avenger]
        super().__init__(name)

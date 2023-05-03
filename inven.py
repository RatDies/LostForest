class objects():
  
class Rock(Objects):
    def __init__(self):
        self.name = "ROCK"
        self.description = """
                            This is just a ROCK
                           """


class Weapon():
    """Weapon Class to raise errors and return the weapon's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{} (+ {} Damage)".format(self.name, self.damage)

class RustedShortSword(Weapon):
    def __init__(self):
        self.name = "Rusted Short Sword"
        self.description = """
                            Practically usleless weapon, but it's all you got.
                           """
        self.damage = 2


class KeyItems():

class Key(KeyItems):
  def __init__(self):
        self.name = "Key"
        self.description = """
                            Should give you access to the multitude of locked treasure chests around this place.
                           """
  
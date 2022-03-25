# Could be used in a game where living and undead versions of characters are very distinct
# VScode

class AbstractCharFactoryFactory:
    def get_factory(living: bool):
        if living:
            return LivingCharFactory()
        else:
            return UndeadCharFactory()

class AbstractCharFactory:
    def get_char(self, get_char: str):
        pass

class UndeadCharFactory(AbstractCharFactory):
    def get_char(self, get_char: str):
        if get_char == "dog":
            return UndeadDog()
        elif get_char == "human":
            return UndeadHuman()
        return None

class LivingCharFactory(AbstractCharFactory):
    def get_char(self, get_char: str):
        if get_char == "dog":
            return LivingDog()
        elif get_char == "human":
            return LivingHuman()
        return None

class Character:
    def attack(self) -> None:
        pass

class LivingHuman(Character):
    def attack(self):
        print("Living Human attacks")

class UndeadHuman(Character):
    def attack(self):
        print("Undead Human attacks")

class LivingDog(Character):
    def attack(self):
        print("Living Dog attacks")

class UndeadDog(Character):
    def attack(self):
        print("Undead Dog attacks")


factory = AbstractCharFactoryFactory.get_factory(False)

char = factory.get_char("dog")

char.attack()

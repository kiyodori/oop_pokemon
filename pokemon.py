# pokemon.py
class Pokemon:
    def __init__(self, name, hp, atk):
        self._name = name
        self._hp = hp
        self._max_hp = hp * 2
        self._atk = atk

    def attack(self, target):
        target.hp -= self._atk
        print(f'{self._name}のこうげき！', end='')
        self.attack_message(target)

    def attack_message(self, target):
        pass

    def is_fainted(self):
        return self._hp <= 0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = value

    @property
    def name(self):
        return self._name

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('ピカチュウ', 20, 10)

    def attack_message(self, target):
        print(f'10万ボルト！{target.name}は{self._atk}ダメージをもらった。{target.name}のHPは{target.hp}だ。')

class Hitokage(Pokemon):
    def __init__(self):
        super().__init__('ヒトカゲ', 18, 5)

    def attack_message(self, target):
        print(f'ひのこ！{target.name}は{self._atk}ダメージをもらった。{target.name}のHPは{target.hp}だ。')

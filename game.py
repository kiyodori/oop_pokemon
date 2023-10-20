# game.py
class Game:
    def __init__(self, pokemon1, pokemon2):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2

    def battle(self):
        self._start()
        winner, loser = self._attack()
        self._show_result(winner, loser)

    def _start(self):
        print(f'{self._pokemon1.name}があらわれた。{self._pokemon1.name}のHPは{self._pokemon1.hp}だ。')
        print(f'{self._pokemon2.name}があらわれた。{self._pokemon2.name}のHPは{self._pokemon2.hp}だ。')

    def _attack(self):
        while True:
            self._pokemon1.attack(self._pokemon2)
            if self._pokemon2.is_fainted():
                return (self._pokemon1, self._pokemon2)

            self._pokemon2.attack(self._pokemon1)
            if self._pokemon1.is_fainted():
                return (self._pokemon2, self._pokemon1)

    def _show_result(self, winner, loser):
        print(f'{loser.name}はたおれた。{winner.name}のかち！')

def main():
    pikachu = 'ピカチュウ'
    hitokage = 'ヒトカゲ'
    hp_pikachu = 20
    hp_hitokage = 18

    print(f'{pikachu}があらわれた。{pikachu}のHPは{hp_pikachu}だ。')
    print(f'{hitokage}があらわれた。{hitokage}のHPは{hp_hitokage}だ。')

    while True:
        hp_hitokage = attack_pikachu(hitokage, hp_hitokage)
        if check_fainted(hp_hitokage):
            print(f'{hitokage}はたおれた。{pikachu}のかち！')
            break

        hp_pikachu = attack_hitokage(pikachu, hp_pikachu)
        if check_fainted(hp_pikachu):
            print(f'{pikachu}はたおれた。{hitokage}のかち！')
            break

def attack_pikachu(pokemon, hp):
    if hp - 10 > 0:
        hp = hp - 10
    else:
        hp = 0

    print(f'ピカチュウのこうげき！10万ボルト！{pokemon}は10ダメージをもらった。{pokemon}のHPは{hp}だ。')
    return hp

def attack_hitokage(pokemon, hp):
    if hp - 5 > 0:
        hp = hp - 5
    else:
        hp = 0

    print(f'ヒトカゲのこうげき！ひのこ！{pokemon}は5ダメージをもらった。{pokemon}のHPは{hp}だ。')
    return hp

def check_fainted(hp):
    if hp <= 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

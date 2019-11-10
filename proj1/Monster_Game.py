#player_name = 'Marco'
#player_attack = 10
#player_heal = 16
#health = 100

#player = ['Marco',10,16,100] List
from random import randint

def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

def game_ends(winner_name):
    print(f'{winner_name} Won the Game')

game_running = True
game_results = []

while game_running == True:
    counter = 0
    player = {'name': 'Marco', 'attack': 15, 'heal': 20, 'health': 100}  # Dictionary
    monster = {'name': 'Monster', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter The Players name')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    new_round = True
    while new_round == True:
        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select an option')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit')
        print('4) Print Results')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for player_stat in game_results:
                print(player_stat)


        else:
            print('Invalid Selection')
        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': monster['name'], 'health': monster['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False





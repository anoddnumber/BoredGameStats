import random

possible_lunch_places = [
    '8 ounce',
    'Santouka',
    'Taco Chukis',
    'Kedai Makan',
    'Swish Swish',
    'Boiling Point',
    'Portage Bay',
    '''Zeek's Pizza''',
    'Lola',
    'Cheesecake Factory',
    'Cedars',
    'Jon\'s Fried Rice',
    'Tofu House',
    'Din Tai Fung',
    'Pho',
    'Ba Bar',
    'Red Robin',
    'Udon',
    'Hard Wok',
    'Hong Kong Bistro',
    'Little Fat Sheep',
    'Issian',
    'Musashis',
    'Facing East',
    'Dough Zone',
    'KBBQ at UW on the ave (Palmi KBBQ)',
    'Zen Noodle',
    'Ezell\'s',
    '45th Stop and Shop (poke)',
    'Suika',
    'Chik-fil-a',
    'Kizuki Ramen',
    'Instant Ramen + Movie',
    'Serious Pie and Biscuit',
    'Xi\' an Noodles'
]


def getRestaurant(possible_restaurants):
    user_input = 'n'

    while (user_input == 'n' or user_input == 'no') and len(possible_restaurants) != 0:
        random_index = random.randint(0, len(possible_restaurants) - 1)
        lunch_place = possible_restaurants[random_index]

        print(lunch_place + "?")
        print("y/n?")
        user_input = input()

        if user_input == 'n' or user_input == 'no':
            print('removing ' + lunch_place + ' as a choice')
            possible_restaurants.pop(random_index)
            print
            print('remaining options: ' + str(possible_restaurants))
            print('number of remaining options: ' + str(len(possible_lunch_places)))
        else:
            print('\nYou chose ' + lunch_place)


getRestaurant(possible_lunch_places)
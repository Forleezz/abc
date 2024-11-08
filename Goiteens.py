# for i in range(1, 1000001):
#             if i %2:
#              print(i)
#
# for i in 'Lviv':
#     print(i)

# for i in (3, 8, 2):
#     print(i)

# name = 'Elisey'
# for i in name:
#     if i == 's':
#         break
#     print(i)

#
# i = 0
# suma = 0
# counter = 0
# while i < 20:
#     if i % 2:
#         counter += 1
#     print(i)
#     i += 1
#
# print(counter,'count')

# word = input("Введіть рядок: ")
# word = [0]
# first_letter = 0
# while True:
#     first_letter += 1
#     continue
# print(count)


# word = input("Введіть рядок: ")
# first_letter = 0
# count = 0
# char = first_letter
# while char is True:
#    if char == first_letter:
#        count += 1
# print("Кількість повторювання першої летері:", count)



# word = list('Hello')
# print(word)

# word = ('aaa,bbb,ccc,ddd,eee')
# print(word[4])


# word = input('Write a word: ')
# counter = 0
# while True:
#     counter += 1
#     print(counter,'count')

# word=input('Enter a word: ')
# count=0
# for count in word:
#     if count == word[0]:
#      count += 1
# print(count)

# nums = [5, 2, 3, 4, 2]
# max_num = nums[0]
# for i in nums:
#     if i > max_num:
#         max_num = i
# print(max_num)

# nums = [2, 3, 4, 5, 9]
# suma = 0
# for i in nums:
#  suma += i
# print(suma)

#
# continents = ['Europe', 'Asie', 'Africa', 'Nord America', 'Sud America', 'Australia', 'Antarctica']
# print(min(continents(str([0],[1],[2][3],[4],[5],[6],))))

# cityes = ['Kyiv'],['Odessa'],['Lviv']
# print(len(cityes))

# city_1 =('Kyiv')
# city_2 =('Odessa')
# city_3 =('Lviv')
# print(len(city_1))
# print(len(city_2))
# print(len(city_3))

# side_1 = 13
# side_2 = 5
# area = side_1 * side_2
# print(area)

# suma = 0
# for i in range(1, 101):
#         suma +=(i)
# print(suma)


# names = ('Andriy, Sergei, Maksim, Andriy ')
# count = str(0)
# for count in names:
#     if count == names[0]:
#      count += str(1)
# print(count)

# items = ['qwerty', 101, True, 'hello', 'bye', None]
# print[0],[3],[4]

# colors = ['red', 'green', 'white', 'yellow', 'red', 'green', 'white', 'black']
# colors.pop(4)
# colors.pop(5)
# colors.pop(3)
# print(colors)

# colors = ['red', 'green', 'white', 'yellow','red', 'green', 'white', 'black']
# colors.pop(4)
# colors.pop(5)
# colors.pop(-2)
# print(colors)

# colors = ['red', 'green', 'white', 'yellow','red', 'green', 'white', 'black']
# colors.pop(1)
# colors.pop(2)
# colors.pop(4)
# print(colors)


# Western_Hemisphere = ['Nord America, Sud America']
# Western_Hemisphere.append('Europe, Asia, Africa')
# Western_Hemisphere.sort()
# print(Western_Hemisphere)

# alph = 'abcdefghijklm'
# word = 'hello'
# counter = 0
# for i in word:
#     if i not in alph:
#       counter +=1
# print('Кількість букв', counter)

# words = ['hello', 'bye', 'qwerty', 'hi']
# new_list = 0
# for i in words:
#     print(new_list)
#
# array = ['a', 'b', 'c', 'f', 'd', 'l', 'e', 'f', 'p', 'g', 'h', 'h', 'i', 'j', 'k', 'l', 'f', 'm', 'n', 'o', 'p', 'a']
# unique_list = []
# counter = 0
# for i in array:
#     if array.count(i) == 1:
#         counter += 1
# unique_list.extend(array)
# print(f"{counter} unique elements in this list. Here they are: \n", unique_list)
#
# western_hemisphere = ['Nord America, Sud America']
# eastern_hemisphere = ['Europe, Asia, Africa']
# western_hemisphere.extend(eastern_hemisphere)
# western_hemisphere.sort()
# print(western_hemisphere)

# my_cars = []
# while True:
#     car = input('Enter your car brand : ')
#     if car == 'quit':
#         break
#     my_cars.append(str(car))
#     print(my_cars)
# for i in range(len(my_cars)):
#     print(i+1, my_cars[i])
# while True:
#     cars_to_delete = input('Enter a number of car to delete it')
#     if cars_to_delete == 'quit':
#         break
#     del my_cars[int(cars_to_delete)-1]
# for i in range(len(my_cars)):
#     print(i + 1, my_cars[i])

# my_tasks = []
# while True:
#     option = input('''Enter your option
# a -  to add new task
# d - to delete a task
# r - to show all tasks
# quit - to cancel all
# : ''')
#     if option == 'quit':
#         break
#     elif option == 'a':
#         task = input('Enter your task:')
#         my_tasks.append(task)
#         print('You have added your task successfully')
#     elif option == 'd':
#         task_to_delete = input('Enter number of task to delete it: r')
#         del my_tasks[int(task_to_delete)-1]
#         print('You have removed your task successfully')
#     elif option == 'r':
#         print('All your tasks')
#         for i in range(len(my_tasks)):
#             print(i+1, my_tasks[i])
# print(my_tasks)

# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)


# while True:
#     print('''Select an option:"
# 1. Greeting
# 2. Entrance''')
#     choice = input("Enter a number of option: ")
#     if choice == "1":
#         print("Hello, How are you?")
#     elif choice == "2":
#         print("Good Bye!")
#         break
#     else:
#         print("Wrong choice. Try again.")

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'Привіт, світ!'
#
# @app.route('/about')
# def about():
#     return 'Це сторінка "Про нас".'
#
# if __name__ == '__main__':
#     app.run(debug=True)

# import time
# start_time= time.time()
# def fun():
#     a=2
#     b=3
#     c=a+b
# end_time= time.time()
# fun()
# timetaken = end_time - start_time
# print("Your program takes: ", timetaken) # 0.0345


# word =  ('Hello')
# new_word = word.upper()
# print(new_word)
#
# age = (52)
# print(int(age)+5)


# word = ('Hello')
# print(word[4])

# word = ('Hello')
# print(word[:5])


# my_name = ('Elisey')
# print(my_name[:3:2])

# sentence = 'lorem ipsum dolor'
# print(sentence[::-1])
#
# print(r'Elisey\nMelnichuk')
# number = 1,2,3,4,5,6,7,8,9
# sentence = ('123abc456def')
# for number in sentence:
#     if not number:
#         del number
# print(sentence)

# word = 'abc123'
# char_list = list(word)
# for i in range(len(char_list) - 1, -1, -1):
#     if char_list[i].isdigit():
#         del char_list[i]
# new_word = ''.join(char_list)
# print(new_word)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_of_unpair_numbers = sum(num for num in numbers if num % 2 != 0)
# print('The sum of odd numbers:', sum_of_unpair_numbers)

# text = input('Введіть декілька речень тексту: ')
# total_chars = len(text)
# words = text.split()
# total_words = len(words)
# sentences = text.split('.')
# total_sentences = len([s for s in sentences if s.strip() != ''])
# unique_words = set(word.lower() for word in words)
# total_unique_words = len(unique_words)
# print('Загальна кількість символів (включаючи пробіли):', total_chars)
# print('Кількість слів:', total_words)
# print('Кількість речень:', total_sentences)
# print('Загальна кількість унікальних слів:', total_unique_words)
# print('Список унікальних слів:', unique_words)

# import random
#
# def guess_the_number():
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
#     print("Я загадав число від 1 до 100. Спробуй вгадати!")
#
#     while True:
#         guess = input("Введи своє число: ")
#         attempts += 1
#         if attempts >= 10:
#             print('Нажаль ти невгадав число спробуй заново')
#             break
#
#         if not guess.isdigit():
#             print("Будь ласка, введи число.")
#             continue
#
#         guess = int(guess)
#
#         if guess < number_to_guess:
#             print("Загадане число більше.")
#         elif guess > number_to_guess:
#             print("Загадане число менше.")
#         else:
#             print(f"Вітаю! Ти вгадав число за {attempts} спроб.")
#             break
#
# guess_the_number()

#
# last_name = ('Melnichuk')
# letter = ('a, b, c , d ,e , f, g, h, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z')
# counter = [0]
# if letter == last_name:
#     counter += 1
# print(counter)

# word = 'abracadbra'
# result = ''
# for i in word:
#     if i == 'a':
# print(word.upper)
''
# s = 'I am learning strings in Python. Some new methods got now.'
# for i in s.split:
#     print(i)

# last_name = ('Melnichuk')
# letter = ('a, b, c , d ,e , f, g, h, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z')
# counter = [0]
# if letter == last_name:
#     counter += 1
# print(counter)

# num = ('5')
# print(num.isdigit())
#
# sentence = ('Hello world')
# print(sentence.isalpha()


# word = 'qwe1asd2zxc36'
# num_counter = 0
# letter_counter = 0
# for i in word:
#     if i.isdigit():
#         num_counter += 1
#     elif i.isalpha():
#         letter_counter += 1
# print(num_counter, 'letters', letter_counter, 'numbers')


# s = 'Boat Rudder Mast Boat Hull'
# upper_counter = 0
# lower_counter = 0
# for i in s:
#     if i.isupper():
#         upper_counter += 1
#     elif i.islower():
#         lower_counter += 1
# if upper_counter < lower_counter:
#     print(lower_counter)
# else:
#     print(upper_counter)

# text = ('Melnichuk')
# letter = ('m, e, l, n, i, c, h, u, k')
# letter_counter = 0
# for letter in text:
#     if letter.isalpha():
#         letter_counter += 1
# most_common_letter = max(str(letter_counter))
# print(most_common_letter)

# text = 'Melnichuk'
# letter_counter = 0
# for letter in text:
#     if letter.isalpha():
#         letter_counter += 1
# most_common_letter = max(str(letter_counter))
# print(most_common_letter)

# word = ("HeLLo WoRLD")
# swapped_word = word.swapcase()
# print(swapped_word)

# nums = [5, 100, 200]
# result = ''
# for num in nums:
#     result += str(num)
# print(result)


# students = [['Андрій', 'Максим'],['Андрій', 'Сергій'],['Андрій', 'Марк'],['Руслан', 'Іван']]
# counter = 0
# for student in students:
#     if student[0] == 'Андрій':
#         counter += 1
# print(counter)

# num_list = 1, 2, 3, 4, 5
# nums_list= [num ** 2 for num in num_list]
# print(nums_list)

# sentence = ('Hello world')
# words = sentence.split()
# longest_word = max(str(words))
# print('Longest word:',sentence)

# names_list = ['Oksana, Gleb, Artem, Katya, Maksim, Gleb, Katya']
# unique_set = set(names_list)
# print('Unique names:', unique_set)

# names_list = ['Oksana, Gleb, Artem, Katya, Maksim, Gleb, Katya']
# unique_names = ''
# for name in names_list:
#     if name not in unique_names:
#         unique_names += name
#     else: del name
# print('Unique names:', unique_names)

# numbers_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
# min_value = min(numbers_set)
# max_value = max(numbers_set)
# print("Сума мінімального та максимального значення:",numbers_set)

# num = [5, 1, 3, 4, 10, 1, 2, 7, 7]
# nums = [5, 1, 1, 3, 4, 10, 10, 1, 2, 7, 7]
# num.remove(min(num))
# num.remove(max(nums))
# nums.remove(min(nums))
# nums.remove(max(nums))
# print(sum(nums))
# print(sum(num))



# lst = ['qwq', 'hello', 'bye', 'abba', 'ewe']
# new_list = ''
# for i in lst:
#     if i[:-3]:
#         new_list += (i)
# print(new_list)

# numbers = [111, 141, 223, 755, 919, 333]
# for i in numbers:
#     if str(i) == str(i)[::-1]:
#         print(i)

# a = 'hello world world hi bye hello'
# new_a = ''
# for i in a:
#     if a.count(i) > 1:
#         new_a += i
#         print(i)

# a = 'qwertyavnbqon'
# vowels = 'aeiou'
# first = ''
# last = ''
# for i in a:
#     if str(i) == str(i)[::-1]:
#         print(i)

# a = 1
# b = 100
# start = min(a, b)
# end = max(a, b)
# total_sum = sum(range(start, end + 1))
# print(total_sum)

# string = 'zx c ab'
# string2 = ''.join(sorted(string.replace(' ', '')))
# print(string2)

# word = 'alibaba'
# separated_word = ' '.join(word)
# word3 = ''.replace('a', '$')
# print(separated_word)

# str1 = 'abc'
# str2 = 'string'
# if(str1[-3:] == 'ing'):
#     str2 = str2 + 'ly'
# else:
#     str1 = str1 + 'ing'
#     print(str1)
# if (str2[-3:] == 'ly'):
#     str1 = str1 + 'ing'
# else:str2 = str2 + 'ly'
# print(str2)

# lst = ['Hello, what is your name?']
# for i in lst:
#     list

# names_list = [('Oksana '), ('Gleb '), ('Artem '), ('Katya '), ('Maksim '), ('Gleb '), ('Katya ')]
# unique_names = ''
# for name in names_list:
#     if name not in unique_names:
#         unique_names += name
#     else: del name
# print('Unique names:', unique_names)

# lst = ['Hello, what is your name?']
# sentence = lst[0]
# words = sentence.split()
# longest_word = words[0]
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)
# colors = {
#     "червоний": (255, 0, 0),
#     "зелений": (0, 255, 0),
#     "синій": (0, 0, 255),
#     "жовтий": (255, 255, 0),
#     "чорний": (0, 0, 0),
#     "білий": (255, 255, 255)
# }
#
# # Запит у користувача назви кольору
# color_name = input("Введіть назву кольору: ").strip().lower()
#
# # Виведення RGB коду або повідомлення "Колір не знайдено"
# if color_name in colors:
#     print(f"RGB код кольору {color_name}: {colors[color_name]}")
# else:
#     print("Колір не знайдено")

# names_list = [('Oksana '), ('Gleb '), ('Artem '), ('Katya '), ('Maksim '), ('Gleb '), ('Katya ')]
# unique_names = list(set(names_list))
# print(unique_names)

# country = {'Ukraine': 'Kiev', 'French': 'Paris'}
# country.update({'America': 'Washington'})
# country['Ukraine'] = country['Ukraine'].upper()
# country['French'] = country['French'].upper()
# country['America'] = country['America'].swapcase()
# print(country)

# cities = {'Kyiv': 2000000, 'Paris': 3000000}
# cities['Kyiv'] += 800
# print(cities)
#
# lst = {'Oleg': 'red', 'Katya': 'bleu'}
# lst['Oleg'] = 'yellow'
# print(lst)
#
# lst = ['hello' 'world' 'car' 'student']
# sentence = lst[0]
# words = sentence.split()
# longest_word = words[0]
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)

# lst = {'name': 'Андрій', 'age': 19, 'city': 'Львів'}
# lst['location'] = lst.pop('city')
# print(lst)

# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV': 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA': 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
# }
#
# transport
# 'II7777AA' - 'Петренко Петро'
# 'АІ1234НН' - 'Іванов Олексій'

# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV': 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA': 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
# }


# stock = {'laptop': 3, 'smartphone': 5, 'mouse': 2, 'keyboard': 1}
# user_item = 'laptop'
# user_quantity = 2
# if stock.value() <= 2:
#     user_item += stock

# dct = {
#     'Kiev': [10],
#     'Odessa': [16],
#     'Lviv': [12],
#     'Kharkiv': [9]
# }
# result = ({sum(dct.values()) / len(dct.values())})
# print(result)


# import random
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.attack = 10
#         self.inventory = []
#
#     def is_alive(self):
#         return self.health > 0
#
#     def attack_enemy(self, enemy):
#         damage = random.randint(1, self.attack)
#         enemy.health -= damage
#         print(f"{self.name} атакует {enemy.name} на {damage} урона!")
#
#
# class Enemy:
#     def __init__(self, name, health, attack):
#         self.name = name
#         self.health = health
#         self.attack = attack
#
#     def is_alive(self):
#         return self.health > 0
#
#
# def encounter_enemy(player):
#     enemies = [
#         Enemy("Гоблин", 30, 5),
#         Enemy("Скелет", 50, 7),
#         Enemy("Дракон", 80, 12)
#     ]
#     enemy = random.choice(enemies)
#     print(f"Вы встретили {enemy.name}!")
#
#     while player.is_alive() and enemy.is_alive():
#         player.attack_enemy(enemy)
#         if enemy.is_alive():
#             enemy_damage = random.randint(1, enemy.attack)
#             player.health -= enemy_damage
#             print(f"{enemy.name} атакует {player.name} на {enemy_damage} урона!")
#
#         print(f"{player.name}: {player.health} HP, {enemy.name}: {enemy.health} HP")
#
#     if player.is_alive():
#         print(f"{enemy.name} повержен!")
#         loot = random.choice(["золото", "зелье", "доспехи"])
#         print(f"Вы нашли {loot}!")
#         player.inventory.append(loot)
#     else:
#         print(f"{player.name} был побежден...")
#
#
# def main():
#     print("Добро пожаловать в игру 'Подземелье'!")
#     player_name = input("Введите имя вашего персонажа: ")
#     player = Player(player_name)
#
#     while player.is_alive():
#         action = input(
#             "Вы хотите исследовать подземелье или выйти? (введите 'исследовать' или 'выйти'): ").strip().lower()
#         if action == "да":
#             encounter_enemy(player)
#         elif action == "нет":
#             print("Спасибо за игру!")
#             break
#         else:
#             print("Неверный ввод. Пожалуйста, введите 'исследовать' или 'выйти'.")
#
#     if not player.is_alive():
#         print("Конец игры.")
#
#
# if __name__ == "__main__":
#     main()
#
#

# from tkinter import *
# import random
#
#
# class Game:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Избегай препятствий")
#
#         self.canvas = Canvas(master, width=400, height=600, bg="white")
#         self.canvas.pack()
#
#         self.player = self.canvas.create_rectangle(180, 550, 220, 580, fill="blue")
#         self.obstacles = []
#
#         self.score = 0
#         self.game_over = False
#
#         self.master.bind("<Left>", self.move_left)
#         self.master.bind("<Right>", self.move_right)
#
#         self.create_obstacle()
#         self.update_game()
#
#     def create_obstacle(self):
#         x = random.randint(0, 380)
#         obstacle = self.canvas.create_rectangle(x, 0, x + 40, 20, fill="red")
#         self.obstacles.append(obstacle)
#
#     def move_left(self, event):
#         if self.canvas.coords(self.player)[0] > 0:
#             self.canvas.move(self.player, -20, 0)
#
#     def move_right(self, event):
#         if self.canvas.coords(self.player)[2] < 400:
#             self.canvas.move(self.player, 20, 0)
#
#     def update_game(self):
#         if self.game_over:
#             self.canvas.create_text(200, 300, text="Игра окончена!", font=("Arial", 24), fill="black")
#             return
#
#         for obstacle in self.obstacles:
#             self.canvas.move(obstacle, 0, 5)
#             if self.canvas.coords(obstacle)[1] > 600:
#                 self.canvas.delete(obstacle)
#                 self.obstacles.remove(obstacle)
#                 self.score += 1
#                 self.create_obstacle()
#
#         self.check_collision()
#         self.master.after(50, self.update_game)
#
#     def check_collision(self):
#         player_coords = self.canvas.coords(self.player)
#         for obstacle in self.obstacles:
#             obstacle_coords = self.canvas.coords(obstacle)
#             if (player_coords[2] > obstacle_coords[0] and
#                     player_coords[0] < obstacle_coords[2] and
#                     player_coords[1] < obstacle_coords[3]):
#                 self.game_over = True
#
#
# if __name__ == "__main__":
#     root = Tk()
#     game = Game(root)
#     root.mainloop()


# from tkinter import *
# import random
#
#
# class SnakeGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Змейка")
#
#         self.canvas = Canvas(master, width=400, height=400, bg="black")
#         self.canvas.pack()
#
#         self.snake = [(200, 200), (190, 200), (180, 200)]
#         self.snake_direction = "Right"
#         self.food_position = self.place_food()
#         self.score = 0
#         self.game_over = False
#
#         self.master.bind("<KeyPress>", self.change_direction)
#         self.update_game()
#
#     def place_food(self):
#         x = random.randint(0, 39) * 10
#         y = random.randint(0, 39) * 10
#         return (x, y)
#
#     def change_direction(self, event):
#         if event.keysym in ["Up", "Down", "Left", "Right"]:
#             self.snake_direction = event.keysym
#
#     def update_game(self):
#         if self.game_over:
#             self.canvas.create_text(200, 200, text="Игра окончена!", font=("Arial", 24), fill="white")
#             return
#
#         self.move_snake()
#         self.check_collision()
#         self.render()
#
#         self.master.after(100, self.update_game)
#
#     def move_snake(self):
#         head_x, head_y = self.snake[0]
#         if self.snake_direction == "Up":
#             new_head = (head_x, head_y - 10)
#         elif self.snake_direction == "Down":
#             new_head = (head_x, head_y + 10)
#         elif self.snake_direction == "Left":
#             new_head = (head_x - 10, head_y)
#         elif self.snake_direction == "Right":
#             new_head = (head_x + 10, head_y)
#
#         self.snake.insert(0, new_head)
#
#         if new_head == self.food_position:
#             self.score += 1
#             self.food_position = self.place_food()
#         else:
#             self.snake.pop()
#
#     def check_collision(self):
#         head_x, head_y = self.snake[0]
#         if (
#                 head_x < 0 or head_x >= 400 or
#                 head_y < 0 or head_y >= 400 or
#                 len(self.snake) != len(set(self.snake))
#         ):
#             self.game_over = True
#
#     def render(self):
#         self.canvas.delete(ALL)
#         for segment in self.snake:
#             x, y = segment
#             self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")
#
#         food_x, food_y = self.food_position
#         self.canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill="red")
#
#
# if __name__ == "__main__":
#     root = Tk()
#     game = SnakeGame(root)
#     root.mainloop()

# from tkinter import *
# import random
#
# class PingPongGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Пинг-Понг")
#
#         self.canvas = Canvas(master, width=800, height=400, bg="black")
#         self.canvas.pack()
#
#         self.ball = self.canvas.create_oval(390, 190, 410, 210, fill="white")
#         self.paddle1 = self.canvas.create_rectangle(30, 150, 50, 250, fill="blue")
#         self.paddle2 = self.canvas.create_rectangle(750, 150, 770, 250, fill="red")
#
#         self.ball_dx = random.choice([-3, 3])
#         self.ball_dy = random.choice([-3, 3])
#
#         self.master.bind("<a>", self.move_paddle1_up)
#         self.master.bind("<q>", self.move_paddle1_down)
#         self.master.bind("<p>", self.move_paddle2_up)
#         self.master.bind("<l>", self.move_paddle2_down)
#
#         self.update_game()
#
#     def move_paddle1_up(self, event):
#         if self.canvas.coords(self.paddle1)[1] > 0:
#             self.canvas.move(self.paddle1, 0, -20)
#
#     def move_paddle1_down(self, event):
#         if self.canvas.coords(self.paddle1)[3] < 400:
#             self.canvas.move(self.paddle1, 0, 20)
#
#     def move_paddle2_up(self, event):
#         if self.canvas.coords(self.paddle2)[1] > 0:
#             self.canvas.move(self.paddle2, 0, -20)
#
#     def move_paddle2_down(self, event):
#         if self.canvas.coords(self.paddle2)[3] < 400:
#             self.canvas.move(self.paddle2, 0, 20)
#
#     def update_game(self):
#         self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
#
#         ball_coords = self.canvas.coords(self.ball)
#         paddle1_coords = self.canvas.coords(self.paddle1)
#         paddle2_coords = self.canvas.coords(self.paddle2)
#
#         # Отскок от стен
#         if ball_coords[1] <= 0 or ball_coords[3] >= 400:
#             self.ball_dy *= -1
#
#         # Отскок от ракеток
#         if (ball_coords[0] <= paddle1_coords[2] and
#             paddle1_coords[1] < ball_coords[3] < paddle1_coords[3]):
#             self.ball_dx *= -1
#
#         if (ball_coords[2] >= paddle2_coords[0] and
#             paddle2_coords[1] < ball_coords[3] < paddle2_coords[3]):
#             self.ball_dx *= -1
#
#         # Проверка, вышел ли мяч за границы
#         if ball_coords[0] <= 0 or ball_coords[2] >= 800:
#             self.canvas.create_text(400, 200, text="Игра окончена!", font=("Arial", 24), fill="white")
#             return
#
#         self.master.after(20, self.update_game)
#
# if __name__ == "__main__":
#     root = Tk()
#     game = PingPongGame(root)
#     root.mainloop()












# from tkinter import *
# import random
#
#
# class SpaceShooter:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Космический шутер")
#
#         self.canvas = Canvas(master, width=800, height=600, bg="black")
#         self.canvas.pack()
#
#         self.score = 0
#         self.score_label = Label(master, text=f"Очки: {self.score}", font=("Arial", 16), bg="black", fg="white")
#         self.score_label.pack()
#
#         # Создание синего корабля
#         self.ship = self.canvas.create_rectangle(370, 500, 430, 550, fill="blue")
#
#         self.asteroids = []
#         self.bullets = []
#
#         self.master.bind("<Left>", self.move_left)
#         self.master.bind("<Right>", self.move_right)
#         self.master.bind("<space>", self.shoot)
#
#         self.spawn_asteroids()
#         self.update_game()
#
#     def spawn_asteroids(self):
#         for _ in range(2):  # Уменьшаем количество астероидов до 2
#             x = random.randint(0, 780)
#             asteroid = self.canvas.create_oval(x, 0, x + 40, 40, fill="gray")
#             self.asteroids.append(asteroid)
#         self.master.after(2000, self.spawn_asteroids)  # Спавн новых астероидов каждые 2 секунды
#
#     def move_left(self, event):
#         if self.canvas.coords(self.ship)[0] > 0:
#             self.canvas.move(self.ship, -20, 0)
#
#     def move_right(self, event):
#         if self.canvas.coords(self.ship)[2] < 800:
#             self.canvas.move(self.ship, 20, 0)
#
#     def shoot(self, event):
#         x1, y1, x2, y2 = self.canvas.coords(self.ship)
#         bullet = self.canvas.create_rectangle((x1 + x2) / 2 - 5, y1, (x1 + x2) / 2 + 5, y1 - 10, fill="red")
#         self.bullets.append(bullet)
#
#     def update_game(self):
#         self.move_asteroids()
#         self.move_bullets()
#         self.check_collisions()
#         self.score_label.config(text=f"Очки: {self.score}")  # Обновляем счёт
#         self.master.after(50, self.update_game)
#
#     def move_asteroids(self):
#         for asteroid in self.asteroids:
#             self.canvas.move(asteroid, 0, 7)  # Устанавливаем скорость на 7
#             if self.canvas.coords(asteroid)[1] > 600:
#                 self.canvas.delete(asteroid)
#                 self.asteroids.remove(asteroid)
#
#     def move_bullets(self):
#         for bullet in self.bullets:
#             self.canvas.move(bullet, 0, -10)
#             if self.canvas.coords(bullet)[1] < 0:
#                 self.canvas.delete(bullet)
#                 self.bullets.remove(bullet)
#
#     def check_collisions(self):
#         asteroids_to_remove = []
#         bullets_to_remove = []
#
#         for asteroid in self.asteroids:
#             for bullet in self.bullets:
#                 if self.check_collision(asteroid, bullet):
#                     asteroids_to_remove.append(asteroid)
#                     bullets_to_remove.append(bullet)
#                     self.score += 1
#
#             if self.check_collision(asteroid, self.ship):
#                 self.canvas.create_text(400, 300, text="Игра окончена!", font=("Arial", 24), fill="white")
#                 self.master.unbind("<Left>")
#                 self.master.unbind("<Right>")
#                 self.master.unbind("<space>")
#                 return
#
#         # Удаляем астероиды и пули после завершения итераций
#         for asteroid in asteroids_to_remove:
#             self.canvas.delete(asteroid)
#             self.asteroids.remove(asteroid)
#
#         for bullet in bullets_to_remove:
#             self.canvas.delete(bullet)
#             self.bullets.remove(bullet)
#
#     def check_collision(self, obj1, obj2):
#         coords1 = self.canvas.coords(obj1)
#         coords2 = self.canvas.coords(obj2)
#         return not (coords1[2] < coords2[0] or coords1[0] > coords2[2] or
#                     coords1[3] < coords2[1] or coords1[1] > coords2[3])
#
#
# if __name__ == "__main__":
#     root = Tk()
#     game = SpaceShooter(root)
#     root.mainloop()











# user = {
#     "name": "Bill",
#     "surname": "Bosh",
#     "age": 22
# }
# if user["age"]:
#     print('yes')
# else:
#     print('no')

# cities = {
#     'Київ': 0,
#     'Вінниця': 240,
#     'Харків': 470,
#     'Ужгород': 808,
#     'Львів': 540,
#     'Житомир': 120,
#     'Одеса': 430
# }
# longest_city = max(cities)
# print(longest_city)

# import pygame
# import sys
#
# # Инициализация Pygame
# pygame.init()
#
# # Константы
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# FPS = 60
#
# # Цвета
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
#
# # Класс игрока
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('')
#         self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
#         self.speed = 5
#
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] and self.rect.x > 0:
#             self.rect.x -= self.speed
#         if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
#             self.rect.x += self.speed
#         if keys[pygame.K_UP] and self.rect.y > 0:
#             self.rect.y -= self.speed
#         if keys[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
#             self.rect.y += self.speed
#
# # Класс пуль
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((5, 5))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect(center=(x, y))
#         self.speed = 10
#
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x > SCREEN_WIDTH:
#             self.kill()  # Удаление пули, если она выходит за пределы экрана
#
# # Основная игра
# def main():
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Звездные войны")
#     clock = pygame.time.Clock()
#
#     # Создание групп
#     all_sprites = pygame.sprite.Group()
#     bullets = pygame.sprite.Group()
#
#     # Создание игрока
#     player = Player()
#     all_sprites.add(player)
#
#     # Основной игровой цикл
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     # Создание пули
#                     bullet = Bullet(player.rect.centerx, player.rect.centery)
#                     all_sprites.add(bullet)
#                     bullets.add(bullet)
#
#         # Обновление
#         all_sprites.update()
#
#         # Рендеринг
#         screen.fill(WHITE)
#         all_sprites.draw(screen)
#
#         # Обновление экрана
#         pygame.display.flip()
#         clock.tick(FPS)
#
# if __name__ == "__main__":
#     main()
#


# word = 'heruvhebvheuh'
# lst = {}
# for char in word:
#     if char in lst:
#         lst[char] += 1
#     else:
#         lst[char] = 1
# sorted_lst = sorted(lst)
# most_common = sorted_lst[:3]
# print(most_common)



















# from flask import Flask, render_template
# import os
#
# app = Flask(__name__)
#
# app.config['SECRET_KEY'] = os.urandom(24)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     if not os.path.exists('templates'):
#         os.makedirs('templates')
#     if not os.path.exists('static'):
#         os.makedirs('static')
#
#     with open('templates/index.html', 'w') as f:
#         f.write('''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>My Flask Application</title>
#     <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
# </head>
# <body>
# </body>
# </html>''')
#
#     with open('static/style.css', 'w') as f:
#         f.write('''body {
#     font-family: Arial, sans-serif;
#     background-color: #f4f4f4;
#     margin: 0;
#     padding: 20px;
# }''')
#
#     app.run(debug=True)































#
# dct = {'a': 2, 'b': 3, 'c': 4}
# lst = 1
# for i in dct.values():
#     lst *= i
# print(lst)











#


# employee = {
#     'John': {
#         'salary': 2000,
#         'start_date': 2020,
#         'position': 'developer'
#     },
#     'Andriy': {
#         'salary': 1000,
#         'start_date': 2020,
#         'position': 'developer'
#     }
# }
# deleted_employees = {}
#
# while True:
#     option = input('''Enter your option
# A to add more
# S to list all employees
# D to delete employee
# E to edit employee
# V to view deleted employees
# Q to quit
# G to get an employee
#     ''')
#
#     if option == 'A':
#         name = input('Enter employee name: ')
#         if name in employee:
#             print('This name already exists.')
#         else:
#             salary = int(input('Enter employee salary: '))
#             start_date = int(input('Enter year: '))
#             position = input('Enter employee position: ')
#
#             employee[name] = {
#                 'salary': salary,
#                 'start_date': start_date,
#                 'position': position,
#             }
#             print('Employee added:', employee)
#
#     elif option == 'S ':
#         if employee:
#             for name, data in employee.items():
#                 print(f'Employee Name: {name}')
#                 for k, v in data.items():
#                     print(f' {k}: {v}')
#                 print('-' * 80)
#         else:
#             print('No employees.')
#
#     elif option == 'D':
#         name_to_del = input('Enter name of employee to delete: ')
#         if name_to_del in employee:
#             deleted_employees[name_to_del] = employee[name_to_del]
#             del employee[name_to_del]
#             print(f'Employee {name_to_del} deleted.')
#         else:
#             print('There is no such employee.')
#
#     elif option == 'E':
#         name_to_edit = input('Enter name of employee to edit: ')
#         if name_to_edit in employee:
#             salary = int(input('Enter new employee salary: '))
#             start_date = int(input('Enter new year: '))
#             position = input('Enter new employee position: ')
#
#             employee[name_to_edit] = {
#                 'salary': salary,
#                 'start_date': start_date,
#                 'position': position,
#             }
#             print(f'Employee {name_to_edit} was been updated.')
#         else:
#             print('There is no such employee.')
#
#     elif option == 'V':
#         if deleted_employees:
#             print('Deleted employees:')
#             for name, data in deleted_employees.items():
#                 print(f'Employee name: {name}')
#                 for k, v in data.items():
#                     print(f' {k}: {v}')
#                 print('-' * 80)
#         else:
#             print('No deleted employees.')
#
#     elif option == 'G':
#         get_name = input('Enter employee name: ')
#         if get_name in employee:
#             for k, v in employee[get_name].items():
#                 print(f' {k}: {v}')
#             print('-' * 80)
#
#     elif option == 'Q':
#         print('Quitting the program.')
#         break
#
#     else:
#         print('Invalid option. Please try again.')
#

# def book_table():
#    last_name = input('Enter your last name')
#    number_of_tables = int(input('Enter a number of tables'))
#    print(f'Table was been reserved for the name {last_name}. Number of tables {number_of_tables}.')
# print(book_table())

# def sum():
#    total = 0
#    nums = [1, 2, 3]
#    for i in nums:
#       total += i ** 2
#    return total
# result = sum()
# print(result)

# def nums(a, b, c, suma=False):
#    if suma:
#       return a+b+c
# print(sum(nums(1, 2, 3)))

# def anagram(str1, str2):
#    str1 = str1.replace(' ', '').lower()
#    str2 = str2.replace(' ', '').lower()
#    return sorted(str1) == sorted(str2)
# print(anagram("abc", "cba"))


# import math
#
# radius = 5
# perimeter = 2 * math.pi * radius
# print(perimeter)

# from collections import Counter
# with open('abc.txt', 'r', encoding='utf-8') as file:
#     names = file.read().splitlines()
# name_counts = Counter(names)
# most_common_name, count = name_counts
# print(most_common_name)


import math
print('Chose an operation: + Addition, - Subtraction, * Multiplication, / Division')
choice = input('Enter an operation')
x, y = float(input('First Number')), float(input('Second Number'))
operations = {
    '+': x + y,
    '-': x - y,
    '*': x * y,
    '/': x / y
}
print(operations.get(choice))

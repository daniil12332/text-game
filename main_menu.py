from os import system
from random import randint
mode = 0
p_index = 24
txt = open("main_menu.txt", "r", encoding="utf-8")
game = list(txt.read())
x = 23
y = 11
while mode != 5:
	while mode == 0:
		if mode == 5:
			break
		system("clear")
		index = 0
		while index != len(game):
			print(game[index], end="")
			index += 1

		key = input(":")

		if key == "w" and p_index - x*4 > 0:
			try:
				p_index -= x*4
				game[p_index+x*4] = " "
				game[p_index] = "Y"
			except:
				None
		if key == "s" and p_index + x*4 < 210:
			try:
				p_index += x*4
				game[p_index-x*4] = " "
				game[p_index] = "Y"
			except:
				None
		if key == "c":
			if p_index == 24:
				mode = 1
			elif p_index == 24+x*4:
				mode = 2
			elif p_index == 24+x*4+x*4:
				mode = 5
			break
	if mode == 1:
		game = []

		air_str = " "
		wall_str = "N"
		end_str = "Z"
		player_str = "P"

		x = 10
		y = 10
		for i in range(0, x*y):
			a = randint(1, 4)
			if a == 1 or a == 2 or a == 3:
				game.append(air_str)
			else:
				game.append(wall_str)

		z_index = randint(0, 24)
		p_index = randint(0, 24)

		while z_index == p_index:
			z_index = randint(0, 24)
			p_index = randint(0, 24)

		game[z_index] = end_str
		game[p_index] = player_str


	while mode == 1:
		system("clear")
		index = 0
		while index != len(game):
			print(game[index], end=" ")
			if (index+1) % x == 0:
				print()
			index += 1

		key = input(":")

		if key == "w":
			try:
				p_index -= x
				if game[p_index] == wall_str:
					p_index += x
				elif game[p_index] == end_str:
					game = []
					for i in range(0, x*y):
						a = randint(1, 4)
						if a == 1 or a == 2 or a == 3:
							game.append(air_str)
						else:
							game.append(wall_str)
					z_index = randint(0, 24)
					game[z_index] = end_str
					game[p_index] = player_str
				else:
					game[p_index+x] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "s":
			try:
				p_index += x
				if game[p_index] == wall_str:
					p_index -= x
				elif game[p_index] == end_str:
					game = []
					for i in range(0, x*y):
						a = randint(1, 4)
						if a == 1 or a == 2 or a == 3:
							game.append(air_str)
						else:
							game.append(wall_str)
					z_index = randint(0, 24)
					game[z_index] = end_str
					game[p_index] = player_str
				else:
					game[p_index-x] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "d":
			try:
				p_index += 1
				if game[p_index] == wall_str:
					p_index -= 1
				elif game[p_index] == end_str:
					game = []
					for i in range(0, x*y):
						a = randint(1, 4)
						if a == 1 or a == 2 or a == 3:
							game.append(air_str)
						else:
							game.append(wall_str)
					z_index = randint(0, 24)
					game[z_index] = end_str
					game[p_index] = player_str
				else:
					game[p_index-1] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "a":
			try:
				p_index -= 1
				if game[p_index] == wall_str:
					p_index += 1
				elif game[p_index] == end_str:
					game = []
					for i in range(0, x*y):
						a = randint(1, 4)
						if a == 1 or a == 2 or a == 3:
							game.append(air_str)
						else:
							game.append(wall_str)
					z_index = randint(0, 24)
					game[z_index] = end_str
					game[p_index] = player_str
				else:
					game[p_index+1] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "exit":
				mode = 0
				p_index = 24
				txt = open("main_menu.txt", "r", encoding="utf-8")
				game = list(txt.read())
				x = 23
				y = 11
				break
		if key == "r":
			game = []
			for i in range(0, x*y):
				a = randint(1, 4)
				if a == 1 or a == 2 or a == 3:
					game.append(air_str)
				else:
					game.append(wall_str)
			z_index = randint(0, 24)
			game[z_index] = end_str
			game[p_index] = player_str

	if mode == 2:
		txt = open("my_level.txt", "r", encoding="utf-8")
		game = list(txt.read())

		x = 15

		air_str = " "
		wall_str = "N"
		end_str = "Z"
		player_str = "P"

		index = 0
		p_index = 0
		for i in game:
			if i == "P":
				p_index = index
			index += 1

	while mode == 2:
		system("clear")
		index = 0
		print("", end=" ")
		while index != len(game):
			print(game[index], end=" ")
			index += 1

		key = input(":")

		if key == "w":
			try:
				p_index -= x
				if game[p_index] == wall_str:
					p_index += x
				elif game[p_index] == end_str:
					mode = 0
					p_index = 24
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 23
					y = 11
					break
				else:
					game[p_index+x] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "s":
			try:
				p_index += x
				if game[p_index] == wall_str:
					p_index -= x
				elif game[p_index] == end_str:
					mode = 0
					p_index = 24
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 23
					y = 11
					break
				else:
					game[p_index-x] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "d":
			try:
				p_index += 1
				if game[p_index] == wall_str:
					p_index -= 1
				elif game[p_index] == end_str:
					mode = 0
					p_index = 24
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 23
					y = 11
					break
				else:
					game[p_index-1] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "a":
			try:
				p_index -= 1
				if game[p_index] == wall_str:
					p_index += 1
				elif game[p_index] == end_str:
					mode = 0
					p_index = 24
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 23
					y = 11
					break
				else:
					game[p_index+1] = air_str
					game[p_index] = player_str
			except:
				None
		if key == "exit":
			mode = 0
			p_index = 24
			txt = open("main_menu.txt", "r", encoding="utf-8")
			game = list(txt.read())
			x = 23
			y = 11
			break

txt.close()

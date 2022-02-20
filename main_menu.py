from os import system
from random import randint
import keyboard
import time
mode = 0
p_index = 46
txt = open("main_menu.txt", "r", encoding="utf-8")
game = list(txt.read())
x = 45
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

		time.sleep(0.15)

		if keyboard.is_pressed("w") and p_index - x*4 > 0:
			try:
				p_index -= x*4
				game[p_index+x*4] = " "
				game[p_index] = "Y"
			except:
				None
		if keyboard.is_pressed("s") and p_index + x*4 <= x*16:
			try:
				p_index += x*4
				game[p_index-x*4] = " "
				game[p_index] = "Y"
			except:
				None
		if keyboard.is_pressed("c"):
			if p_index == 46:
				mode = 1
			elif p_index == 46+x*4:
				mode = 2
			elif p_index == 46+x*4+x*4:
				mode = 3
			elif p_index == 46+x*4+x*4+x*4:
				mode = 5
			break
	if mode == 1:
		game = []

		air_str = " "
		wall_str = "H"
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

		time.sleep(0.15)

		if keyboard.is_pressed("w"):
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
		if keyboard.is_pressed("s"):
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
		if keyboard.is_pressed("d"):
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
		if keyboard.is_pressed("a"):
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
		if keyboard.is_pressed("e"):
				mode = 0
				p_index = 46
				txt = open("main_menu.txt", "r", encoding="utf-8")
				game = list(txt.read())
				x = 45
				y = 11
				break
		if keyboard.is_pressed("r"):
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

		index = 0
		x = 0
		for i in game:
			if i == "\n":
				x = index+1
				break
			index += 1

	while mode == 2:
		system("clear")
		index = 0
		while index != len(game):
			print(game[index], end=" ")
			index += 1

		time.sleep(0.15)

		if keyboard.is_pressed("w"):
			try:
				p_index -= x
				if game[p_index] == wall_str:
					p_index += x
				elif game[p_index] == end_str:
					mode = 0
					p_index = 46
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 45
					y = 11
					break
				else:
					game[p_index+x] = air_str
					game[p_index] = player_str
			except:
				None
		if keyboard.is_pressed("s"):
			try:
				p_index += x
				if game[p_index] == wall_str:
					p_index -= x
				elif game[p_index] == end_str:
					mode = 0
					p_index = 46
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 45
					y = 11
					break
				else:
					game[p_index-x] = air_str
					game[p_index] = player_str
			except:
				None
		if keyboard.is_pressed("d"):
			try:
				p_index += 1
				if game[p_index] == wall_str:
					p_index -= 1
				elif game[p_index] == end_str:
					mode = 0
					p_index = 46
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 45
					y = 11
					break
				else:
					game[p_index-1] = air_str
					game[p_index] = player_str
			except:
				None
		if keyboard.is_pressed("a"):
			try:
				p_index -= 1
				if game[p_index] == wall_str:
					p_index += 1
				elif game[p_index] == end_str:
					mode = 0
					p_index = 46
					txt = open("main_menu.txt", "r", encoding="utf-8")
					game = list(txt.read())
					x = 45
					y = 11
					break
				else:
					game[p_index+1] = air_str
					game[p_index] = player_str
			except:
				None
		if keyboard.is_pressed("e"):
			mode = 0
			p_index = 46
			txt = open("main_menu.txt", "r", encoding="utf-8")
			game = list(txt.read())
			x = 45
			y = 11
			break

	if mode == 3:
		game = []
		x = 40
		y = 40
		skeletons = []
		trees = []
		p_index = 0
		for i in range(0, x*y):
			if i < x:
				game.append("H")
				if i == x-1:
					game.append("\n")
			elif i >= (y-1)*x:
				game.append("H")
			elif i % x == 0:
				game.append("H")
			elif (i+1) % x == 0:
				game.append("H")
				game.append("\n")
			else:
				game.append(" ")

		while game[p_index] != " ":
			p_index = randint(0, x*y)

		for i in range(0, 15):
			index = randint(0, x*y)
			if game[index] != " ":
				index = randint(0, x*y)
			skeletons.append(index)

		for i in range(0, 50):
			index = randint(0, x*y)
			if game[index] != " ":
				index = randint(0, x*y)
			trees.append(index)
		
		game[p_index] = "O"

		for i in skeletons:
			game[i] = "S"

		for i in trees:
			game[i] = "T"


	while mode == 3:
		system("clear")
		index = 0
		for i in game:
			if i == "\n":
				print(i, end="")
			else:
				print(i, end=" ")
			index += 1
		print()

		time.sleep(0.15)

		index = 0
		while index != len(skeletons):
			a = randint(0, 3)
			if a == 0 and game[skeletons[index]+x+1] == " ":
				game[skeletons[index]] = " "
				skeletons[index] += x+1
				game[skeletons[index]] = "S"
			if a == 1 and game[skeletons[index]-x-1] == " ":
				game[skeletons[index]] = " "
				skeletons[index] -= x+1
				game[skeletons[index]] = "S"
			if a == 2 and game[skeletons[index]+1] == " ":
				game[skeletons[index]] = " "
				skeletons[index] += 1
				game[skeletons[index]] = "S"
			if a == 3 and game[skeletons[index]-1] == " ":
				game[skeletons[index]] = " "
				skeletons[index] -= 1
				game[skeletons[index]] = "S"
			index += 1

		if keyboard.is_pressed("w") and game[p_index - x-1] == " ":
			game[p_index] = " "
			p_index -= x+1
			game[p_index] = "O"
		if keyboard.is_pressed("s") and game[p_index + x+1] == " ":
			game[p_index] = " "
			p_index += x+1
			game[p_index] = "O"
		if keyboard.is_pressed("a") and game[p_index - 1] == " ":
			game[p_index] = " "
			p_index -= 1
			game[p_index] = "O"
		if keyboard.is_pressed("d") and game[p_index + 1] == " ":
			game[p_index] = " "
			p_index += 1
			game[p_index] = "O"

		if keyboard.is_pressed("e"):
			mode = 0
			p_index = 46
			txt = open("main_menu.txt", "r", encoding="utf-8")
			game = list(txt.read())
			x = 45
			y = 11
			break

txt.close()
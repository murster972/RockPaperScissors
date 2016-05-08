#!/usr/bin/env python
from random import randint

class Player:
	valid_moves = {"1": "rock", "2": "paper", "3": "scissors"}

	def __init__(self):
		self.played_moves = []
		self.current_move = ""

	def select_move(self):
		'''allows the user to make their move'''
		pass

	def _valid_move(self):
		'''comapares the users current move to the valid moves to ensure it's valid'''
		return Player().valid_moves.get(self.current_move, 0)

class Person(Player):
	def select_move(self):
		'''allows a Person to select rock, paper or scissors'''
		self.current_move = ""

		while not self._valid_move():
			self.current_move = input("Please Select an option: 1 - Rock, 2 - Paper or 3 - Scissors: ")

		self.current_move = Player().valid_moves[self.current_move]
		print("Player has selected: {}".format(self.current_move))

class AI(Player):
	def select_move(self):
		'''allows the AI to randomly select rock, paper or scissors'''
		self.current_move = Player().valid_moves[str(randint(1, 3))]
		print("AI has selected: {}".format(self.current_move))
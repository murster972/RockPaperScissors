#!/usr/bin/env python
from random import randint
import sys, os

class Game:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.next_player = self.player1

class Player:
	valid_moves = {"1": "rock", "2": "paper", "3": "scissors"}

	def __init__(self):
		self.moves = []
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
			select_move = input("Please Select an option: 1 - Rock, 2 - Scissors and 3 - Paper: ")

class AI(Player):
	def select_move(self):
		'''allows the AI to randomly select rock, paper or scissors'''
		self.current_move = valid_moves[str(randint(1, 3))]
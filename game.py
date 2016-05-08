#!/usr/bin/env python
import players
import sys
import os

class Game:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.next_player = self.player1
		self.game_no = 1
		self.current_game = 0

	def run(self):
		'''runs each game, printing winners'''
		while True:
			if self.current_game != self.game_no:
				self.current_game = self.game_no
				print("Game {}".format(str(self.game_no)))

			self.next_move()
			self.next_move()

			if self.get_winner() == 'draw':
				print("No winner yet, continue current game.")
			else:
				print("Winner is {}".format(self.get_winner()))
				self.game_no += 1
				nex_game = input("Press enter to start the next game...")

			print()

	def next_move(self):
		'''gets the next move for the next player'''
		self.next_player.select_move()
		self.next_player = self.player1 if self.next_player == self.player2 else self.player2

	def get_winner(self):
		'''Returns the winner of the current game, or draw if players select same option'''
		if self.player1.current_move == self.player2.current_move:
			return "draw"

		elif self.player1.current_move == 'rock' and self.player2.current_move == 'scissors':
			return "Player 1"

		elif self.player1.current_move == 'paper' and self.player2.current_move == 'rock':
			return "Player 1"

		elif self.player1.current_move == 'scissors' and self.player2.current_move == 'paper':
			return "Player 1"

		else:
			return "Player 2"

def main():
	os.system("clear")
	p1 = players.Person()
	p2 = players.AI()
	print("AI is player 2")
	game = Game(p1, p2)
	game.run()

if __name__ == '__main__':
	main()
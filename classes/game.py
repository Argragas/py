import random
import pprint
from .magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
	def __init__(self, hp, mp, atk, df, magic):
		self.hp = hp
		self.hpmax = hp
		self.mp = mp
		self.max_mp = mp
		self.atk = atk
		self.df = df
		self.magic = magic
		self.atkmin = atk - 10
		self.atakmax = atk + 10
		self.actions = ["Attack", "Magic"]
	

	def generate_damage(self):
		return random.randrange(self.atkmin, self.atk)
	
	
	# def generate_spell_damage(self, i):
	# 	mgl = self.magic[i]["dmg"] - 5
	# 	mgh = self.magic[i]["dmg"] + 5
	# 	return random.randrange(mgl, mgh)

	
	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def heal(self, dmg):
		self.hp += dmg
		if self.hp > self.hpmax:
			self.hp = self.hpmax


	def get_hp(self):
		return self.hp


	def get_maxhp(self):
	   return self.hpmax


	def get_mp(self):
	   return self.mp


	def get_maxmp(self):
	   return self.max_mp
	
	def reduce_mp(self, cost):
	   self.mp -= cost

	# def get_spellname(self, i):
	#    return self.magic[i]["name"]
	#
	# def get_spellcost(self, i):
	# 	return self.magic[i]["cost"]
	
	def choose_magic(self):
		i = 1
		print(bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
		for spell in self.magic:
			print(str(i), ":", spell.name, "(cost :", spell.cost, ")")
			i += 1
		
	def choose_action(self):
		print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
		i = 1
		for item in self.actions:
			print(str(i), ":", item)
			i += 1

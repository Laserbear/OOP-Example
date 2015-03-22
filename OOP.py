#Christian Ng
#Prompt from MakeSchool
# -*- coding: utf-8 -*-
import random  #Library for pseudorandom numbers

humanNameList = ["Christian", "Jeremy", "Tommy", "Ryan", "Douglas"] #List of human names; Not strictly necessary

petNameList = ["Fido", "Chester", "Ripper", "Lucky", "Tucker", "Niko", "Koda", "Bear", "Shadowfax"] #list of pet names 

humanList = [] #initialize empty list 


def populate(humanstomake): # generate a specified number of humans
	for i in range(humanstomake):
		humanList.append(Human(humanNameList[random.randint(0,4)], Pet(petNameList[random.randint(0,8)], random.randint(1,2) , random.randint(0,1)))) #use arbitrary values

class Pet(object):
	def __init__(self, name, type, audible): #important characteristics defined
		self.name = name
		self.type = type
		self.audible = audible
	def Eat(self): 
		print(self.name + " is eating")
		if (self.type == 1 and self.audible == 1): #Checks that it is a cat and that it can make noise
			print(self.name + " says 'Meowww, I’m still hungry'")

	def makeNoise(self): 
		if (self.audible) == 1: #checks that it can make noise
			if (self.type == 2): #checks if it is a dog
				print(self.name + " says 'Woof'")
			else: 
				print(self.name + " says 'Meow'")
		else:
			print(self.name + " *remains silent*")
	
class Human(object):
	population = 0
	def __init__(self, name, pet):
		self.name = name
		self.pet = pet 
		Human.population += 1 #increment population

	@staticmethod
	def populationCount():
		print("The total human population is " + str(Human.population) ) #output humans created

	def makePetMakeNoise(self): #call makeNoise function on pet
		Pet.makeNoise(self.pet)

	def feedPet(self): #call Eat function on pet
		Pet.Eat(self.pet)
	


def main():
	populate(random.randint(10, 15)) #make between 10 and 15 humans
	for item in humanList: #iterate through list
		Human.makePetMakeNoise(item)
		Human.feedPet(item)
	Human.populationCount() 
		
	

	
main()


	


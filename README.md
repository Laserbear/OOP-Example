# OOP-Example
Object Oriented Programming exercises to fufill these requisites:

Humans have a name and a Pet. Humans have two important instance methods:
makePetMakeNoise: this method calls makeNoise on the Human's pet and passes a random integer as a parameter
feedPet: this method calls the eat method of the Human's pet

Humans also have a class method called populationCount  that will return the total amount of Humans created (hint: use a class variable to implement this!)

Pets have a name and a noise stored as strings as well as a boolean canMakeNoise. Our program has two types of Pets: Cats and Dogs. They also have a makeNoise method that accepts a parameter number that prints their noise along with their name to the console number times unless they can't make a noise, in which case they print "<pet's name> *remains silent*" to the console.

Finally all Pets have an eat method. When a Pet eats it prints "<pet's name> is eating...". 
A cat will additionally print "I'm still hungry, meow".

Create a program that creates multiple Humans and creates a Pet for each of them. Make sure to create at least one of each type of Pet.  There should be at least one Pet for which canMakeNoise is set to FALSE. 

Store these multiple Humans in a list and iterate through this list once, calling makePetMakeNoise and feedPet on each Human. After iterating through the list print the total population of Humans to the console.

As a result you should see each of these messages at least once in the console:
<pet's name> is eating
I'm still hungry, meow
<pet's name> *remains silent*
<pet's name> <pet's noise>
The total number of humans is: <populationSize>


Currently done in Python

C, Ruby, and Swift planned

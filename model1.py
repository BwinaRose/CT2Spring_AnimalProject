"""
Created on Thu Mar 19 13:11:50 2020

@author: srkrueger19@students.desu.edu, marcelovalenzuela,
         gsdaniel19@students.desu.edu,

"""

class Animal:
    def __init__(self, name, color, age, num_legs, inHeat):
        self.name = name
        self.age = age
        self.color = color
        self.num_legs = num_legs
        self.inHeat = inHeat
    
    def description(self):
        return self.name, self.age
    
    def makeSound(self):
        raise NotImplementedError("Animals have multiple sounds they make.")
    
    def move(self):
        return '{} moved.' .format(self.name)
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_numlegs(self, num_legs):
        return self.num_legs
    
    def get_age(self):
        return self.age
    
    def get_mating(self):
        return self.inHeat
    
    def set_inHeat(self):
        if (self.age > 4):
            self.inHeat = True
        
    def breed(self):
        if (self.inHeat == True):
            return '{} found another {}.'.format(self.name,self.name)
        else:
            return '{} is not old enough to breed'.format(self.name)
    
    def ageUp(self):
        if (self.age > 15):
            return '{} has passed peacefully.'.format(self.name)
        else:
            self.age = self.age + 1
        

class Mammal(Animal):
    species = 'mammal'
    
    #####FIX ME ADD Rest of code#####
    
    def makeSound(self):
        raise NotImplementedError("Mammals have multiple sounds they make.")
    
    def set_BloodTemp(self):
        return "{} is a {} and runs at greater than a 97 body temperature.".format(self.name, self.species)

####creat carnivora class below  
class Perisodactyla(Mammal):
    
    def makeSound(self):
        raise NotImplementedError("Perisodactyla have multiple sounds they make.")
    
    pass #####FIX ME ADD Rest of code#####
   
###########     
# Child class (inherits Perisodactyla class)    
class Horse(Perisodactyla):
    typeOfBreed = ""
    isRaceHorse = True
    
    def makeSound(self):
        return "neigh"

class Donkey(Perisodactyla):
    def makeSound():
        return "bray"
    def carryLoad():
        return int
    
class Artiodactyla(Mammal):
    
    #####FIX ME ADD Rest of code#####
    pass ##Remove and fix me
    
 
###########   
# Child class (inherits Artiodactyla class)
# very basic but works    
class Goat(Artiodactyla):
    def makeSound():
        return "bleat"
    def getMilk():
        return "Got Goat Milk"
    
class Sheep(Artiodactyla):
    def makeSound():
        return "baaa"
    def getWool():
        return "Got Woool"
    
class Pig(Artiodactyla):
    typeOfPig = "Pig"
    earSize = 12

    def makeSound(self):
        return "A {} makes the sound oink.".format(self.typeOfPig)
    def eatAnything(self):
        return "A {} will eat anything.".format(self.typeOfPig)
    def digWithSnout(self):
        return "A {} digs with its snout.".format(self.typeOfPig)
    
    def get_earSize(self): 
        return "A {} has at least {} inch ears.".format(self.typeOfPig, self.earSize)    
    
class Cow(Artiodactyla): 
    spotColor = "Black"
    forMilkProduction = True
    
    def makeSound(self):
        return "A {} spotted cow make the sound Mooo.".format(self.spotColor)
    
    def get_Milk(self):
        
        if self.forMilkProduction == True:
               return "You received milk from a {} spotted cow.".format(self.spotColor)
        elif self.forMilkProduction == False:
               return "You did not get milk from a {} spotted cow.".format(self.spotColor)
        else:
               return "Acceptable answers for milk Production (True or False)."
    
    def eatGrass(self):
        return "A {} spotted cow eats grass.".format(self.spotColor)   
    
class Carnivora(Mammal):
    canEatMeat = True
    isPredator = True
    
    def hunt(self, animal):
        return "It is {} that a carnivora is a predator and is {} that they can eat {} meat.".format(self.isPredator, self.canEatMeat, animal)
    def chasePray(self, animal):
        return "Carnivora like to hase {} pray.".format(animal)
    
# Child class (inherits Carnivora class)
class Dog(Carnivora):
    likesBones = True
    likesWalks = True
    
    def set_Trick(self, trick):
        return "{} can {} and is {} that he/she likes walks.".format(self.name, trick, self.likesWalks)
    
    def get_Smell(self, smell):
        return "It's {} that {} likes bones and can smell {}.".format(self.likesBones, self.name, smell)
    
    def makeSound(self):
        #return "Moo"
        return "A dog makes the sound Woof."   
    
class Cat(Carnivora):
    likesFish = True
    catLifes = 9
    
    def scratchFurniture(self, furniture):
        return "{} is a cat that like to scratch a {}.".format(self.name, furniture)
    
    def groomSelf(self):
        return "It's {} that {} likes Fish and has {} lifes still but likes to spend most of the day grooming him/her self".format(self.likesFish, self.name, self.catLifes)
    
    def makeSound(self):
        #return "Moo"
        return "A cat makes the sound Meow." 
    
class Oviparous(Animal):
    def __init__(self, name, color, age, num_legs, inHeat, sound,bloodType,
                     currentlymolting, nestLocation, eggsInBatch):
        super().__init__(name, color, age, num_legs, inHeat, sound)
        self.bloodType = bloodType
        self.currentlymolting = currentlymolting
        self.nestLocation = nestLocation
        self.eggsInBatch = eggsInBatch

    def get_bloodType(self):
        return '{} is a {} oviparous.'.format(self.name, self.bloodType)

    def get_currentlyMolting(self):
        return self.currentlyMolting

    def get_nestLocation(self):
        return self.nestLocation

    def get_eggsInBatch(self):
        return self.eggsInBatch

    def setNestLocation(self):
        self.nestLocation = input('New nest location:')

    def makeSound(self):
        raise NotImplementedError("Oviparous have multiple sounds they make.")

class Bird(Oviparous):
    def __init__(self):
        self.beakLength = None
        self.wingSpeed = None
        self.ableToFly = None
        self.chirpFrequency = None

    def get_beakLength(self, ):
        pass

    def get_wingSpeed(self, ):
        pass

    def get_ableToFly(self, ):
        pass

    def get_chirpFrequency(self, ):
        pass

    def makeSound(self, chirpFrequency):
        pass

    def setChirpFrequency(self, int):
        pass

class Reptile(Oviparous):
    def __init__(self):
        self.tailLength = None
        self.numOfScales = None
        self.ableToSwim = None
        self.isVenomous = None
        self.numOfClicks = None

    def get_tailLength(self, ):
        pass

    def get_numScales(self, ):
        pass

    def get_ableToSwim(self, ):
        pass

    def get_isVenomous(self, ):
        pass

    def makeSound(self, numOfClicks):
        pass

    def set_numOfClicks(self, int):
        pass

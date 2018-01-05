import random
#Indivitual Class
class Individual:
    geneLength = 0
    fitness = 0
    word = None
    def __init__(self,geneLength,w):
        self.geneLength = geneLength
        self.gene = []
        self.word = w
        for i in range(self.geneLength):
            self.gene.append(chr(random.randint(65,90)))

    def calculateFitness(self):
        self.fitness = 0
        for i in range(len(self.gene)):
            self.fitness += abs(ord(self.gene[i]) - ord(self.word[i]))
        return self.fitness

    def showGene(self):
        print(self.gene,'=',self.fitness)

#Population Class
class Population:
    populationSize = 0
    indivituals = []
    fitness = []
    fittest = None
    fittestIndivitualIndex = None
    totalFItness = 0
    finalWord = None
    geneLen = 0
    foundValue = 0

    def __init__(self,populationSize,geneLen,word):
        self.populationSize = populationSize
        self.geneLen = geneLen
        self.finalWord = word.upper()
        self.initializePopulation()

    def initializePopulation(self):
        for i in range(self.populationSize):
            self.indivituals.append(Individual(self.geneLen,self.finalWord))

    def calculateFitnessOfIndiviuals(self):
        self.totalFItness = 0
        for i in range(self.populationSize):
           self.totalFItness += self.indivituals[i].calculateFitness()

    def sortIndiviual(self):
        for i in range(len(self.indivituals)):
            for j in range(0,len(self.indivituals)-i-1):
                if self.indivituals[j].fitness > self.indivituals[j+1].fitness:
                    self.indivituals[j], self.indivituals[j+1] = self.indivituals[j+1], self.indivituals[j]

    def copyIndivitual(self,ind):
        n = Individual(self.geneLen,self.finalWord)
        n.gene.clear()
        for i in ind.gene:
            n.gene.append(i)
        return n

    def getFittestIndivitual(self):
        self.sortIndiviual()
        self.fittestIndivitualIndex = 0
        self.fittest = self.indivituals[0].fitness
        return self.copyIndivitual(self.indivituals[0])

    def getSecondFittestIndivitual(self):
        return self.copyIndivitual(self.indivituals[1])

    def getLeastIndivitual(self):
        return self.populationSize - 1

    def printPopulation(self):
        self.sortIndiviual()
        for i in self.indivituals:
            i.showGene()

    def found(self):
        for w in self.indivituals:
            if w.fitness is self.foundValue:
                return True
        return False



def crossOver(fittest,secondFittest):
    randomCrossOverPoint = random.randint(0,fittest.geneLength-1)
    for i in range(randomCrossOverPoint,fittest.geneLength):
        fittest.gene[i],secondFittest.gene[i] = secondFittest.gene[i], fittest.gene[i]



def mutation(fittest, secondFittest):
    randomCrossOverPoint = random.randint(0, fittest.geneLength-1)
    if fittest.gene[randomCrossOverPoint] is not fittest.word[randomCrossOverPoint]:
         fittest.gene[randomCrossOverPoint] = fittest.word[random.randint(0,fittest.geneLength-1)]
    if secondFittest.gene[randomCrossOverPoint] is not secondFittest.word[randomCrossOverPoint]:
        secondFittest.gene[randomCrossOverPoint] = secondFittest.word[random.randint(0,fittest.geneLength-1)]


def offSpring(population,fittest,secondFittest):
    population.indivituals[population.getLeastIndivitual()].gene.clear()
    if fittest.calculateFitness() <= secondFittest.calculateFitness():
        for i in fittest.gene:
            population.indivituals[population.getLeastIndivitual()].gene.append(i)
    else:
        for i in secondFittest.gene:
            population.indivituals[population.getLeastIndivitual()].gene.append(i)

# -- Main --
popSize = 10
word = 'Hello World'
geneLen = len(word)
population = Population(popSize,geneLen,word)
population.calculateFitnessOfIndiviuals()
generationCount = 1
population.printPopulation()
print('Generation:',generationCount)
print('-----------------------')
while population.found() is False:

    fittest = population.getFittestIndivitual()
    secondFittest = population.getSecondFittestIndivitual()
    crossOver(fittest, secondFittest)
    mutation(fittest,secondFittest)
    offSpring(population,fittest,secondFittest)
    generationCount += 1
    population.calculateFitnessOfIndiviuals()
    population.printPopulation()
    print('Generation:',generationCount)
    print('-----------------------')

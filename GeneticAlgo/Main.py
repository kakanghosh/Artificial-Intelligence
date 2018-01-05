import random
class Individual:
    geneLength = 0
    fitness = 0
    def __init__(self,geneLength):
        self.geneLength = geneLength
        self.gene = []
        for i in range(self.geneLength):
            self.gene.append(random.randint(0,10)%2)

    def calculateFitness(self):
        self.fitness = 0
        for i in self.gene:
            if i is 1:
                self.fitness += 1
        return self.fitness

    def showGene(self):
        print(self.gene)

class Population:
    populationSize = 0
    indivituals = []
    copyIndivitual = []
    fitness = []
    fittest = None
    fittestIndivitualIndex = None
    totalFItness = 0

    def __init__(self,populationSize):
        self.populationSize = populationSize
        self.initializePopulation()

    def initializePopulation(self):
        for i in range(self.populationSize):
            self.indivituals.append(Individual(5))

    def calculateFitnessOfIndiviuals(self):
        self.totalFItness = 0
        for i in range(self.populationSize):
           self.totalFItness += self.indivituals[i].calculateFitness()

    def sortIndiviual(self):
        for i in range(len(self.indivituals)):
            for j in range(0,len(self.indivituals)-i-1):
                if self.indivituals[j].fitness < self.indivituals[j+1].fitness:
                    self.indivituals[j], self.indivituals[j+1] = self.indivituals[j+1], self.indivituals[j]

    def copyIndivitual(self,ind):
        n = Individual(5)
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
        print('------------------------')
        print('Total Fitness:', self.totalFItness)

    def isMaximum(self,value):
        for i in self.indivituals:
            if i.fitness is value:
                return True
        return False

def crossOver(fittest,secondFittest):
    randomCrossOverPoint = random.randint(0,4)
    for i in range(randomCrossOverPoint,5):
        fittest.gene[i],secondFittest.gene[i] = secondFittest.gene[i], fittest.gene[i]



def mutation(fittest, secondFittest):
    randomCrossOverPoint = random.randint(0, 4)
    if fittest.gene[randomCrossOverPoint] is 0:
        fittest.gene[randomCrossOverPoint] = 1
    if secondFittest.gene[randomCrossOverPoint] is 0:
        secondFittest.gene[randomCrossOverPoint] = 1

def offSpring(population,fittest,secondFittest):
    population.indivituals[population.getLeastIndivitual()].gene.clear()
    if fittest.calculateFitness() >= secondFittest.calculateFitness():
        for i in fittest.gene:
            population.indivituals[population.getLeastIndivitual()].gene.append(i)
    else:
        for i in secondFittest.gene:
            population.indivituals[population.getLeastIndivitual()].gene.append(i)

# -- Main --
population = Population(10)
population.calculateFitnessOfIndiviuals()
generationCount = 1
population.printPopulation()
print('Generation:',generationCount)
print('-----------------------')
while population.isMaximum(5) is not True:

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

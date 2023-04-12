# Green Beard Altruism

## Authors

- [Tomasz Wojakowski](https://github.com/Wojaqqq)
- [Bartosz Nieroda](https://github.com/qymaensheel)
- [Krzysztof Pala](https://github.com/pallovsky)


# Introduction
The green-beard effect is a thought experiment used in evolutionary biology to explain selective altruism among individuals of a species. The idea of a green-beard gene was proposed by William D. Hamilton in his articles of 1964 and got the name from the example used by Richard Dawkins: "I have a green beard and I will be altruistic to anyone else with green beard" in his work titled The Selfish Gene (1976). A green-beard effect occurs when variations of genes, or a set of linked alleles, produce three expressed or phenotypic effects: 
- a perceptible trait — the hypothetical "green beard”
- recognition of this trait by others
- preferential treatment of individuals with the trait by others with the trait

The green beard individual has the ability of recognizing other individuals carrying the same gene. On this basis he alters his behaviour towards other representatives of his specie and acts altruistically towards them. This behaviour carried among some limited group of specie may cause an effect of prioritization the survival of one of the groups, which greatly affect their further evolution. This effect stands to be a negation in the view of old evolutionary theories which mainly focused on the role of competition between the organisms. In this model the natural selection happen with the context of the gene, which even though causes altruistic behaviours among the specimen, it acts selfish on the level of whole population.
The goal of this simulation is to check the behaviour of this effect in simplified environment and to determine needed variables and their values for this effect to take place. We want to check the limits of its occurrence and also the boundary conditions of the environment which effects the most probable evolutionary path of a specie. This simulation is based on a YouTube video – Simulating Green-Beard Algorithm.

# Implementation
The main component of model we’d like to propose consists of Home entity which represents the living environment for the habitants of our simulation: Blobs which are the representation of the individuals of a particular specie. The blob population is not homogenous – some of the Blob have the green-beard gene and/or altruistic gene, which differs their behaviour in further steps of the simulation. Each day in order to survive the Blobs will go to the forest which contains Trees with fruits that the Blobs will approach to collect. Each tree due to its size can be approached at once by up to two Blobs. The survival of the Blobs is dependable on their successful attempt to eat a fruit from a tree they have approached to. In a perfect scenario the Blobs will collect a fruit and head back towards home where they will be safe. Only in this situation Blobs are able to reproduce themselves creating one or two new Blobs in their places and therefore increase the total number of Blobs population. The reproduced Blobs carry the same gene as their parent, what is a key element of our simulation.
Not all of the scenarios end with the reproduction of the Blobs though. In some of the Trees there may be a predator, which want to eat a Blob. In that case, one of the Blobs near that tree can take an action based on their gene and whether they have a beard. In the final version of our simulation, we will have four possible genes and beard combinations and each one of them will have a different action when a predator is seen:
- True Coward (cowardice gene and no beard) - they don't warn the other blob and run away with a fruit letting the other blob to die
- Unlucky Altruist (altruist gene and no beard) - they warn blobs with beard but nobody warns them because of lack of beard
- True Altruist (green beard altruist gene and beard) - they warn blobs with beard and receive warnings from other altruists
- Impostor Cowards (cowardice gene and beard) - they receive warnings from other altruists but never give ones

When altruist blob spots that the other blob has a beard and there is a predator on a tree it shouts and makes the other blob run away with previously collected fruit. However, he gets the attention of the predator on a tree, which tries to eat him. Then, the Blob will have to rely on his luck to determine if they were able to run away safely or, unfortunately, he is being eaten by the predator.
After calculating blob behaviour for all the available trees, blobs which collected a fruit and therefore survived the next day had will head back home and reproduce. After each day we summarize the population sizes for all types of blobs in order to study the green-beard effect between them. 

# Simulation parameters
Among the simulation parameters we can distinguish following properties:
- Number of Blobs – the value describing the initial size of the total population.
- Number of Trees – number of trees in the forest that will be generated each day of the simulation. Note that this parameter is our only way to control the maximum size of the total population, which also determines the final result of simulation.
- Probability of the presence of a predator on a tree. 
- Probability of a Blob getting eaten after shouting and warning other blob.
- Probability of producing two blobs instead of one during reproduction phase
- Gene distribution – parameter containing each blob type and corresponding percentage of starting population.
- Steps – number of days in the simulation.

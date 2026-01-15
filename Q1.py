import streamlit as st
import numpy as np
import random

POPULATION = 300
CHROM_LENGTH = 80
GENERATIONS = 50
TARGET_ONES = 40

def fitness(chromosome):
    return CHROM_LENGTH - abs(np.sum(chromosome) - TARGET_ONES)

def crossover(p1, p2):
    point = random.randint(1, CHROM_LENGTH - 1)
    return np.concatenate([p1[:point], p2[point:]])

def mutate(chromosome, rate=0.01):
    for i in range(len(chromosome)):
        if random.random() < rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

st.title("Genetic Algorithm Bit Pattern Generator")

population = [np.random.randint(0, 2, CHROM_LENGTH) for _ in range(POPULATION)]
best_scores = []

for gen in range(GENERATIONS):
    scored = [(fitness(ind), ind) for ind in population]
    scored.sort(reverse=True, key=lambda x: x[0])
    best_scores.append(scored[0][0])

    elites = [ind for _, ind in scored[:10]]
    new_pop = elites.copy()

    while len(new_pop) < POPULATION:
        p1, p2 = random.sample(elites, 2)
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)

    population = new_pop

st.write("Best Fitness Over Generations:")
st.line_chart(best_scores)

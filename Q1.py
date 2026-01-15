# File: q1_genetic_algorithm.py
import streamlit as st
import random

st.title("Genetic Algorithm Bit Pattern Generator")

# Fixed parameters
POPULATION_SIZE = 300
CHROMOSOME_LENGTH = 80
MAX_GENERATIONS = 50
TARGET_ONES = 40
MAX_FITENESS = CHROMOSOME_LENGTH

def generate_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def fitness(chromosome):
    return sum(chromosome)

def select(population):
    return random.choices(population, weights=[fitness(c) for c in population], k=2)

def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome, rate=0.01):
    return [1 - gene if random.random() < rate else gene for gene in chromosome]

def run_genetic_algorithm():
    population = [generate_chromosome() for _ in range(POPULATION_SIZE)]
    best_fitness = []
    
    for gen in range(MAX_GENERATIONS):
        population.sort(key=fitness, reverse=True)
        best_fitness.append(fitness(population[0]))
        
        if fitness(population[0]) == TARGET_ONES:
            st.success(f"Target reached at generation {gen}: {population[0]}")
            break
        
        new_population = population[:10]  # Elitism
        
        while len(new_population) < POPULATION_SIZE:
            p1, p2 = select(population)
            c1, c2 = crossover(p1, p2)
            new_population.extend([mutate(c1), mutate(c2)])
        
        population = new_population[:POPULATION_SIZE]
    
    return population[0], best_fitness

if st.button("Run Genetic Algorithm"):
    result, fitness_history = run_genetic_algorithm()
    st.write("Best Chromosome:", result)
    st.write("Fitness Over Generations:", fitness_history)
    st.line_chart(fitness_history)
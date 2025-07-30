#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:53:34 2024

@author: anshuldani
"""

import csv
import sys

def load_data():
    # Load driving distances
    driving_distances = {}
    with open("driving2.csv") as file:
        reader = csv.reader(file)
        states = next(reader)[1:]  # Get state names from the first row
        for row in reader:
            state = row[0]
            driving_distances[state] = {states[i]: int(row[i + 1]) for i in range(len(states))}

    # Load national parks data
    national_parks = {}
    with open("parks.csv") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the first row (headers)
        for row in reader:
            for i in range(1, len(row)):  # Skip the first column
                state = headers[i]  # Get state abbreviation from the header
                national_parks[state] = int(row[i])  # Map state to number of parks

    # Load zones data
    zones = {}
    with open("zones.csv") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the first row (headers)
        for row in reader:
            for i in range(1, len(row)):  # Skip the first column
                state = headers[i]  # Get state abbreviation from the header
                zones[state] = int(row[i])  # Map state to zone value

    return driving_distances, national_parks, zones

def is_assignment_complete(assignment, no_of_parks, national_parks):
    return (
        len(assignment) >= 7 and 
        sum(national_parks[state] for state in assignment) >= no_of_parks
    )

def select_unassigned_variable(assignment, zones, currentzone):
    return currentzone + 1 if currentzone < 12 else None

def order_domain_values(zones, currentzone):
    return sorted([state for state, zone in zones.items() if zone == currentzone])

def inference(csp, var, assignment):
    return True

def backtrack(csp, assignment, no_of_parks, driving_distances, national_parks, zones, currentzone):
    if is_assignment_complete(assignment, no_of_parks, national_parks):
        return assignment

    var = select_unassigned_variable(assignment, zones, currentzone)
    if var is None:
        return None

    for value in order_domain_values(zones, var):
        if is_consistent(assignment, value, driving_distances, zones):
            assignment.append(value)
            inferences = inference(csp, var, assignment)
            if inferences:
                result = backtrack(csp, assignment, no_of_parks, driving_distances, national_parks, zones, var)
                if result:
                    return result
                assignment.pop()  # backtrack if unsuccessful
    return None

def is_consistent(assignment, newstate, driving_distances, zones):
    if not assignment:
        return True
    laststate = assignment[-1]
    lastzone = zones[laststate]
    newzone = zones[newstate]
    
    # Ensure new state is in the next zone westward
    if newzone != lastzone + 1:
        return False

    # Check direct road connection between laststate and newstate
    return driving_distances[laststate].get(newstate, -1) > 0

def backtracking_search(csp, no_of_parks, driving_distances, national_parks, zones, initialstate):
    assignment = [initialstate]
    initialzone = zones[initialstate]
    return backtrack(csp, assignment, no_of_parks, driving_distances, national_parks, zones, initialzone)

def main():
    if len(sys.argv) != 3:
        print("ERROR: Not enough or too many input arguments.")
        sys.exit(1)

    initialstate = sys.argv[1]
    no_of_parks = int(sys.argv[2])

    driving_distances, national_parks, zones = load_data()
    csp = {}  # Initialize CSP as needed, or pass required data directly

    solution = backtracking_search(csp, no_of_parks, driving_distances, national_parks, zones, initialstate)

    if solution:
        path_cost = sum(driving_distances[solution[i]][solution[i + 1]] for i in range(len(solution) - 1))
        parks_visited = sum(national_parks[state] for state in solution)
        print("Dani, Anshul Kaushalbhai, A20580060 Solution:")
        print(f"Solution path: {', '.join(solution)}")
        print(f"Number of states on a path: {len(solution)}")
        print(f"Path cost: {path_cost}")
        print(f"Number of national parks visited: {parks_visited}")
    else:
        print("Solution path: FAILURE: NO PATH FOUND\nNumber of states on a path: 0\nPath cost: 0\nNumber of national parks visited: 0")

if __name__ == "__main__":
    main()

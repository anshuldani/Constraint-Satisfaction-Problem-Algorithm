This project uses a Constraint Satisfaction Problem (CSP) and backtracking search to solve a road trip planning problem across the contiguous United States.

Problem Description
The United States is represented as a graph, where:

Each node is a U.S. state (or D.C.), grouped into 12 zones (Z1 to Z12).

Each node is labeled with the number of national parks in that state.

Edges between nodes represent direct borders between states (undirected graph).

Travel is only allowed westward from lower zone numbers to higher zone numbers.

Objective

Plan a valid road trip path starting in any state (from any zone) and ending in a state within zone Z12 (CA, NV, OR, or WA), visiting exactly one state per zone between the start zone and zone Z12. 

The trip must:

Form a connected path through valid neighboring states.

Accumulate at least NO_OF_PARKS total national parks across all visited states.

Key Constraints

You must assign one state per zone from your start zone through Z12.

You may start in any zone/state, but the zone determines the number of zones to traverse.

You must only select neighboring states per zone (i.e., states that are directly connected).

You must visit all national parks in any state you travel through.

PARKS_VISITED keeps a cumulative total of national parks visited.

The total parks visited must satisfy: PARKS_VISITED >= NO_OF_PARKS.

Assumptions

Each zone variable Z1–Z12 has a list of states as domain values.

A valid assignment must include all zones between (and including) start and end zones.

The search uses backtracking with CSP.

State-to-state adjacency is determined using driving distances between capitals.

Example

If you start in TN (Zone Z6), then your zone variables are:

Z6 -> Z7 -> Z8 -> Z9 -> Z10 -> Z11 -> Z12

Your solution will assign one valid, neighboring state to each of these zones

You must end in CA, NV, OR, or WA (zone Z12)

Implementation Notes

The backtracking algorithm checks for path validity and national park constraints.

State neighbors and park counts are pre-defined based on the map.

A final path is valid if:

It includes exactly one state per zone from start to Z12

It respects adjacency constraints

Total parks visited >= NO_OF_PARKS

This project models real-world constraints in a fun, geographical CSP challenge and helps develop core skills in search algorithms, constraint modeling, and Python logic programming.


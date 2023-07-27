#!/bin/python3

import os
import sys

def best_total_score(config):
    N, V, P = config
    routes = [(0, 0)] 
    for step in range(1, N):
        
        if not routes:
            print("all routes failed")
            return None
        this_score = V[step - 1]
        this_energy = P[step-1]
        
        if this_energy > 0:
            
            all_max_score = max([route_max_score for (energy, route_max_score) in routes])
            takeEnergy = (this_energy - 1, all_max_score)
            
            newRoutes = [(energy - 1, route_max_score + this_score) for (energy,  route_max_score) in routes if (energy > this_energy or (energy > 0 and route_max_score+this_score > all_max_score))]
            newRoutes.append(takeEnergy)
        else:
            newRoutes = [(energy - 1, route_max_score + this_score) for (energy, route_max_score) in routes if energy > 0]
        routes = newRoutes
    this_score = V[N - 1]
    return max(route_max_score for (energy, route_max_score) in routes) + this_score

def robot(vp):
    N = len(vp)
    V = []
    P = []
    for [vi, pi] in vp:
        V.append(vi)
        P.append(pi)
    config = (N,V,P)
    return best_total_score(config)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    vp = []
    for _ in range(n):
        vp.append(list(map(int, input().rstrip().split())))
    result = robot(vp)
    fptr.write(str(result) + '\n')
    fptr.close()

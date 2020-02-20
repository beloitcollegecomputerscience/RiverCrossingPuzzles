#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:18:09 2020

@author: Wadood
"""

wholeFile = []
items = []
beginLeft = []
beginBoat = []
beginRight = []
boatIncompatiable = {}
boatOccupancy = 0
teams = []
teamIncompatible = {}
immovables = []
pilot = "abc"
isIsland = False

file = open(r"rules.txt")
wholeFile = file.readlines()

for x in range(0,4):
    items = wholeFile[x]
    
    #print(items)
    
for x in range(5,11):
    beginLeft = wholeFile[x]
    
    #print(beginLeft)
    
for x in range(12,14):
    beginBoat = wholeFile[x]
    
    #print(beginBoat)
    
for x in range(17,20):
    beginRight = wholeFile[x]
    
   # print(beginRight)
    
for x in range(22,24):
    beginIncompatiable = wholeFile[x]
    
   # print(beginIncompatiable)

boatOccupancy = wholeFile[24]
#print(boatOccupancy)

for x in range(27,28):
    teams = wholeFile[x]
    
    #print(teams)
    
for x in range(28,30):
    teamIncompatiable = wholeFile[x]
    
    #print(teamIncompatiable)
    
for x in range(30,32):
    immovables = wholeFile[x]
    
    #print(immovables)
    
for x in range(33,35):
    pilot = wholeFile[x]
    
    #print(pilot)    
    
isIsland = wholeFile[37]
#print(isIsland)

    


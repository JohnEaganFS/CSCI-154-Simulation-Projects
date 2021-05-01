# CSCI-154-Simulation-Projects
This repo contains my three simulation projects for CSCI 154.
The 3 projects are:
1. Monty Hall Problem - Monte Carlo Methods
2. Blackjack - Monte Carlo Methods
3. Bank & Tellers - Discrete Event Simulation

Within each project folder, there are 3-4 primary files of code that I used to test and produce my experimental results.
The important files for each project are listed below (**bold** = implementation, *italic* = data gathering/output)

----------
Monty Hall
----------
1. main.py - Driver function to test different variants of Monty Hall Problem (MHP). Feel free to mess around with different values and see how the results differ.
2. **customProblem.py** - Contains the majority of my code for the Monty Hall Problem variations. Look here for most of the implementation.
3. **generalFunctions.py** - Some general functions I used often enough that I decided to include them as a separate module. Also includes some code for implementing MHP.
4. *test.py* - The actual file I ran to gather my data. It imports and calls from customProblem.py. Note that this took very long to process so I suggest reducing the iterations if you want to run it yourself (~1 day).

---------
Blackjack
---------
1. main.py - Driver function for variants of Blackjack and Player Strategies.
2. **customGame.py** - Main implementation of Blackjack and variations.
3. *test.py* - Data gathering file. Once again, I suggest reducing iteration count (~12 hours)

--------------
Bank & Tellers
--------------
1. **customTeller.py** - Contains implementation of a general bank & teller situation as well as a priority queue for light requests. Look here for implementation.
2. *test.py* - Data gathering file. Quite fast so don't worry about iteration count (<1 min)
3. main.py - Small driver function for custom variations. Feel free to mess around.
4. Every other file - All just the different variations I wanted to test out. Implementation is the same as in customTeller.py just for different scenarios.

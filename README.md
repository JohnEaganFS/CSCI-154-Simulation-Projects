# CSCI-154-Simulation-Projects
This repo contains my three simulation projects for CSCI 154.
The 3 projects are:
1. Monty Hall Problem - Monte Carlo Methods
2. Blackjack - Monte Carlo Methods
3. Bank & Tellers - Discrete Event Simulation

Within each project folder, there are 3-4 primary files of code that I used to test and produce my experimental results.
The important files for each project are listed below:

----------
Monty Hall
----------
1. main.py - Driver function to test different variants of Monty Hall Problem (MHP). Feel free to mess around with different values and see how the results differ.
2. customProblem.py - Contains the majority of my code for the Monty Hall Problem variations. Look here for most of the implementation.
3. generalFunctions.py - Some general functions I used often enough that I decided to include them as a separate module. Also includes some code for implementing MHP.
4. test.py - The actual file I ran to gather my data. It imports and calls from customProblem.py. Note that this took very long to process so I suggest reducing the iterations if you want to run it yourself (~2 days).

---------
Blackjack
----------

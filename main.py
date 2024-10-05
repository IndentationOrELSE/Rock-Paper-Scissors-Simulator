# INIT
import random
import matplotlib.pyplot as plt
import numpy as np

# Initialize lists to store match results
matches = []
random_wins = []
not_random_wins = []
draws = []
copy_wins = []
against_copyist = [0]

# Define cycle for Rock-Paper-Scissors (1: Rock, 2: Paper, 3: Scissors)
cycle = [1, 2, 3]

# Initialize win counters
RANDOM_WINS = 0
NOT_RANDOM_WINS = 0
DRAWS = 0
COPY_WINS = 0

# WIN LOGIC

"""
Determine the winner of a Rock-Paper-Scissors game between two players.
    
    Parameters
    ----------
    player1 : int
        The choice of player 1 (0: Rock, 1: Paper, 2: Scissors)
    player2 : int
        The choice of player 2 (0: Rock, 1: Paper, 2: Scissors)
    player1_name : str
        The name of player 1
    player2_name : str
        The name of player 2
    
    Returns
    -------
    str
        The name of the winner (or "Tie" if it's a draw)
    """
def determine_winner(player1, player2, player1_name, player2_name):
	results = [
    	["Tie", player2_name, player1_name],
    	[player1_name, "Tie", player2_name],
    	[player2_name, player1_name, "Tie"]
	]
	return results[player1][player2]

# SIMULATION
for i in range(100000):
    matches.append(i)
    not_randomist = (cycle[i % 3]) - 1
    randomist = random.randint(0, 2)
    copyist = against_copyist[-1]

    result1 = determine_winner(randomist, not_randomist, "randomist", "not_randomist")
    result2 = determine_winner(randomist, copyist, "randomist", "copyist")

    against_copyist.append(randomist)
    copyist = against_copyist[-1]

    result3 = determine_winner(not_randomist, copyist, "not_randomist", "copyist")

    against_copyist.append(not_randomist)
    results = [result1, result2, result3]

    for result in results:
        if result == "randomist":
            RANDOM_WINS += 1
        elif result == "not_randomist":
            NOT_RANDOM_WINS += 1
        elif result == "copyist":
            COPY_WINS += 1
        else:
            DRAWS += 1

    not_random_wins.append(NOT_RANDOM_WINS)
    random_wins.append(RANDOM_WINS)
    copy_wins.append(COPY_WINS)
    draws.append(DRAWS)

# GRAPH PLOTTING
matches = np.array(matches)
plt.title('Rock Paper Scissors')
plt.xlabel('Matches')
plt.ylabel('Wins')
plt.grid()
plt.plot(matches, random_wins, label="Random Wins")
plt.plot(matches, not_random_wins, label="Structured Wins")
plt.plot(matches, draws, label="Draws")
plt.plot(matches, copy_wins, label="Copy Wins")

# Final results output
print(f'RANDOM WINS: {RANDOM_WINS}, STRUCTURED Wins: {NOT_RANDOM_WINS}, DRAWS: {DRAWS}, COPY WINS: {COPY_WINS}')
plt.legend()
plt.show()

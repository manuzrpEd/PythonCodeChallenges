'''
Given the numbers of players and available courts, calculate the maximum number of parallel tennis games.
P players, who will take part in the first round of this tournament, are already registered and you have reserved C tennis courts for the matches.
Exactly two players play in each game and only one game can be played on each court at any given time.
You want to host the maximum possible number of games starting at the same time (in order to finish the first round quickly).
Write a function:
https://app.codility.com/programmers/trainings/3/tennis_tournament/
    def solution(P, C)

that, given the number of players P and the number of reserved courts C, returns the maximum number of games that can be played in parallel.
'''

def solution(P, C):
    assert type(P) is int
    assert type(C) is int
    if (P % 2) != 0:
        courts_needed = round((P / 2) - 0.5)
    else:
        courts_needed = round(P / 2)
    if courts_needed > C:
        return C
    else:
        return courts_needed

# Examples:
'''
1. Given P = 5 players and C = 3 available courts, the function should return 2. 
Two games can be played simultaneously (for instance, the first and second players can play on the first court, 
and the third and fourth players on the second court, and the third court will be empty because the fifth player does not have a partner to play with).
'''
P = 5
C = 3
print("\n Solution: ", solution(P, C))

'''
2. Given P = 10 players and C = 3 courts, the function should return 3. At most three games can be hosted in parallel.
'''
P = 10
C = 3
print("\n Solution: ", solution(P, C))

P = 25
C = 30000
print("\n Solution: ", solution(P, C))

P = 2
C = 30000
print("\n Solution: ", solution(P, C))
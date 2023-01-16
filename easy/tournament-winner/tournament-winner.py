# # Time complexity: O(n) where n is the number of competitions. 
# Space complexity: O(m) where m is the number of teams who have won at least once.
def tournament_winner(competitions, results):
    absolute_winner = ""
    teams = {}
    
    for match in range(len(competitions)):
        if results[match] == 1:
            winner = competitions[match][0]
        else:
            winner = competitions[match][1]

        if winner in teams:
            teams[winner] += 1
        else:
            teams[winner] = 1

        if teams[winner] == len(competitions) - 1:
            absolute_winner = winner
            return absolute_winner


print(tournament_winner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
], [0, 0, 1]))
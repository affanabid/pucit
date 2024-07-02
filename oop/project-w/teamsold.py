import random

class Team:
    def __init__(self , id , team_name , captain_name , coach_name):
        self.id = id
        self.team_name = team_name
        self.captain_name = captain_name
        self.coach_name = coach_name


    def __str__(self):
        return f'Team ID: {self.id}\nTeam Name: {self.team_name}\nCaptain: {self.captain_name}\nCoach: {self.coach_name}'

class Points:
    def __init__(self , team_name , matches_played , won , lost , draw):

        if any(val < 0 for val in [matches_played, won, lost, draw]):
            raise ValueError("Number of matches, wins, losses, and draws must be non-negative.")
        
        self.team_name = team_name
        self.matches_played = matches_played
        self.won = won
        self.lost = lost
        self.draw = draw
        self.points = self.won * 2


    def show_details(self):
        header = f"{'Team Name':<15}{'Matches Played':<20}{'Won':<10}{'Lost':<10}{'Draw':<10}{'Points':<10}"
        data = f"{self.team_name:<15}{self.matches_played:<20}{self.won:<10}{self.lost:<10}{self.draw:<10}{self.points:<10}"

        print(header)
        print(data)

# obj = Points('Lost Boys',4,3,1,0)
# obj.show_details()

class Match:
    def __init__(self , date , match_no , team1 , team2 , overs , match_type):
        self.date = date
        self.match_no = match_no
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.match_type = match_type
        
    def __str__(self):
        return f'{self.match_type}\nDate: {self.date }\nMatch Number: {self.match_no}\nTeams: {self.team1} v/s {self.team2}\nOvers: {self.overs}'

# obj = Match('10/02/2024',4,'Lost Boys','Falcons',6,'Semi Finals')
# print(obj)

class Toss:
    def __str__(self):
        # random.choice = always 2 arguments only 
        self.toss_result = random.choice(["Heads" , "Tails"])
        return self.toss_result

# toss_winner = Toss()
# print(f"Toss Result: {toss_winner}")

class Result:
    def __init__(self ,team1 , team2 , team1_final_score , team2_final_score):
        self.team1 = team1
        self.team2 = team2
        self.team1_final_score = team1_final_score
        self.team2_final_score = team2_final_score
    
    def __str__(self):
        if self.team1_final_score > self.team2_final_score:
            return f'{self.team1} won by {self.team1_final_score} runs'
        else:
            return f'{self.team2} won by {self.team2_final_score} runs'

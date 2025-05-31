scoring = {1: 10, 2: 8, 3: 6, 4: 4, 5: 2, 6: 1}

def assign_scores(event, rankings):
    print(f"\nAssigning scores for {event}:")
    for rank, team in enumerate(rankings, start=1):
        if rank <= 6:
            score = scoring[rank]
            teams[team]['scores'].append(score)
            print(f"{team} - {score} points")
        else:
            print(f"{team} - No points")

def calculate_total_scores():
    total_scores = {}
    for team, data in teams.items():
        total_scores[team] = sum(data['scores'])
    return total_scores

def display_results():
    total_scores = calculate_total_scores()
    sorted_teams = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
    print("\nFinal Rankings:")
    for rank, (team, score) in enumerate(sorted_teams, start=1):
        print(f"{rank}. {team} - {score} points")

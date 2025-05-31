def main():
    for event in events:
        rankings = input(f"\nEnter the rankings for {event} (comma-separated): ").split(',')
        rankings = [team.strip() for team in rankings]
        assign_scores(event, rankings)

    display_results()

if __name__ == "__main__":
    main()

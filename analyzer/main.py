from ff_espn_api import League



if __name__ == "__main__":
    league = League(league_id=1360211, year=2019, debug=True)

    for team in league.teams:
        print(team)

    print(league)
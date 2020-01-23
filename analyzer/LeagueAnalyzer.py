from ff_espn_api import League
from datetime import date

class LeagueAnalyzer(object):
    def __init__(self, id):
        self.id = id
        self.years = self.getYears(2019, sum=0)
        self.league = self.getLeague(id)

    def getYears(self, year, sum):
        return 1
        try:
            l = League(league_id=self.id, year=year, debug=True)
            return self.getYears(year - 1, sum + 1)
        except:
            return sum

    def getLeague(self, id):
        return League(league_id=self.id, year=2019, debug=True)
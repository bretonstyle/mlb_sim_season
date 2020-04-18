import statsapi
from pprint import pprint
from baseball.database import ScheduleDB
import configparser

class Schedule:

    def retrieve_schedule(self):
        self.schedule_db = ScheduleDB()
        # TODO: Error handle the DB stuff in case it doesn't exist (god this code is messy)
        self.schedule_db.drop_schedule()
        self.schedule_db.add_schedule()
        self.schedule_list = []
        raw_schedule = []
        raw_schedule.append(statsapi.schedule(start_date='01/01/2010', end_date='12/31/2010', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2011', end_date='12/31/2011', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2012', end_date='12/31/2012', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2013', end_date='12/31/2013', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2014', end_date='12/31/2014', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2015', end_date='12/31/2015', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2016', end_date='12/31/2016', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2017', end_date='12/31/2017', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2018', end_date='12/31/2018', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='01/01/2019', end_date='12/31/2019', team="147"))
        raw_schedule.append(statsapi.schedule(start_date='10/05/2019', end_date='12/31/2019', team="147"))
        pprint(raw_schedule[0])
        for x in raw_schedule:
           incrementer = 1
           for y in x:
                if y['status'] != 'Final':
                    continue
                else:
                    print(y['game_date'] +  "   " + y['winning_team'] + " WON OVER " + y['losing_team'])
                    self.schedule_db.add_entry(game_id_pass=y['game_id'], winning_team_pass=y['winning_team'],
                                               losing_team_pass=y['losing_team'], away_score_pass=y['away_score'],
                                               home_score_pass=y['home_score'], game_date_pass=y['game_date'])
                    incrementer= incrementer+1

schedule=Schedule()
schedule.retrieve_schedule()

# for x in raw_sched:
    #     if x['game_type'] == 'S':
    #
    #     else:
    #         print('Game Type: Something Else')



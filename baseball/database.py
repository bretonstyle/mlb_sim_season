from sqlalchemy import MetaData, Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class ScheduleDB(Base):

    __tablename__ = 'schedule'
    column_id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer)
    home_score = Column(Integer)
    away_score = Column(Integer)
    winning_team = Column(String)
    losing_team = Column(String)
    game_date = Column(Date)
    engine = create_engine(config['conn_string'])
    DBSession = sessionmaker(bind=engine)

    def add_entry(self, game_id_pass, winning_team_pass, losing_team_pass,
                  game_date_pass, home_score_pass, away_score_pass):
        new_game = ScheduleDB(game_id=game_id_pass,
                              winning_team=winning_team_pass,
                              losing_team=losing_team_pass,
                              game_date=game_date_pass,
                              home_score=home_score_pass,
                              away_score=away_score_pass)
        session = self.DBSession()
        session.add(new_game)
        session.commit()

    def drop_schedule(self):
        ScheduleDB.__table__.drop(self.engine)

    def add_schedule(self):
        Base.metadata.create_all(self.engine)


# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()



# Insert a game into the schedule table
# new_game = ScheduleDB(game_id=500, winning_team = "New York Yankees", losing_team="Boston Red Sox", game_date="04/18/2020", home_score="16", away_score = "1")
# session.add(new_game)
# session.commit()




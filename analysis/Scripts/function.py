

import pandas as pd


def load_process(path):
    data = (pd.read_csv(path)
              .drop(['MIN', 'FGM', 'FGA', 'FG%', '3PM', '3PA',
               '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK',
               'TOV', 'PF', 'EFF', 'AST/TOV', 'STL/TOV'], axis=1)
           .dropna()
           .rename(columns={'PTS':'Points','Pos':'Position'})
           )
    data.to_csv('../data/processed/data.csv')
    return data
import pandas as pd
import numpy as np
import webbrowser as wb

#website='http://en.wikipedia.org/wiki/NFL_win-loss_records'
#wb.open(website)

nfl_frame=pd.read_clipboard()
print(nfl_frame)
print("First five columns in table:")
print(nfl_frame.head())

print("Heading of the table:")
print(nfl_frame.columns)

print(nfl_frame.Team.head(3))

print(pd.DataFrame(nfl_frame,columns=['Team','First NFL season','Total Games']))

print(nfl_frame.head())

print(nfl_frame.loc[3])

nfl_frame['Stadium']='Levis sadium'

print(nfl_frame)
import os
import pandas as pd

from cosine_sim import PlayerRecommendationSystem as prs

while True:
    os.system('clear')
    lookup_name = input('/n/nPlayer Name: ')
    subset = 
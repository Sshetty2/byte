
import pandas as pd
import numpy as np
import os

from sklearn.neighbors import NearestNeighbors

class PlayerCompSystem(object):
    """Python class for creation, training, and comparison of data using cosine
    similarity. The algorithm will filter and return indices of the data, so
    these indices should be in a format that the user will understand.

    Arguments:

    comparison_matrix -- a pandas DataFrame consisting entirely of numerical
        values, and indices that are useful to the viewer
    """

    def __init__(self, comparison_matrix):
        self.matrix = comparison_matrix
#        self.lookup_matrix = pd.read_csv('football_lookup.csv')

    def get_row(self, name):
        """Takes in an athlete name, and returns the row with that index
        
        Arguments:

        name -- (str) the name of the player we want to compare to
        matrix -- (DataFrame) the DataFrame that we are querying
        """
        #row = self.lookup_matrix.loc[self.slookup_matrix.index==name]
        row = self.matrix.loc[self.matrix.index==name][:1]

        print(row)
        return row, row['Age']

    def near_neighbors(self, age):
        """Use our input matrix to generate and train a cosine similarity model
        to judge similarity between each row in our data. Returns trained model

        Arguments:

        age -- (int) the age of player we are comparing
        """
        model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.age_matrix = self.matrix#.loc[self.matrix['Age']==age]
        model.fit(self.age_matrix)
        return model

    def rec_by_users(self, name, neighbors=11):
        """Use our matrix to create a model, train it, and return the n-most
        similar indices from our data.

        Arguments:

        name -- The index position of the player we want to compare
        age -- the age of the player we are comparing, to filter for only
            historical data at that age
        neighbors -- number of similar players to return. This model returns 
            our query player as its first result, so this must be equal to
            (number of comparables + 1) (default is 11)
        """
        test_player, age = self.get_row(name)
        input('Train')
        model = self.near_neighbors(age)
        if len(self.age_matrix) < neighbors:
            neighbors = len(self.age_matrix)
        input('Return similarities')
        distances, indices = model.kneighbors(
            test_player.values.reshape(1, -1), n_neighbors=neighbors)
        
        #print(distances[:4], indices[:4])
        
        for i in range(0, len(distances.flatten())):
            if i == 0:
                print('Recommendations for {0} ({1}):\n'.format(
                            name, distances.flatten()[0]))
            else:
                print('{0}: {1}, {2}'.format(
                    i, self.matrix.index[indices.flatten()[i]], 
                                        distances.flatten()[i].round(5)))


if __name__=='__main__':
    df = pd.read_csv('football_total.csv', index_col='Unnamed: 1')
    recs = PlayerCompSystem(df)
    while True:
        os.system('clear')
        player = input('\nWho would you like to compare?\n')
        recs.rec_by_users(player)
        input()

"""
The purpose of this file is to hold various sql queries to be used in utilities functions
"""

import sqlite3 as sql3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DBQueries:

    def __init__(self):
        self.conn = sql3.connect('expense_tracker.db')
        self.cursor = self.conn.cursor()

    def get_data(self, file):
        data = pd.read_csv(file)
        attributes = ['hrk','vendor', 'date', 'description','meansofpayment','city', 'category', 'currency','country']
        new_data = data[attributes]
        new_data.rename(columns={'hrk': 'cost'}, inplace=True)
        return new_data
    
    def run(self):
        file = 'expences1.csv'
        data = self.get_data(file)
        data.to_sql('expense', self.conn, index=False, if_exists='replace')
    
if __name__ == '__main__':
    data_obj = DBQueries()
    data_obj.run()


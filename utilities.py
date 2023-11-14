"""
The main purpose of this file is to provide various functions to carry out CRUD operaitions
"""

import sqlite3 as sql3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Utilities:

    def __init__(self):
        self.conn = sql3.connect('expense_tracker.db')
        self.cursor = self.conn.cursor()

    def get_all_data(self):
        sql = """
        select * from expense
        """
        res = self.cursor.execute(sql)
        return res.fetchall()

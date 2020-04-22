#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from example.introduction_class import IntroductionClass
import pandas as pd

class testClass(IntroductionClass):

    def read_data(self):
        df = pd.read_csv('/Users/MatthewPrzybyla/Downloads/DummyData_Page 1_Time series.csv')
        df['Date'] = pd.to_datetime(df['Year Month'])
        self.data = df
        return self.data.head()


# %%

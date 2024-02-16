# Importing the required libraries
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# Loading and exploring the data
df = pd.read_csv('output_svenska.csv')

#preprocessing
df['Obestämd Vokalratio'] = pd.cut(df['Obestämd Vokalratio'], bins=10, labels=False)
df['Bestämd Vokalratio'] = pd.cut(df['Bestämd Vokalratio'], bins=10, labels=False)
df['Obestämd Ord Längd'] = pd.cut(df['Obestämd Ord Längd'], bins=10, labels=False)
df['Bestämd Ord Längd'] = pd.cut(df['Bestämd Ord Längd'], bins=10, labels=False)


# Hot encoding the Data
df_encoded = pd.get_dummies(df)


frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
print(rules.head())


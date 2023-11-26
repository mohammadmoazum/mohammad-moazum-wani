# Import pandas library
import pandas as pd

# initialize list elements
data = [10,20,30,40,50,60]

# # Create the pandas DataFrame with column name is provided explicitly
df3 = pd.DataFrame(data, columns=['Numbers'])
print("printintg the list",df3)
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
df2 = pd.DataFrame( columns=['Name', 'Age'])


# print dataframe.
print("printing dataframes",df)
print("printing dataframes",df2)



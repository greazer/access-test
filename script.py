# %% [markdown]
# ## Install needed packages
# Just need to do this once, either here or in a terminal with your conda environment activated.
#%%
%conda install pyodbc
# Installing with pip because sqlalchemy-access is not available via conda. 
# Use pip as a fallback in this case.
%pip install sqlalchemy-access

#%% [markdown]
# ## Connect with pure ODBC driver
# Just to make sure we have something that could possibly work.


#%%
import pyodbc
conn = pyodbc.connect(r'DSN=access-test')
cursor = conn.cursor()
cursor.execute('select * from Table1')

# %%
for row in cursor.fetchall():
    print(row)
    
#%% [markdown]
# ## Pandas and SQLAlchemy 
# Now let's use Pandas and SQLAlchemy instead


# %%
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("access+pyodbc://@access-test")
cnx = engine.connect()
# %%
df = pd.read_sql_table('Table1', cnx)
df.head()
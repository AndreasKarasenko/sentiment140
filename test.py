#%%
import zipfile
import pandas as pd
z = zipfile.ZipFile("./trainingandtestdata.zip")
names = z.namelist()
print(names)
col_names = ["sentiment", "tweet_id", "date", "query", "user_name", "message"]
files = [pd.read_csv(z.open(i),encoding="ISO-8859-1",
                     delimiter=",", quotechar='"', header=None, names=col_names) for i in names]
# %%
test = files[0]
# %%
test.head()
# %%

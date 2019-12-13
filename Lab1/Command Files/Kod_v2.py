
import pandas as pd

df=pd.read_csv("./TIER Protocol Documentation/Analysis Data/tb.csv")
df = pd.melt(df, id_vars=["iso2","year"], value_name="cases", var_name="sex_and_age")

tmp_df = df["sex_and_age"].str.extract("(\D)(\d+)(\d{2})")
tmp_df.columns = ["sex", "age_lower", "age_upper"]
tmp_df["age"] = tmp_df["age_lower"] + "-" + tmp_df["age_upper"]

df = pd.concat([df, tmp_df], axis=1)
df = df.drop(['sex_and_age',"age_lower","age_upper"], axis=1)
df = df.dropna()
df = df.sort_values(ascending=True,by=["iso2", "year", "sex", "age"])
print(df.head(10))
df.to_csv("./TIER Protocol Documentation/Analysis Data/demtb.csv", index=None)


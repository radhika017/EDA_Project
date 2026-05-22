import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\radhi\OneDrive\Desktop\CS\Data analysis\Exploratory Data Analysis (EDA)\EDA_Project\netflix_titles.csv")

# View data
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Statistical summary
print(df.describe())

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
plt.show()

# Histogram
df.hist(figsize=(10,10))
plt.show()

# Boxplot
sns.boxplot(data=df.select_dtypes(include='number'))
plt.show()
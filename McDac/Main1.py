import pandas as pd
df = pd.read_csv("menu.csv")
sp=[]
def sod(arg):
    if arg >50:
        arg = None
        return arg
    return arg 

def car(arg):
    if arg >20:
        arg = None
        return arg
    return arg 

def diet(arg):
    if arg >19:
        arg = None
        return arg
    return arg

def prot(arg):
    if arg >17:
        arg = None
        return arg
    return arg

def sug(arg):
    if arg >15:
        arg = None
        return arg
    return arg

def chol(arg):
    if arg >30:
        arg = None
        return arg
    return arg

def fats(arg):
    if arg >20:
        arg = None
        return arg
    return arg

def cal(arg):
    if arg>485 or arg==0:
        arg=None
        return arg
    return arg
df["Calories"]=df["Calories"].apply(cal)
df["Total Fat (% Daily Value)"]=df["Total Fat (% Daily Value)"].apply(fats)
df["Cholesterol (% Daily Value)"]=df["Cholesterol (% Daily Value)"].apply(chol)
df["Sugars"]=df["Sugars"].apply(sug)
df["Protein"]=df["Protein"].apply(prot)
df["Dietary Fiber (% Daily Value)"]=df["Dietary Fiber (% Daily Value)"].apply(diet)
df["Carbohydrates (% Daily Value)"]=df["Carbohydrates (% Daily Value)"].apply(car)
df["Sodium (% Daily Value)"]=df["Sodium (% Daily Value)"].apply(sod)
df=df.dropna()
#print(df["Carbohydrates (% Daily Value)"].min())

print(df.info())

#print(df["Sodium (% Daily Value)"].head())
#print(df["Dietary Fiber (% Daily Value)"].head())
#print(df["Calories"].head())
#print(df["Sugars"].head())
#print(df["Total Fat (% Daily Value)"].head())
#print(df["Cholesterol (% Daily Value)"].head())
#print(df["Protein"].head())
#print(df["Carbohydrates (% Daily Value)"].head())

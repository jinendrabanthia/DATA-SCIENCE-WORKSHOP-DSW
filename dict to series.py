import pandas as pd
sd={'adi':67985346,"sus":345434878,"jay":6786876876,"raj":6786876876,"man":6786876876}
s=pd.Series(sd)
s.to_dict()
print(s)
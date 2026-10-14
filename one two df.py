import pandas as pd
d={"one":pd.Series([10,20,30,40],index=["a","b","c","d"]),
"two":pd.Series([50,60,70,80],index=["a","b","c","d"])}
print(pd.DataFrame(d))
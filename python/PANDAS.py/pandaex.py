'''import pandas as pd
df = pd.DataFrame()
print(df)

import pandas as pd
lst=['BITM','ballari','karnataka']
df=pd.DataFrame(lst)
print(df)

import pandas as pd
names=['vaishu','harshi','deepu','tanu','sneha']
branch=['ece','cse','mech','eee','ai']
list_of_data=list(zip(names,branch))
names.append('teju')
branch.append('ece')
list_of_data=list(zip(names,branch))
df=pd.DataFrame(list_of_data,columns=['name','branch'])
for n,b in list_of_data:
    print(n,b)

import pandas as pd
brands=['iphone','samsung','redmi']
prices=[79999,54000,67000]
data=list(zip(brands,prices))
df=pd.DataFrame(data,columns=['brands','price'])
print(df)'''

import pandas as pd
menu={
    'briyani':500,
    'milkshake':250,
    'gobi':100
     }
df=pd.DataFrame.from_dict(menu,orient='index')
print(df)
'''python 

import pandas as pd 
import re

input_file1= open("C:\\Users\\hp\\Desktop\\Kalyani\\Python\\data.txt", "rt")
output_file1= open("C:\\Users\\hp\\Desktop\\Kalyani\\Python\\outputfile1.txt","wt")

for line in input_file1:
   line=(re.sub(' +','\t',line.strip()) ) +'\n'
   output_file1.write(line)

input_file1.close()
output_file1.close()

output_file1 = pd.read_csv("C:\\Users\\hp\\Desktop\\Kalyani\\Python\\outputfile1.txt",  delimiter = '\t')
output_file1.to_csv('C:\\Users\\hp\\Desktop\\Kalyani\\Python\\data_csv.csv', index = None)

#print(output_file1['yyyy'][0:15] )  print( output_file1['mm'][0:12])
new_df= pd.DataFrame(columns =output_file1.keys())

x=0
y=11

def argxy(x,y):
    arg= output_file1.loc[x:y]
    return(arg_var)
     
def avg(arg):
    yr=int(output_file1['yyyy'][x:y].mean())
    avg_tmax=float(output_file1['tmax'][x:y].mean())
    avg_tmin=float(output_file1['tmin'][x:y].mean())
    avg_af=float(output_file1['af'][x:y].mean())
    avg_rain=float(output_file1['rain'][x:y].mean())
    #avg_sun=float(output_file1['sun'][x:y].mean())
    
    new_row = {'yyyy':yr, 'mm':12, 'tmax':avg_tmax, 'tmin':avg_tmin, 'af':avg_af,'rain':avg_rain,'sun':12}
    return new_row
 
for i in range(5):
    arg_var=argxy(x,y)
    x=y+1
    y=x+11
    new_row=avg(arg_var)
    new_df=new_df.append(new_row, ignore_index=True)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

new_df.plot.bar(x = 'yyyy', y = ['tmax', 'tmin'], rot = 40, ax = ax)
for p in ax.patches: 
    ax.annotate(np.round(p.get_height(),decimals=2), (p.get_x()+p.get_width()/2., p.get_height()))

new_df.plot(x="yyyy", y="af", kind="bar")
new_df.plot(x="yyyy", y="rain", kind="bar")


'''

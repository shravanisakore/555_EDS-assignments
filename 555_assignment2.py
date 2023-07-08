product_details=[]
supplier_details={}
customer_details=[]
Gender={}
fp=open("D:\Sales.csv","r")
while(True):
    data=fp.readline()
    if not data:
      break;
     #print(data)
    data=data.replace("\n","")
    temp=data.split(",")
    product_details.append(temp[1]) 
    customer_details.append(temp[3])
    supplier_details.update({temp[0]:temp[2]})
    Gender.update({temp[3]:temp[4]})
fp.close()
customer_details=tuple(customer_details)
print(type(customer_details))
print("product_details",product_details,)
print("customer_details",customer_details)
print("supplier_details",supplier_details)
print("Gender_details",Gender)
frequency={}
for item in product_details:
    if item in frequency:
         frequency[item]=1
         frequency[item]+=1
    else:
       frequency[item]=1
print(frequency)
marklist=sorted(frequency.items(),key=lambda x:x[1],reverse=True)
sortdict=dict(marklist)
print(sortdict)
print("The most of the product for sales",list(sortdict.keys())[0],"Sold",list(sortdict.values())[0],"Items")
marklist=sorted(frequency.items(),key=lambda x:x[1],reverse=True)
sortdict=dict(marklist)
print(sortdict)
print("The most of the supplier for sales",list(sortdict.keys())[0],"Sold",list(sortdict.values())[0],"Items")
marklist=sorted(frequency.items(),key=lambda x:x[1],reverse=True)
sortdict=dict(marklist)
print(sortdict)
print("The most of the product buying customer",list(sortdict.keys())[0],"Sold",list(sortdict.values())[0],"Items")
from collections import Counter
counter=dict(Counter(Gender))
names=list(counter.keys())
print(names)
male=0
female=0
for name in names:
    if Gender[name]=="Male":
       male=male+1
    if Gender[name]=="Female":
       female=female+1
print("Total no of Female=",female)
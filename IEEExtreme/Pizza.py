toppings={"Anchovies":50,"Artichoke":60, "Bacon":92,"Broccoli":24,"Cheese":80,"Chicken":30,"Feta":99,"Garlic":8,"Ham":46,"Jalapeno":5,"Meatballs":120,"Mushrooms":11,"Olives":25,"Onions":11,"Pepperoni":80,"Peppers":6,"Pineapple":21,"Ricotta":108,"Sausage":115,"Spinach":18,"Tomatoes":14}
val=[]
prod=[]
topps=[]
calorias=0
x=raw_input().split()
for i in range(1,len(x),2):
    val.append(int(x[i]))
for j in range(2,len(x),2):
    prod.append(x[j])

for k in range(len(prod)):
    topps.append(prod[k].split(","))

vec=[]
for i in topps:
    a=0
    for j in i:
      a+=toppings.get(j)
    vec.append(a)

for i in range(len(vec)):
    calorias+= ((vec[i]+270)*val[i])

print "The total calorie intake is "+str(calorias)

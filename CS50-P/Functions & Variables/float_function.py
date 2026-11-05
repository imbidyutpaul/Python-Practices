x = float(input ("Enter X = "))
y = float(input ("Enter Y = "))
print ("Your anser was: ", x+y)

#another one
xx = float(input ("Enter XX = "))
yy = float(input ("Enter YY = "))

#input= 2.223344   output= 2.22
zz = round (xx+yy, 3)

#input= 223344   output= 223,344
print ("plus value was: " f"{zz :,}")

#or use this to one line
print ("Devided value was: ", round (xx/yy, 2))

#or use this to round number but tough
print ("Plus vale was: " f"{zz:.2f}")

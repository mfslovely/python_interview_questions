names = ['Joseph','Nathan','Sara','Sharan','Sara']
dict_1 = {}
for name in names:
        if name.startswith("S"):
                if name in dict_1:
                        dict_1[name] +=1
                else:
                        dict_1[name] = 1
print(dict_1)    
        

        
   
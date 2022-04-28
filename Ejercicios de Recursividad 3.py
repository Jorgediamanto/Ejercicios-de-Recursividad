
FICHAS = ["r","b","b","r","g","b","b","r","b","r","r","g","r","r","b","g","g"]
print("Fichas sin ordenar: "+str(FICHAS))
RED = []
BLUE = []
GREEN = []

for x in range(len(FICHAS)):
    if FICHAS[x]=="r":
        RED.append(x)

    if FICHAS[x]=="b":
        BLUE.append(x)

    if FICHAS[x]=="g":
        GREEN.append(x)


for x in range(len(FICHAS)):
    if x < len(RED):
        skrr = True
        for xx in range(len(RED)):
            if RED[xx]==x:
                skrr = False
        if skrr:
            for y in range(len(RED)):
                if RED[y]>(len(RED)-1):
                    
                    

                    for yy in range(len(GREEN)):
                        if GREEN[yy] == x:
                            GREEN[yy] = RED[y]
                            
                    
                    
                    for yyy in range(len(BLUE)):
                        if BLUE[yyy] == x:
                            BLUE[yyy] = RED[y]

                    RED[y]=x
                    break





    if x > len(RED)-1 and x < (len(RED)+len(GREEN)):
        skrra = True
        for xx in range(len(GREEN)):
            if GREEN[xx]==x:
                skrra = False
        if skrra:
            for y in range(len(GREEN)):
                if GREEN[y]>(len(GREEN)+len(RED)-1):
          
                    
                    
                    for yyy in range(len(BLUE)):
                        if BLUE[yyy] == x:
                            BLUE[yyy] = GREEN[y]

                    GREEN[y]=x
                    break




    




print("Fichas ordenadas: ")
print("Posiciones de las fichas rojas: "+str(RED))
print("Posiciones de las fichas verdes: "+str(GREEN))
print("Posiciones de las fichas azules: "+str(BLUE))


#print(RED)
#print(GREEN)
#print(BLUE)

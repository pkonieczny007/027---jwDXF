import os 
import fdxf

n=0

for filename in os.listdir():
    try:
        if filename.endswith('.dxf'):
            n+=1
            wys=fdxf.wys(filename)
            szer=fdxf.sze(filename)
            print(n, filename, wys, szer)
    except:
        print(n, filename, 'ERROR')
        


        

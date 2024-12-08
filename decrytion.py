##################################################################
###############Code written by PunV###############################
##################################################################
######Immitation of program is punishable offence#################
##################################################################
####################The decryptor#################################
##################################################################
tbprcs='encrypted_file.encpunv'
tbprcs=open(str(tbprcs),'r').read()
key=input('Enter the decryption key: ').strip()
row=ord(key[0])^86
col=ord(key[1])^67
dec=[]
we=0
op=0
cmplt=False
for p in range(0,row*col):
    dec.append('')
for r in range(col*row):
    op=r
    while not cmplt:
     try:
        dec[we]=tbprcs[op]
        op+=row
        we+=1
     except:
         cmplt=True
    cmplt=False
enod=''
for e in dec:
    enod+=e
d=open('decrypted_file.decpunv','w')
d.write(enod)
d.close()
print('file decrypted successfully!!')
print(enod)

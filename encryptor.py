##################################################################
###############Code written by PunV###############################
##################################################################
######Immitation of program is punishable offence#################
##################################################################
####################The encryptor#################################
##################################################################
import pyperclip
st=input('Entr the text to be encrypted: \r')

import random as ra
import time as tym
cols=ra. randint(4,10)
deceive=[]
for a in range(97,110):
	deceive.append(chr(ra.randint(33,99)))
# print(deceive)
cmplt=False
rows=0
while not cmplt:
	if rows*cols<len(st):
		while rows*cols<len(st):
			rows+=1
	cmplt=True
# print(rows,cols,len(st))
x=0
st=st+' '*(rows*cols-len(st))
# print(st.count(' '))
m=''
done=False
for e in range(cols):
	x=e
	done=False
	while not done:
		try:
			m+=st[x]
			x+=cols
		except:
			done=True





print('encrypted as: \n')
print(m)
print('*'*40)
dc=str(int(tym.time()))
print('The encryption key has been copied to your clipboard. \nShare it with only those with whom you want the message  to be shared\n')
keygen=chr(86^rows)+chr(67^cols)+deceive[ra.randint(0,12)]+dc[0:3]+deceive[ra.randint(0,12)]+dc[5:9]
print('decryption key: ',keygen)
pyperclip.copy(keygen)
k=open('encrypted_file.encpunv','w')
k.write(m)
k.close()

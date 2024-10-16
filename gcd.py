def gcd(a,b):
	while b!=0:
	    a,b=b,a%b
	return a

def modinv(e,phi):
	d,x1,x2,y1=0,0,1,1
	temp_phi=phi
	while e>0:
	    temp1,temp2=divmod(temp_phi,e)
	    temp_phi,e=e,temp2
	    x=x2-temp1*x1
	    y=d-temp1*y1
	    y2,x=x1,x 
	    d,y1=y1,y
	if temp_phi==1:
	    return d+phi 
	
def generate_keypair(p,q):
	n=p*q
	phi=(p-1)*(q-1)
	e=17
	g=gcd(e,phi)
	while g!=1:
	    e+=1
	    g=gcd(e,phi)
	d=modinv(e,phi)
	return((e,n),(d,n))
	
def encrypt(pk,plaintext):
	key,n=pk
	cipher=[pow(ord(char),key,n)for char in plaintext]
	return cipher
	
def decrypt(pk,ciphertext):
	key,n=pk
	plain=[chr(pow(char,key,n))for char in ciphertext]
	return "".join(plain)
	
if __name__=='__main__':
	p=int(input("enter a prime number(p):"))
	q=int(input("enter a anthor prime number(q):"))
	
	public,private=generate_keypair(p,q)
	print(f"public key:{public}");
	print(f"private key:{private}")
	
	message=input("enter the message to encrypt")
	
	encrypted_msg=encrypt(public,message)
	print(f"encrypted message:{encrypted_msg}")
	
	decrypted_msg=decrypt(private,encrypted_msg)
	print(f"decrypted message:{decrypted_msg}")

output:
sahyadri@sahyadri:~$ python gcd.py
enter a prime number(p):13
enter a anthor prime number(q):17
public key:(17, 221)
private key:(113, 221)
enter the message to encrypthello
encrypted message:[104, 186, 23, 23, 128]
decrypted message:hello

sahyadri@sahyadri:~$ python gcd.py
enter a prime number(p):11
enter a anthor prime number(q):13
public key:(17, 143)
private key:(113, 143)
enter the message to encryptwelcom
encrypted message:[136, 95, 114, 99, 89, 109]
decrypted message:welcom
sahyadri@sahyadri:~$ 


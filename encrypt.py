
import pyAesCrypt
import sys
import getpass

bufferSize = 64 * 1024

def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

if __name__ == "__main__":
	
	while True:
		passwd = getpass.getpass("Enter Password:")
		if not password_check(passwd):
			print("Invalid Password")
			continue
		else:
			break

	pyAesCrypt.encryptFile("pwd.txt", "sample.txt.aes", passwd, bufferSize)
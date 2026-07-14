import re

def check_password_strength(password):
    score=0
    suggestions=[]

    if len(password)>=8:
        score+=1
    else:
        suggestions.append("Use at least 8 character")
    
    if re.search(r'[A-Z]',password):
        score+=1
    else:
        suggestions.append("Use atleast 1 capital character")

    if re.search(r'[a-z]',password):
        score+=1
    else:
        suggestions.append("Use atleast 1 small character")
    
    if re.search(r'[\d]',password):
        score+=1
    else:
        suggestions.append("Use atleast 1 digit")
    
    if re.search(r"[!@#$%^&*():<>:;'./]",password):
        score+=1
    else:
        suggestions.append("Use atleast 1 special character")
    
    if(score==1):
        strength = "VERY WEAK PASSWORD"
    if(score==2):
        strength="WEAK PASSWORD"
    if(score==3):
        strength= "MEDIUM PASSWORD"
    if(score>=4):
        strength="STRONG PASSWORD"

    return suggestions, strength

password=input("Enter your password: ")
strength,suggestions=check_password_strength(password)
print(strength,suggestions)
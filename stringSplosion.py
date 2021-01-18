# William Ikenna-Nwosu (wiknwo)
# stringSplosion
# Given a non-empty string like "Code" return a string 
# like "CCoCodCode".
# stringSplosion("Code") → "CCoCodCode"
# stringSplosion("abc") → "aababc"
# stringSplosion("ab") → "aab"
def stringSplosion(stringinput):
    if stringinput == "":
        return stringinput
    
    else:
        return stringSplosion(stringinput[:-1]) + stringinput

def main():
    userinput = input("Please enter string: ")
    print(stringSplosion(userinput))

if __name__ == "__main__":
    main()
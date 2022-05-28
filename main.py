#Ceasar cipher encoder/decoder
def CeasarCode(code: str, encode: bool, num) -> str:
    #reads words.txt
    from pathlib import Path
    p = Path(__file__).with_name('words.txt')
    with p.open('r') as w:
        wo=w.read()
    words=wo.split('\n')#   this returns a **list** containing the 1000 most common English words, plus some words that I added
    
    #converts input into list of strs
    code=code.lower()
    for letter in code:
        if letter not in 'abcdefghijklmnopqrstuvwxyz':
            code.replace(letter,'')
    codelist=code.split()
    
    #decoding
    if not encode:
        #auto decode
        attempt=0
        prev=[]
        for i in range(26):
            test=CeasarCode(code, True, i+1)
            for word in words:
                if word in test and test not in prev:
                    attempt += 1
                    print('Attempt '+str(attempt)+': '+test)
                    DidItWork=input('Is it decoded? [(Y)es/(N)o]\n>')
                    while DidItWork.lower()[0] not in 'yn':
                        DidItWork=input('Input invalid. Is it decoded? [(Y)es/(N)o]\n>')
                    if DidItWork.lower()[0] == 'y':
                        return ('Decoding successful after '+str(attempt)+' attempts. Plaintext: '+ CeasarCode(code, True, i+1))
                    elif DidItWork.lower()[0] == 'n':
                        prev.append(test)
                        continue
                else:
                    continue
        continueManual=input('AI decoding failed. Continue with manual decoding?[(Y)es/(N)o]\n>')
        while continueManual.lower()[0] not in 'yn':
            continueManual=input('Input invalid. Continue with manual decoding?[(Y)es/(N)o]\n>')
        if continueManual == 'n':
            return 'Decoding failed: Manual decoding denied'
        try:
            del(DidItWork)
        except:
            DidItWork=''
            #manual decode
        for k in range(26):
            print('Attempt ' + str(k+1) + ': ' + CeasarCode(code, True, k+1))
            DidItWork=input('Is it decoded? [(Y)es/(N)o]\n>')
            while DidItWork.lower()[0] not in 'yn':
                DidItWork=input('Input invalid. Is it decoded? [(Y)es/(N)o]\n>')
            if DidItWork.lower()[0] == 'y':
                return ('Decoding successful after '+str(k+1)+' attempts. Plaintext: '+ CeasarCode(code, True, k+1))
            elif DidItWork.lower()[0] == 'n':
                print('Continuing manual decoding.')
        return 'Decoding failed: Automatic and manual decoding failed.'

    #encoding
    elif encode:
        if num == None:
            num = input('Input amount of steps to shift:\n>')
            while type(num) is not int:
                try:
                    num=int(num)
                    while num > 25:
                        num = input('Unable to shift more than 25 steps. Try again:\n>')
                except:
                    num = input('Input invalid. Input amount of steps to shift:\n>')
        tempcode=''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        codeletters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        for i in range(len(code)):
            if code[i] == ' ':
                tempcode+=' '
                continue
            if letters.find(code[i]) == -1:
                tempcode+=' '
                continue
            tempcode+=codeletters[letters.find(code[i])+num]
        return tempcode

#main loop
print('Welcome to CeasarEncode!')
while True:
    e=input('(E)ncode or (D)ecode?\n>')
    if e.lower()[0] == 'e':
        encode = True
    elif e.lower()[0] == 'd':
        encode = False
    else:
        while e.lower()[0] != 'e' or 'd':
            e=input('Input invalid. Encode or Decode? (type E for encode or D for decode, then press enter)\n>')
            if e.lower()[0] == 'e':
                encode = True
                break
            elif e.lower()[0] == 'd':
                encode = False
                break
    code=input('Input code:\n>')
    print(CeasarCode(code, encode, None))

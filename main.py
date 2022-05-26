#Ceasar cipher encoder/decoder
def CeasarCode(code: str, encode: bool) -> str:
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
    if not encode:
        print()    
    elif encode:
        num = input('Input how many steps to shuffle:\n>')
        while type(num) is not int:
            try:
                num=int(num)
            except:
                num = input('Input invalid. Try again:\n>')
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
    print('Operation successful. Output: '+CeasarCode(code,encode))


    

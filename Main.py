from playsound import playsound
from antapi import encrypt
  

def main():

    def dot():
        playsound('Dot.wav')

    def dash():
        playsound('Dash.wav')

    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'," ":" ","!":"-.-.--",
                        '"':".-..-.","#":"#","$":"$","%":"%","^":"^","&":".-...",
                        "*":"*","=":"=","+":".-.-.","\ ":"\ ","/":"-..-.","<":"<",
                        ">":">","~":"~",'\x7f':"\x7f","'":".----.","`":"`","|":"|"
                        ,"//":"//","}":"}","{":"{","[":"]","\\":"\\"
                        }


    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())

    def plaintexenmor():

        text = input("A Text: ");
        text = encrypt(text)
        for i in text:
            u = (MORSE_CODE_DICT[i.upper()])
            print(u,end="")
            for k in u:
                    if(k=="-"):
                        dash()
                    else:
                        dot()
    
    



    def morseFile(name):
       
       f = open(name,"w")
       text = input("A Text: ");
       text = encrypt(text)
       oo = ""
       for i in text:
            u = (MORSE_CODE_DICT[i.upper()])
            oo = oo+u
       f.write(oo)
       f.close()



    n = int(input("1.Encode\n2.Morse File\nChoose: "))
    if(n==1):
        plaintexenmor()
    elif(n==2):
        name = input("Enter File name: ")
        morseFile(name)
    else:
        print("Wrong option")

if __name__ == '__main__':
    main()


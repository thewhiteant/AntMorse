from playsound import playsound
  
# for playing note.mp3 file
def dot():
    playsound('Dot.wav')

def dash():
     playsound('Dash.wav')

MORSE_CODE_DICT = { 'A':'._', 'B':'_...',
                    'C':'_._.', 'D':'_..', 'E':'.',
                    'F':'.._.', 'G':'__.', 'H':'....',
                    'I':'..', 'J':'.___', 'K':'_._',
                    'L':'._..', 'M':'__', 'N':'_.',
                    'O':'___', 'P':'.__.', 'Q':'__._',
                    'R':'._.', 'S':'...', 'T':'_',
                    'U':'.._', 'V':'..._', 'W':'.__',
                    'X':'_.._', 'Y':'_.__', 'Z':'__..',
                    '1':'.____', '2':'..___', '3':'...__',
                    '4':'...._', '5':'.....', '6':'_....',
                    '7':'__...', '8':'___..', '9':'____.',
                    '0':'_____', ', ':'__..__', '.':'._._._',
                    '?':'..__..', '/':'_.._.', '_':'_...._',
                    '(':'_.__.', ')':'_.__._'," ":" "}

text = input("A Text: ");

for i in text:
    print(MORSE_CODE_DICT[i.upper()],end="")
    for k in MORSE_CODE_DICT[i.upper()]:
        if(k=="_"):
            dash()
        else:
            dot()

#TODO: File Manage and Engcrition

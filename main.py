
def Binary_Search ():
    values= (1,12,15,17,190,196,200)
T= 17
MIN = 0
HIGH = len(values)
FOUND = False
ANSWER = 0
MID =0

while (FOUND == False) and (MIN <= HIGH):
    MID = ((MIN + HIGH)//2)
    if values [MID] == T:
        FOUND = True
        ANSWER = MID
    elif T > VALUES [MID]:
        MIN = MID +1
else:
        HIGH = MID - 1
        print(FOUND,MID)
        if FOUND == True:
            print(T,"FOund as string", ANSWER)
        else:
            print(T,"was not found")
            Binary_Search()






# my_str = 'سعيد'
# my_str = my_str[:2] + 'ي' + my_str[3:]
# print(my_str)
import pyperclip as pc
matn = "1"
while matn!="0":
    matn=pc.paste()
    if matn=="0":
        break
    kol_martabe=len(matn)
    for i in range (kol_martabe):
        if matn[i]=="ی":
            matn = matn[:i] + 'ي' + matn[i+1:] 
    # print(matn)
    pc.copy(matn)
    # print("copy shod!")

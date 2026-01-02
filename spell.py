from tkinter import*
from textblob import TextBlob
main=Tk()
main.title("Spelling Checker")
main.geometry("700x400")
spell_text=StringVar()
def check_spelling():
    word=text_field.get()
    check=TextBlob(word)
    correct_word=str(check.correct())
    spell_text.set("Correct Word:"+correct_word)
    
#Title Label
title_label=Label(main,text="Spelling Checker",font=("poppins",30,"bold"))
title_label.pack(pady=50)
#Text Field
text_field=Entry(main,font=("poppins",25))
text_field.pack()
#Check Button
check_button=Button(main,text="Check",font=("poppins",20),command=check_spelling)
check_button.pack(pady=20)
#Spell Label
spell_label=Label(main,font=("poppins",20),textvariable=spell_text)
spell_label.pack()
main.mainloop()

def creatwidthes():
    ########################################################################################### Labels
    TrackLabel = Label(root,text ='Select Audio Track : ',background='purple',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)
################################################################################################Entry Box
    TrackLabelEntry =Entry(root,font=('arial',16,'italic bold'),width=35)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
###############################################################################################Buttons
    BrowseButton =Button(root,text='Search',background='deep pink',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4')
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root, text='Play', background='green2', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4')
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    PauseButton = Button(root, text='Pause', background='yellow', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4')
    PauseButton.grid(row=1, column=1, padx=20, pady=20)

    VolumnupButton = Button(root, text='VolumnUp', background='blue', font=('arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4')
    VolumnupButton.grid(row=1, column=2, padx=20, pady=20)

    StopButton = Button(root, text='Stop', background='red', font=('arial', 13, 'italic bold'), width=20, bd=5,                        activebackground='purple4')
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumnDownButton = Button(root, text='VolumnDown', background='blue', font=('arial', 13, 'italic bold'), width=20, bd=5,                     activebackground='purple4')
    VolumnDownButton.grid(row=2, column=2, padx=20, pady=20)






###############################################################################################
from tkinter import *
root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Sound Player')
root.iconbitmap('')
root.resizable(False,False)
root.configure(bg='purple')
###############################################################################################  Create slider
aa ='DEVELOPED BY SYEDA ARBISH'
count = 0
text=''
SliderLabel =Label(root,text=aa, bg ='purple',font=('arial', 38, 'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
    global  count,text
    if(count>=len(aa)):
        count= -1
        text=''
        SliderLabel.configure(text=text)
    else:
        text=text+aa[count]
        SliderLabel.configure(text=text)

    count += 1
    SliderLabel.after(200,IntroLabelTrick())


IntroLabelTrick()
creatwidthes()
root.mainloop()
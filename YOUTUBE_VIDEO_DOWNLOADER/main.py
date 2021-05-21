from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mbox
from  pytube import YouTube
from playsound import *
foldername=""

#function for file loaction
def location():
    global foldername
    foldername=filedialog.askdirectory()
    if len(foldername)>1:
        patherror.config(text=foldername,fg="green")
    else:
        patherror.config(text="Please choose a folder !!",fg="red")
#function for download video
def downloadvideo():
    c=ytdchoice.get()
    link=ytdentry.get()
    fn=foldername
    if len(link)==0 and fn=="":
        mbox.showerror("!! ERROR !!","Please enetr both link as well as location")
    elif len(link)==0:
        mbox.showerror("!! ERROR !!","Please enetr the link ")
    elif fn=="":
        mbox.showerror("!! ERROR !!","Please enetr the location")
    elif len(link)>1:
        ytderror.config(text="")
        yt=YouTube(link)
        if c==choice[0]:
            vid=yt.streams.filter(resolution="240p").first().download(foldername)
            ytderror.config(text="!!! DOWNLOAD COMPLETED !!!", fg="green", font=("jost", 15, "bold italic"))
            playsound("download.mpeg")
        elif c==choice[1]:
            vid=yt.streams.filter(resolution="360p").first().download(foldername)
            ytderror.config(text="!!! DOWNLOAD COMPLETED !!!", fg="green", font=("jost", 15, "bold italic"))
            playsound("download.mpeg")
        elif c==choice[2]:
            vid=yt.streams.filter(resolution="720p").first().download(foldername)
            ytderror.config(text="!!! DOWNLOAD COMPLETED !!!", fg="green", font=("jost", 15, "bold italic"))
            playsound("download.mpeg")
        elif c==choice[3]:
            vid=yt.streams.first().download(foldername)
            ytderror.config(text="!!! DOWNLOAD COMPLETED !!!", fg="green", font=("jost", 15, "bold italic"))
            playsound("download.mpeg")
        elif c==choice[4]:
            vid=yt.streams.filter(type="audio").last().download()
        else:
            ytderror.config(text="Paste Link Again!!",fg="red")

def information():
    url=ytdentry.get()
    yt=YouTube(url)
    h=str(yt.title)
    t=int(yt.length)
    hour=str(t//3600)
    min=str((t%3600)//60)
    sec=str((t%3600)%60)
    dur=hour+"hour"+":"+min+"minutes"+":"+sec+"seconds"
    v=yt.views
    titlelabel.config(text=f"TITLE :- {h}", fg="cyan", bg="purple", font=("jost",9, "bold"))
    timelabel.config(text=f"LENGTH:- {dur}", fg="cyan", bg="purple", font=("jost",12, "bold"))
    viewlabel.config(text=f"VIEWS :- {v}", fg="cyan", bg="purple", font=("jost",12, "bold"))


root=Tk() # creating tkinter object to access all its method
root.title(" YOUTUBE DOWNLOADER created by y@sh")
root.geometry("550x600") # set  our GUI window size
root.columnconfigure(0,weight=1) # set all our content in the centre
root.configure(bg="purple")

ytdlabel=Label(root,text=" PLEASE ENTER LINK (URL) OF THE VIDEO HERE",bg="yellow",font=("jost",12,"bold"))
ytdlabel.grid(row=1,column=0,padx=0,pady=5) # assign this level to our grid

ytdentryvar=StringVar()
ytdentry=Entry(root,width=75,textvariable=ytdentryvar) # box for entry link
ytdentry.grid()

#error message
ytderror= Label(root,text="ERROR URL" ,fg="red",bg="purple",font=("jost",12,"bold"))
ytderror.grid()

blank1=Label(root,text="",width=70,bg="purple",font=("jost",12,"bold"))
blank1.grid() # to just create space between different lable

# saving of the youtube video
savelable=Label(root, text=" GET READY TO DOWNLOAD VIDEO ",bg="yellow",font=("jost",18,"bold"))
savelable.grid()

blank2=Label(root,width=50,bg="purple",font=("jost",12,"bold"))
blank2.grid()

saveentry=Button(root,width=12,bg="red",fg="black",text="Select Location",font=("jost",10,"bold"),command=location)
saveentry.grid()

#location error
patherror=Label(root,text="ERROR OF FILE LOCATION",fg="red",bg="purple",font=("jost",10,"bold"))
patherror.grid()

blank3=Label(root,width=20,bg="purple",font=("jost",12,"bold"))
blank3.grid()

ytdquality=Label(root,text="SELECT QUALITY",fg="black",bg="yellow",font=("jost",10,"bold"))
ytdquality.grid()

choice=["240","360","720","1080","audio mp3"]
ytdchoice=ttk.Combobox(root,values=choice)
ytdchoice.grid()

blank3=Label(root,width=20,bg="purple",font=("jost",12,"bold"))
blank3.grid()

#information button
infobtn=Button(root,width=13,bg="red",fg="white",text="Information",font=("jost",13,"bold"),command=information)
infobtn.grid()
blank6=Label(root,width=20,bg="purple")
blank6.grid()

titlelabel=Label(root,width=70,bg="purple",font=("jost",12,"bold"))
titlelabel.grid()

timelabel=Label(root,width=40,bg="purple",font=("jost",12,"bold"))
timelabel.grid()

viewlabel=Label(root,width=40,bg="purple",font=("jost",12,"bold"))
viewlabel.grid()

blank6=Label(root,width=20,bg="purple")
blank6.grid()

#download button
downloadbtn=Button(root,text="Download",width=15,bg="red",fg="black",font=("jost",12,"bold"),command=downloadvideo)
downloadbtn.grid()

end=Label(root,text=" A Yash's Creation ",bg="cyan",fg="black",width=30,font=("jost",20,"bold italic"))
end.grid()
playsound("welcome.mpeg")

root.mainloop()
playsound("thankyou.mpeg")

from tkinter import *
from tkinter import IntVar
from tkinter import ttk
from random import *
from tkinter import filedialog
import tkinter.filedialog
txt = ["Text file", "*.txt"]

# just names from the albums, don't touch this :chofe:
lSmfthb = ["The", "Haunted", "Ballroom", "By", "The", "Seaside", "One", "Thousand", "Memories", "Haunting", "Me", "A", "Summer", "Romance", "Den", "of", "Iniquity", "Dream", "Waltz", "a", "Handful", "of", "Stars", "Request", "Dance", "In", "The", "Dark", "Reckless", "Night", "Thronged", "With", "Ghosts", "From", "Out", "of", "Nowhere", "Friends", "Past", "Reunited", "You", "And", "The", "Night", "Moonlight", "Serenade", "Disillusioned", "The", "Revolving", "Bandstand", "Garden", "of", "Weeds", "Excuse", "Me", "For", "Ladies", "In", "Days", "of", "Old", "September", "1939", "Thanks", "Midnight", "The", "Stars", "And", "You", "Thanks"]
lAstts = ["We", "Cannot", "Escape", "The", "Past", "Cloudy", "Since", "You", "Went", "Away", "Emptiness", "Consigned", "To", "a", "Yesterday", "Masquerade", "Ball", "Malign", "Forces", "of", "Occult", "On", "Edge", "of", "Breakdown", "Robins", "And", "Roses", "Date", "With", "An", "Angel", "It's", "All", "Forgotten", "Now", "Each", "Today", "Doesn't", "Lead", "To", "a", "Tomorrow", "Home", "Friends", "Past", "Re-united", "a", "Stairway", "To", "The", "Stars"]
lWagroar = ["I", "Saw", "Your", "Face", "in", "a", "Dream", "We'll", "All", "Go", "Riding", "On", "a", "Rainbow", "That", "Old", "Feeling", "The", "Weeping", "Dancefloor", "Driven", "Beyond", "The", "Limits", "The", "Memory", "Of", "a", "Song", "And", "The", "Bands", "Played", "On", "Here", "I", "Am", "Broken", "Hearted", "Hoping", "For", "Some", "Kind", "of", "Recognition", "Under", "a", "Warm", "Golden", "Light", "Unmasking", "At", "Midnight", "Roll", "Up", "the", "Carpet", "And", "Dance", "Contemplation", "Faith", "In", "Time", "We", "Have", "Been", "Here", "Before", "Stardust"]
lDsfd = ["Deleted", "Scenes", "Forgotten", "Dreams"]
lProp = ["Lacunar", "Amnesia", "Persisten", "Repetition", "of", "Phrases", "Rosy", "Retrospection", "Long", "Term", "Remote", "Poor", "Ennunciation", "Past", "Life", "Regression", "False", "Memory", "Syndrome", "Von", "Restorff", "Effect", "Unmasking", "Alzheimer's"]
lAebbtw = ["All", "You", "Are", "Going", "To", "Want", "To", "Do", "Is", "Get", "Back", "There", "Moments", "Of", "Sufficient", "Lucidity", "The", "Great", "Hidden", "Sea", "of", "The", "Unconscious", "Libet's", "Delay", "I", "Feel", "As", "If", "I", "Might", "Be", "Vanishing", "An", "Empty", "Bliss", "Beyond", "This", "World", "Bedded", "Deep", "in", "Long", "Term", "Memory", "A", "Relationship", "With", "The", "Sublime", "Mental", "Caverns", "Without", "Sunshine", "Pared", "Back", "To", "The", "Minimal", "Tiny", "Gradiations", "of", "Loss", "Camaraderie", "at", "Arms", "Length", "The", "Sublime", "is", "Disapointingly", "Elusive"]
lPas = ["Everything", "is", "On", "The", "Point", "of", "Decline", "As", "if" "One", "Were", "Sinking", "Into", "Sand", "Approaching", "The", "Outer", "Limits", "of", "Our", "Solar", "System", "When", "the", "Dog", "Days", "Were", "Drawing", "to", "An", "End", "A", "Last", "Glimpse", "of", "the", "Land", "Being", "Lost", "Forever", "The", "Homesickness", "That", "Was", "Corroding", "Her", "Soul", "I", "Have", "Become", "Almost", "Invisible", "to", "Some", "Extent", "Like", "a", "Dead", "Man", "In", "the", "Deep", "and", "Dark", "Hours", "of", "the", "Night", "No", "One", "Knows", "What", "Shadowy", "Memories", "Haunt", "Them", "to", "This", "Day", "Increasingly", "Absorbed", "In", "His", "Own", "World", "Isolated", "Lights", "on", "the", "Abyss", "of", "Ignorance", "Now", "The", "Night", "is", "Over", "and", "Dawn", "is", "About", "to", "Break"]
lEPas = ["Everything", "Is", "On", "The", "Point", "of", "Decline", "Again", "So", "Run", "Down", "Isolated", "Lights", "Again", "Of", "Grace", "and", "Providence", "A", "Golden", "Pheasant", "on", "a", "Black", "Ground", "The", "Quilter", "Standard", "After", "The", "Earth", "Has", "Ground", "Itself", "Down", "But", "The", "Stars", "Had", "Come", "Out", "Sebald"]
lEateotS1 = ["It's", "Just", "a", "Burning", "Memory", "We", "Don't", "Have", "Many", "Days", "Late", "Afternoon", "Drifting", "Childishly", "Fresh", "Eyes", "Slightly", "Bewildered", "Things", "That", "Are", "Beautiful", "And", "Transient", "All", "That", "Follows", "is", "True", "An", "Autumnal", "Equinox", "Quiet", "Internal", "Rebellions", "The", "Loves", "of", "My", "Entire", "Liefe", "Into", "Each", "Others", "Eyes", "My", "Heart", "Will", "Stop", "In", "Joy"]
lEateotS2 = ["A", "Losing", "Battle", "is", "Raging", "Misplaced", "in", "Time", "What", "Does", "it", "Matter", "How", "My", "Heart", "Breaks", "Glimpses", "of", "Hope", "in", "Trying", "Times", "Surrendering", "to", "Despair", "I", "Still", "Feel", "as", "Though", "I", "Am", "Me", "Quiet", "Dusk", "Coming", "Early", "Last", "Moments", "of", "Pure", "Recall", "Denial", "Unravelling", "The", "Way", "Ahead", "Feels", "Lonely"]
lEateotS3 = ["Back", "There", "Benjamin", "And", "Heart", "Breaks", "Hidden", "Sea", "Buried", "Deep", "Libet's", "All", "Joyful", "Camaraderie", "To", "the", "Minimal", "Great", "Hidden", "Sublime", "Beyond", "Loss", "Bewildered", "In", "Other", "Eyes", "Long", "Term", "Dusk", "Glimpses", "Gradiations", "of", "Arms", "Length", "Drifting", "Time", "Misplaced", "Internal", "Bewildered", "World", "Burning", "Despair", "Does", "Ache", "Aching", "Cavern", "Without", "Lucidity", "An", "Empty", "Bliss", "Beyond", "This", "World", "Libet", "Delay", "Mournful", "Cameraderie"]
lEateotS4 = ["Post", "Awareness", "Confusions", "Temporary", "Bliss", "State"]
lEateotS5 = ["Advanced", "Plaque", "Entanglements", "Synapse", "Retrogenesis", "Sudden", "Time", "Regression", "Into", "Isolation"]
lEateotS6 = ["A", "Confusion", "So", "Thick", "You", "Forget", "Forgetting", "A", "Brutal", "Bliss", "Beyond", "Beyond", "This", "Empty", "Defeat", "Long", "Decline", "is", "Over", "Place", "in", "The", "World", "Fades", "Away"]
lEaeb = ["Loss", "of", "Want", "Back", "There", "I", "Might", "Be", "Vanishing", "Empty", "Beyond", "Beyond", "Beyond", "Losing", "Battle", "of", "Loss", "Advanced", "Plaque", "Camaraderie", "All", "Eyes", "Bewildered", "Glimpses", "of", "Life", "Denial", "Equinox", "Eyes", "Will", "Stop", "Losing", "Loss", "of", "Battle", "Plaque", "Advanced", "Despair", "Benjamin", "Beyond", "Bliss", "Drifting", "Sublime", "Hope", "Minimal", "All", "You", "Are", "Internal", "Unravel", "Dusk", "Memory", "Fraction", "Entanglement", "Synapse", "Ache", "And", "Bliss", "Everyhwere", "Bliss"]
lEaebM = ["An", "Empty", "Everywhere" "I", "Might", "Be", "Vanishing", "Losing", "Battle", "of", "Loss", "Advanced", "Plaque", "Camaraderie", "All", "Eyes", "Bewildered", "Glimpses", "of", "Life", "Denial", "Losing", "Loss", "of", "Battle", "Plaque", "Advanced", "Despair", "Benjamin", "Beyond", "Bliss", "Drifting", "Sublime", "Hope", "Internal", "Unravel", "Dusk", "Memory", "Fraction", "My", "Heart", "Is", "True", "Lonely", "Way", "Ahead", "Hidden", "Minimal", "Sea", "Elusive", "Sunshine"]
lTciadot = ["Take", "Care", "It's", "A", "Desert", "Out", "There"]

def inFile():
    folderPathIn = tkinter.filedialog.askopenfile(mode='r')
    # write from selected file
    ctn = folderPathIn.read()
    pullFrom.delete(0, END)
    pullFrom.insert(0, ctn)
def outFile():
    folderPathOut = tkinter.filedialog.asksaveasfile(filetypes=(("Text Files", "*.txt"),))
    # jfc I spent like 20 minutes on google trying to figure this out. I just needed to add ".name" in there wtf
    # write to selected file
    fileDir = open(folderPathOut.name, "w", encoding="utf-8")
    fileDir.write(outputS.get())
def setAll0():
    # literally just adding 0 to all the entries
    smfthb.delete(0,END)
    smfthb.insert(0,"0")

    astts.delete(0,END)
    astts.insert(0,"0")

    wagroar.delete(0,END)
    wagroar.insert(0,"0")

    dsfd.delete(0,END)
    dsfd.insert(0,"0")

    prop.delete(0,END)
    prop.insert(0,"0")

    aebbtw.delete(0,END)
    aebbtw.insert(0,"0")

    pas.delete(0,END)
    pas.insert(0,"0")

    epas.delete(0,END)
    epas.insert(0,"0")

    s1.delete(0,END)
    s1.insert(0,"0")

    s2.delete(0,END)
    s2.insert(0,"0")

    s3.delete(0,END)
    s3.insert(0,"0")

    s4.delete(0,END)
    s4.insert(0,"0")

    s5.delete(0,END)
    s5.insert(0,"0")

    s6.delete(0,END)
    s6.insert(0,"0")

    eaeb.delete(0,END)
    eaeb.insert(0,"0")

    eaebm.delete(0,END)
    eaebm.insert(0,"0")

    tciadot.delete(0,END)
    tciadot.insert(0,"0")

    aText.delete(0,END)
    aText.insert(0,"0")

def setAll100():
    #ditto last except with 100

    smfthb.delete(0,END)
    smfthb.insert(0,"100")

    astts.delete(0,END)
    astts.insert(0,"100")

    wagroar.delete(0,END)
    wagroar.insert(0,"100")

    dsfd.delete(0,END)
    dsfd.insert(0,"100")

    prop.delete(0,END)
    prop.insert(0,"100")

    aebbtw.delete(0,END)
    aebbtw.insert(0,"100")

    pas.delete(0,END)
    pas.insert(0,"100")

    epas.delete(0,END)
    epas.insert(0,"100")

    s1.delete(0,END)
    s1.insert(0,"100")

    s2.delete(0,END)
    s2.insert(0,"100")

    s3.delete(0,END)
    s3.insert(0,"100")

    s4.delete(0,END)
    s4.insert(0,"100")

    s5.delete(0,END)
    s5.insert(0,"100")

    s6.delete(0,END)
    s6.insert(0,"100")

    eaeb.delete(0,END)
    eaeb.insert(0,"100")

    eaebm.delete(0,END)
    eaebm.insert(0,"100")

    tciadot.delete(0,END)
    tciadot.insert(0,"100")

    aText.delete(0,END)
    aText.insert(0,"100")

def scramble():
    b=0
    # iteration var, too lazy to change, soz

    # clear out list from previous session and prepare text in "Additional Text" for scrambling process
    listS.clear()
    strUns = pullFrom.get()
    listUns = strUns.split()

    namesToGen = int(selectGens.get())
    for i in range(len(lSmfthb)-1):
        a=randint(0,100)
        # var for % chance
        if int(smfthb.get()) > a:
            listUns.append(lSmfthb[b])
            # append song titles from smfthb, ditto for each next loop
            b=b+1
    b=0
    for i in range(len(lAstts)-1):
        a=randint(0,100)
        if int(astts.get()) > a:
            listUns.append(lAstts[b])
            b=b+1
    b=0
    for i in range(len(lWagroar)-1):
        a=randint(0,100)
        if int(wagroar.get()) > a:
            listUns.append(lWagroar[b])
            b=b+1
    b=0
    for i in range(len(lDsfd)-1):
        a=randint(0,100)
        if int(dsfd.get()) > a:
            listUns.append(lDsfd[b])
            b=b+1
    b=0
    for i in range(len(lProp)-1):
        a=randint(0,100)
        if int(prop.get()) > a:
            listUns.append(lProp[b])
            b=b+1
    b=0
    for i in range(len(lAebbtw)-1):
        a=randint(0,100)
        if int(aebbtw.get()) > a:
            listUns.append(lAebbtw[b])
            b=b+1
    b=0
    for i in range(len(lPas)-1):
        a=randint(0,100)
        if int(pas.get()) > a:
            listUns.append(lPas[b])
            b=b+1
    b=0
    for i in range(len(lEPas)-1):
        a=randint(0,100)
        if int(epas.get()) > a:
            listUns.append(lEPas[b])
            b=b+1
    b=0
    for i in range(len(lEateotS1)-1):
        a=randint(0,100)
    if int(s1.get()) > a:
        listUns.append(lEateotS1[b])
        b=b+1
    b=0
    for i in range(len(lEateotS2)-1):
        a=randint(0,100)
    if int(s2.get()) > a:
        listUns.append(lEateotS2[b])
        b=b+1
    b=0
    for i in range(len(lEateotS3)-1):
        a=randint(0,100)
    if int(s3.get()) > a:
        listUns.append(lEateotS3[b])
        b=b+1
    b=0
    for i in range(len(lEateotS4)-1):
        a=randint(0,100)
    if int(s4.get()) > a:
        listUns.append(lEateotS4[b])
        b=b+1
    b=0
    for i in range(len(lEateotS5)-1):
        a=randint(0,100)
    if int(s5.get()) > a:
        listUns.append(lEateotS5[b])
        b=b+1
    b=0
    for i in range(len(lEateotS6)-1):
        a=randint(0,100)
    if int(s6.get()) > a:
        listUns.append(lEateotS6[b])
        b=b+1
    b=0
    for i in range(len(lEaeb)-1):
        a=randint(0,100)
    if int(eaeb.get()) > a:
        listUns.append(lEaeb[b])
        b=b+1
    b=0
    for i in range(len(lEaebM)-1):
        a=randint(0,100)
    if int(eaebm.get()) > a:
        listUns.append(lEaebM[b])
        b=b+1
    b=0
    for i in range(len(lTciadot)-1):
        a=randint(0,100)
    if int(tciadot.get()) > a:
        listUns.append(lTciadot[b])
        b=b+1
    b=0
    for i in range(namesToGen):
        length = randint(1,int(selectLength.get()))
        for j in range(length):
            a = randint(0,len(listUns)-1)
            listS.append(listUns[a])
        listS.append("\n")
    # clear old output and add new
    outputS.delete(0,END)
    outputS.insert(0,listS)
# I HATE TKINTER I HATE TKINTER I HATE TKINTER
# yeah no I ain't commenting this sorry

root = Tk()
listS = []
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Additional keywords").grid(column=0, row=0)
pullFrom = ttk.Entry(frm, width=30)
pullFrom.grid(column=0, row=1)
ttk.Label(frm, text="Amount of names to generate").grid(column=0, row=3)
selectGens = ttk.Entry(frm,width=20)
selectGens.grid(column=0,row=4)
ttk.Button(frm, text="Scramble", command=scramble).grid(column=0, row=2)
ttk.Label(frm, text="Maximum name length").grid(column=0, row=5)
selectLength = ttk.Entry(frm,width=20)
selectLength.grid(column=0,row=6)
ttk.Label(frm, text="Output").grid(column=0, row=7)
outputS = ttk.Entry(frm, width=30)
outputS.grid(column=0,row=8)
ttk.Label(frm, text="% Chance of SMFTHB names").grid(column=1, row=0)
smfthb = ttk.Entry(frm, width=10)
smfthb.grid(column=2,row=0)
ttk.Label(frm, text="% Chance of ASTTS names").grid(column=1, row=1)
astts = ttk.Entry(frm, width=10)
astts.grid(column=2,row=1)
ttk.Label(frm, text="% Chance of WAGROAR names").grid(column=1, row=2)
wagroar = ttk.Entry(frm, width=10)
wagroar.grid(column=2,row=2)
ttk.Label(frm, text="% Chance of DS/FD names").grid(column=1, row=3)
dsfd = ttk.Entry(frm, width=10)
dsfd.grid(column=2,row=3)
ttk.Label(frm, text="% Chance of PROP names").grid(column=1, row=4)
prop = ttk.Entry(frm, width=10)
prop.grid(column=2,row=4)
ttk.Label(frm, text="% Chance of AEBBTW names").grid(column=1, row=5)
aebbtw = ttk.Entry(frm, width=10)
aebbtw.grid(column=2,row=5)
ttk.Label(frm, text="% Chance of P(AS) names").grid(column=1, row=6)
pas = ttk.Entry(frm, width=10)
pas.grid(column=2,row=6)
ttk.Label(frm, text="% Chance of EP(AS) names").grid(column=1, row=7)
epas = ttk.Entry(frm, width=10)
epas.grid(column=2,row=7)
ttk.Label(frm, text="% Chance of EATEOTS1 names").grid(column=1, row=8)
s1 = ttk.Entry(frm, width=10)
s1.grid(column=2,row=8)
ttk.Label(frm, text="% Chance of EATEOTS2 names").grid(column=3, row=0)
s2 = ttk.Entry(frm, width=10)
s2.grid(column=4,row=0)
ttk.Label(frm, text="% Chance of EATEOTS3 names").grid(column=3, row=1)
s3 = ttk.Entry(frm, width=10)
s3.grid(column=4,row=1)
ttk.Label(frm, text="% Chance of EATEOTS4 names").grid(column=3, row=2)
s4 = ttk.Entry(frm, width=10)
s4.grid(column=4,row=2)
ttk.Label(frm, text="% Chance of EATEOTS5 names").grid(column=3, row=3)
s5 = ttk.Entry(frm, width=10)
s5.grid(column=4,row=3)
ttk.Label(frm, text="% Chance of EATEOTS6 names").grid(column=3, row=4)
s6 = ttk.Entry(frm, width=10)
s6.grid(column=4,row=4)
ttk.Label(frm, text="% Chance of TCIADOT names").grid(column=3, row=5)
tciadot = ttk.Entry(frm, width=10)
tciadot.grid(column=4,row=5)
ttk.Label(frm, text="% Chance of EAEB names").grid(column=3, row=6)
eaeb = ttk.Entry(frm, width=10)
eaeb.grid(column=4,row=6)
ttk.Label(frm, text="% Chance of EAEBCD names").grid(column=3, row=7)
eaebm = ttk.Entry(frm, width=10)
eaebm.grid(column=4,row=7)
ttk.Label(frm, text="% Chance of Additional text").grid(column=3, row=8)
aText = ttk.Entry(frm, width=10)
aText.grid(column=4,row=8)
ttk.Button(frm, text="Set all 100", command=setAll100).grid(column=5, row=0)
ttk.Button(frm, text="Set all 0", command=setAll0).grid(column=5, row=1)
ttk.Button(frm, text="Import text from .txt file", command=inFile).grid(column=0, row=9)
ttk.Button(frm, text="Export text to .txt file", command=outFile).grid(column=1, row=9)
root.mainloop()

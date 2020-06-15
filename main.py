import gkeepapi

old_keep = gkeepapi.Keep()
suc = old_keep.login('OLD_EMAIL','OLD_PASSWORD') #Fill in info

new_keep = gkeepapi.Keep()
suc = new_keep.login('NEW_EMAIL','NEW_PASSWORD') #Fill in info

notes = old_keep.all()

for x in notes:
    if(notes.index(x) >= 0): #For me the first 2 notes always came up as NULL
                             #so try changing the 0 to a 2 if that is an issue
        if(str(type(x)) == "<class 'gkeepapi.node.Note'>"):
            newnote = new_keep.createNote(x.title,x.text)
##            print(x.text)
            
        elif(str(type(x)) == "<class 'gkeepapi.node.List'>"):
            listitems = x.items
            newnote = new_keep.createList(x.title,[])
            for i in listitems:
                newnote.add(i.text,i.checked)          
##            print(x.text)

        else:
            print("ERROR" + str(type(x)) + "\n" + "On note: " x.title)


        for i in x.labels.all():
            label_names = []
            labels = new_keep.labels()
            for v in labels:
                label_names.append(v.name)
            if i.name in label_names:
                newnote.labels.add(list(labels)[label_names.index(i.name)])
            else:
                newlabel = new_keep.createLabel(i.name)
                newnote.labels.add(newlabel)


new_keep.sync()


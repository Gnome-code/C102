import os, shutil 
fromDir =  "/Users/tanushtalekar/Downloads"
toDir = "/Users/tanushtalekar/Desktop/c102"
listOfFiles = os.listdir(fromDir)
#print(listOfFiles)
for i in listOfFiles:
    name, ext = os.path.splitext(i)
    #print(ext)
    if ext == "":
        continue
    if ext in [".png", ".jpeg", ".gif", ".jpg", ".jfif", ".JPG", ".odg", ".dwg", ".PNG"]:
        path1 = fromDir +"/"+ i
        path2 = toDir+"/"+"imagefiles"
        path3 = toDir+"/"+"imagefiles"+"/"+i
        if os.path.exists(path2):
            print("The file is being moved")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("The file is being moved")
            shutil.move(path1, path3)
    if ext in [".pdf",".txt", ".doc", ".docx", ".pptx", ".xlsx", ".html"]:
        path1 = fromDir +"/"+ i
        path2 = toDir+"/"+"docfiles"
        path3 = toDir+"/"+"docfiles"+"/"+i
        if os.path.exists(path2):
            print("The file is being moved")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("The file is being moved")
            shutil.move(path1, path3)
    if ext in [".jar",".zip"]:
        path1 = fromDir +"/"+ i
        path2 = toDir+"/"+"compfiles"
        path3 = toDir+"/"+"compfiles"+"/"+i
        if os.path.exists(path2):
            print("The file is being moved")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("The file is being moved")
            shutil.move(path1, path3)
    if ext in [".dmg"]:
        path1 = fromDir +"/"+ i
        path2 = toDir+"/"+"installers"
        path3 = toDir+"/"+"installers"+"/"+i
        if os.path.exists(path2):
            print("The file is being moved")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("The file is being moved")
            shutil.move(path1, path3)
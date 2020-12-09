import os, shutil
from distutils.dir_util import copy_tree
lakocion = "./"
inputLakocion = "otazky/"
sorceName = "otazka"
picture = "picture/"
suffix = ".md"

otputLakocion = "final/"

folders = ["pr/","tz/"]
names = ["prenosi_dat_a_signalu.md","telekomunikacni_zarizeni_a_systemy.md"]

number = 25

for i in range(len(folders)):
    lakocionOfOutputFile = lakocion + folders[i] + otputLakocion + names[i]
    lakocionOfOutputPictureFolder = lakocion + folders[i] + otputLakocion + picture 
    outputFile = open(lakocionOfOutputFile, "w+", encoding="utf-8")
    for j in range(1, number + 1):
        src = lakocion + folders[i] + inputLakocion + sorceName + str(j) + "/" + picture 
        copy_tree(src, lakocionOfOutputPictureFolder)
        lakocionOfinputFile = lakocion + folders[i] + inputLakocion + sorceName + str(j) + "/" + sorceName + str(j) + suffix
        inputFile = open(lakocionOfinputFile, "r", encoding="utf-8")
        text = inputFile.read()
        inputFile.close()
        outputFile.write(text)
    outputFile.close()

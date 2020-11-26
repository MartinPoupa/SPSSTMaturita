lakocion = "./"
endFile = "prenosi_dat_a_signalu.md"
sorceFolder = "otazky/"
sorceName = "otazka"
suffix = ".md"

number = 25


lakocionOfOutputFile = lakocion + endFile

outputFile = open(lakocionOfOutputFile, "w+", encoding="utf-8")


for i in range(1, number + 1):
    lakocionOfinputFile = lakocion + sorceFolder + sorceName + str(i) + "/" + sorceName + str(i) + suffix
    inputFile = open(lakocionOfinputFile, "r", encoding="utf-8")
    text = inputFile.read()
    inputFile.close()
    outputFile.write(text)
outputFile.close()

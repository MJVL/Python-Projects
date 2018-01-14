Flesch_Indexs = [91,81,71,61,51,31,0]
Flesch_Levels = ["5th Grade","6th Grade","7th Grade","8th and 9th Grade","10th to 12th Grade","College Student","College Graduate"];

Flesch_Score = int(input("Enter the text's flesch score: "))

for i in range(0,len(Flesch_Indexs)):
    if Flesch_Score >= Flesch_Indexs[i]:
        print(Flesch_Levels[i])
        break
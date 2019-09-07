import csv
import os   #stands for operating system

#udemy_csv= "./resources/web_starter.csv"   #OldSchool way
udemy_csv=os.path.join(".","resources","web_starter.csv")    #BetterWay

title=[]
price=[]
subscribers=[]
reviews=[]
reviews_percent=[]
length=[]


with open(udemy_csv,"r", encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    #test=next(csvreader)       #read first row

    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent=round(int(row[6])/int(row[5]),2)
        reviews_percent.append(percent)
        new_length=row[9].split(" ")
        length.append(float(new_length[0]))

#print("\n")
#print(test)    #print first row
#print(reviews_percent)    #print first row
#print("\n")

cleanCsv=zip(title,price,subscribers,reviews,reviews_percent,length)
outputFile=os.path.join("web_solved.csv")

with open (outputFile, "w", newline="\n") as datafile:
    writer=csv.writer(datafile)
    writer.writerow(["Title","Course Price","Subscribers","Reviews","% Reviews","Lenght of course"])
    writer.writerows(cleanCsv)




# We want the title, price, suscribers
# reviews, percent of review, length


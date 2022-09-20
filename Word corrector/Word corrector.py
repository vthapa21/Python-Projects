from textblob import TextBlob


#reading file
file = open("trial.txt", "r")
data = file.read()
data_into_list = data.replace('\n', ' ').split(".")
print(data_into_list)
file.close()

corrected_words=[]
for i in data_into_list:
    corrected_words.append(TextBlob(i))

print("Corrected words are\n")
for i in corrected_words:
    print(i.correct(),end=' ')
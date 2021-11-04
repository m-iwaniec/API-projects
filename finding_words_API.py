import requests

# datamuse API is a word-finding query engine
# words that rhyme with forgetful -	/words?rel_rhy=forgetful
# rel_rhy is keyword indicating to the API to get perfect rhymes for the word specified

print("words that rhyme with 'sing':\n")
parameter = {"rel_rhy":"sing"}
request = requests.get("https://api.datamuse.com/words?rel_rhy=sing")

# decode json
rhyme_json = request.json()
# slice the list to print first 5 words that rhyme
for i in rhyme_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words with a meaning similar to 'ringing in the ears':\n")
parameter = {"ml":"ringing in the ears"}
request = requests.get("https://api.datamuse.com/words?ml=ringing+in+the+ears")

meaning_json = request.json()
for i in meaning_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("adjectives describing ocean sorted by how related they are to temperature:\n")
request = requests.get("https://api.datamuse.com/words?rel_jjb=ocean&topics=temperature")

adj_describing_json = request.json()
for i in adj_describing_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words that are triggered by (strongly associated with) the word 'cow':\n")
request = requests.get("https://api.datamuse.com/words?rel_trg=cow")

associated_json = request.json()
for i in associated_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words that rhyme with 'grape' that are related to breakfast:\n")
request = requests.get("https://api.datamuse.com/words?ml=breakfast&rel_rhy=grape")

rhyme_related_json = request.json()
for i in rhyme_related_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("adjectives that are often used to describe 'ocean':\n")
request = requests.get("https://api.datamuse.com/words?rel_jjb=ocean")

adj_json = request.json()
for i in adj_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words that start with 't', end in 'k', and have 2 letters in between:\n")
request = requests.get("https://api.datamuse.com/words?sp=t??k")

letters_json = request.json()
for i in letters_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words that sound like 'jirraf':\n")
request = requests.get("https://api.datamuse.com/words?sl=jirraf")

sounds_like_json = request.json()
for i in sounds_like_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words related to duck that start with the letter 'b':\n")
request = requests.get("https://api.datamuse.com/words?ml=duck&sp=b*")

related_json = request.json()
for i in related_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("suggestions for the user if they have typed in rawand so far:\n")
request = requests.get("https://api.datamuse.com/sug?s=rawand")

suggestion_json = request.json()
for i in suggestion_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words that often follow 'drink' in a sentence, that start with the letter 'w':\n")
request = requests.get("https://api.datamuse.com/words?lc=drink&sp=w*")

words_follow_json = request.json()
for i in words_follow_json[0:5]:
    print(i['word'])

print("--------------------------------------------------------------------------------")


print("words related to 'spoon' that end with the letter 'a'\n")
request = requests.get("https://api.datamuse.com/words?ml=spoon&sp=*a")

ending_in_json = request.json()
for i in ending_in_json[0:5]:
    print(i['word'])
import requests

# https://www.datamuse.com/api/
print("Popular adjectives used to modify the given noun, per Google Books Ngrams:\n")
request = requests.get("https://api.datamuse.com/words?rel_jjb=beach")

r1_json = request.json()
for i in r1_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

print("Synonyms (words contained within the same WordNet synset):\n")
request = requests.get("https://api.datamuse.com/words?rel_syn=dog")

r2_json = request.json()
for i in r2_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

print("Triggers (words that are statistically associated with the query word in the same piece of text):\n")
request = requests.get("https://api.datamuse.com/words?rel_trg=farmer")

r3_json = request.json()
for i in r3_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

print("Homophones (sound-alike words):\n")
request = requests.get("https://api.datamuse.com/words?rel_hom=see")

r4_json = request.json()
for i in r4_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

print("Comprises (direct holonyms, per WordNet):\n")
request = requests.get("https://api.datamuse.com/words?rel_com=school")

r5_json = request.json()
for i in r5_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

print("Topic words: An optional hint to the system about the theme of the document "
      "being written. Results will be skewed toward these topics. "
      "At most 5 words can be specified. Space or comma delimited. Nouns work best.:\n")
request = requests.get("https://api.datamuse.com/words?topics=school")

r6_json = request.json()
for i in r6_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

print("Right context: An optional hint to the system about the word that"
      " appears immediately to the right of the target word in a sentence. "
      "(At this time, only a single word may be specified.):\n")
request = requests.get("https://api.datamuse.com/words?rc=tree")

r6_json = request.json()
for i in r6_json[0:5]:
    print(i['word'])

print("---------------------------------------------------------------------------")

# Metadata flags: extra lexical knowledge to be included with the results.
# Query echo: The presence of this parameter asks the system to prepend a result to
# the output that describes the query string from some other parameter, specified as
# the argument value. This is useful for looking up metadata about specific words.

print("The pronunciation and word frequency for 'flower':\n")
request = requests.get("https://api.datamuse.com/words?sp=flower&qe=sp&md=frd")

r7_json = request.json()
print(r7_json)

print("---------------------------------------------------------------------------")

print("Definitions for 'house':\n")
request = requests.get("https://api.datamuse.com/words?sp=house&qe=sp&md=d")

r8_json = request.json()
for i in r8_json[0:5]:
    print(i['defs'])

print("---------------------------------------------------------------------------")

print("The pronunciation and word frequency for 'puppy':\n")
request = requests.get("https://api.datamuse.com/words?sp=puppy&qe=sp&md=d")

r9_json = request.json()

print(r9_json)
print()

for i in r9_json[0:5]:
    print(i['defs'])

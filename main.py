from db import VectorDB
import numpy as np

vector_db = VectorDB()


# open senteces.txt
with open('headlines.txt', 'r') as f:
    sentences = f.readlines()
print("fetched from file")


count = 2000
random_idx = np.random.randint(0, len(sentences)-count)
sentences = sentences[random_idx:random_idx + count]
#sentences = np.random.permutation(sentences)
# randomize the order of the sentences
print("randomized the order of the sentences")

# Building the vocabulary
vocabulary = set()  # Initializing an empty set to store unique words
for sentence in sentences:  # Iterating over each sentence in the list
    tokens = sentence.lower().split()  # Tokenizing the sentence by splitting on whitespace and converting to lowercase
    vocabulary.update(tokens)  # Updating the set of vocabulary with unique tokens

print("Built the vocabulary")

# Assign unique indices to vocabulary words
word_to_index = {word: i for i, word in enumerate(vocabulary)} 

index_to_word = {i: word for word, i in word_to_index.items()}


vocab_data = {}
for sentence in sentences:
    tokens = sentence.lower().split()
    vector = np.zeros(len(vocabulary))
    for token in tokens:
        vector[word_to_index[token]] += 1
    vocab_data[sentence] = vector
print("Built the vocabulary data")

# store in vectorstore
for sentence, vector in vocab_data.items():  # Iterating over each sentence vector
    vector_db.add_vector(sentence, vector)  # Adding the sentence vector to the VectorStore

print("Stored in vectorstore")

queries = [
    "How is the weather today?", 
    "What is the time now?",
    "What is the future of Artificial Intelligence?",
#  "What is the best way to learn to play the guitar?",
 "How to plan a picnic?",
]

for query in queries:
    query_vector = np.zeros(len(vocabulary))
    query_tokens = query.lower().split()

    for token in query_tokens:
        if token in word_to_index:
            query_vector[word_to_index[token]] += 1

# querying the vectorstore with the query vector
    similar_sentences = vector_db.cosine_similarity(query_vector, count=3)  # Finding similar sentences

# Display similar sentences
    print("query:", query)
    print("\nsimilar:")
    for sentence, similarity in similar_sentences:  # Iterating over each similar sentence and its similarity score
        print(f"{sentence}\t:similarity = {similarity:.3f}")
    print("-" * 50)
    print("\n\n")

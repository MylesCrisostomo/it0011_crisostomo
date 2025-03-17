def count_unique_words(text): 
    excluded = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}  # list of words to exclude
    words, word_counts, word = [], {}, ""
    
    for char in text + " ":
        if char.isalpha(): # if character is a letter, add to the current word
            word += char
        elif word:
            if word.lower() not in excluded: # check if word is not in the excluded list
                word_counts[word] = word_counts.get(word, 0) + 1
            word = ""  # reset word for next word extraction
    
    sorted_words = sorted(word_counts, key=lambda x: (x[0].isupper(), x)) # sorts lowercase words first, then uppercase words
    
    print("\n")
    for w in sorted_words:  # print each word with its count
        print(w, " - ", word_counts[w])
    
    print("\nTotal words filtered:", sum(word_counts.values())) # print total number of filtered words

count_unique_words(input("Enter a string statement:\n"))

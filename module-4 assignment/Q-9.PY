def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
        words = content.split()

        word_frequency = {}
   
        for word in words:
            word = word.lower() 
            word_frequency[word] = word_frequency.get(word, 0) + 1

        return word_frequency

file_path = 'sample_text.txt'  
result = count_word_frequency(file_path)

for word, frequency in result.items():
    print(f'{word}: {frequency}')

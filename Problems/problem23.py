#reverse the sentence

sent = 'Welcome to India'

word_list = sent.split()
print(word_list)
r_word_list = word_list[::-1]
print(r_word_list)
r_sent = ' '.join(r_word_list)
print(r_sent)


sent = input()
r_sent = ' '.join(sent.split()[::-1])
print(r_sent)
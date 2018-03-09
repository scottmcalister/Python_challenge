import os
import string

file_num = 1

file_PyPara = 'paragraph_' + str(file_num) +'.txt'

paragraph_str = ''

with open(file_PyPara, 'r') as txtfile:
    paragraph_txt = txtfile.read()

sen_count = paragraph_txt.count('.') + paragraph_txt.count('?') + paragraph_txt.count('!')
letters = string.ascii_letters + " " 

for x in paragraph_txt:
    if x not in letters:
        paragraph_txt = paragraph_txt.replace(x,'')

paragraph_list = paragraph_txt.split()

letter_total = 0
for word in paragraph_list:
    letter_total += len(word)

word_count = len(paragraph_list)
avg_word_length = letter_total/word_count
words_per_sentence = word_count/sen_count

print('Paragraph Analysis\n-----------------\nApproximate Word Count: ' 
                        + str(word_count)+ '\nApproximate Sentence Count: '+ str(sen_count) + 
                        '\nAverage Letter Count: ' + str(avg_word_length) + 
                        '\nAverage Sentence Length: ' + str(words_per_sentence))


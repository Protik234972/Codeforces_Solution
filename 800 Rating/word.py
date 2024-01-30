old_list= "Hello my name is Protik Barua"
new_list = []
for sentence in old_list:
    sentence_list = []
    word = ''
    for ch in sentence:
        if ch == ' ' and word != '':
            sentence_list.append(word)
            word = ''
        else:
            word += ch
    if word != '':
        sentence_list.append(word)
    new_list.append(sentence_list)
print(new_list)
        


    
        
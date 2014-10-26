'''
The encryption key consists of three lower case characters, decrypt
the message and find the sum of the ASCII values in the original text.
'''

eng_words = ['and', 'the', 'The']
printable_ascii = frozenset(xrange(32, 127))
with open("p059_cipher.txt") as cipher:
    text = cipher.read()
text = map(int, text.split(','))

valid_letters = [[], [], []]
for i in xrange(3):
    for j in xrange(97, 123):
        exit_flag = False
        for k in xrange(i, len(text), 3):
            decrypt_val = j ^ text[k]
            if decrypt_val not in printable_ascii:
                exit_flag = True
                break
        if not exit_flag:
            valid_letters[i].append(j)

for a in valid_letters[0]:
    for b in valid_letters[1]:
        for c in valid_letters[2]:
            curr_translation = []
            pass_num = 0
            pass_letters = [a, b, c]
            for text_letter in text:
                curr_translation.append(pass_letters[pass_num] ^ text_letter)
                pass_num = (pass_num + 1) % 3

            string = ''.join(map(chr, curr_translation))
            words = frozenset(string.split(' '))
            if any(eng_word in words for eng_word in eng_words):
                print string, '\n', sum(curr_translation)

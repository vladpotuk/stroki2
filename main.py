text = input("Введіть текст: ")

reserved_words = input("Введіть список зарезервованих слів через кому: ").split(',')



for word in text.split():



 if word.lower() in reserved_words:

  text = text.replace(word, word.upper())



print(text)




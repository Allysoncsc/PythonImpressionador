


# a = 18
# b = 0


# try:
#   c = a/b
# except ZeroDivisionError:
#   print('tentou dividir por zero')
# except NameError:
#   print('Variavel não definida')
# except Exception:
#   print('ERRO desconhecido')





import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
text = '''Hoje é um grande dia.  Está ainda 
melhor do que ontem. E ontem foi o melhor 
dia de todos. Amanhã será um dia especial.'''
print("\nOriginal string:")
print(text)
token_text = sent_tokenize(text)
print("\nSentence-tokenized copy in a list:")
print(token_text)
print("\nRead the list:")
for s in token_text:
    print(s)
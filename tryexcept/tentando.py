


a = 18
b = 0


try:
  c = a/b
except ZeroDivisionError:
  print('tentou dividir por zero')
except NameError:
  print('Variavel não definida')
except Exception:
  print('ERRO desconhecido')











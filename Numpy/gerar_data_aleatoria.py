import numpy as np

def transformar_em_str(valor):
  
  if valor < 10:
    return '0'+str(valor)
  
  return str(valor)

rng = np.random.default_rng()


def gerar_mes():
  mes_aleatorio = rng.integers(low=1, high=10)
  mes_aleatorio = transformar_em_str(mes_aleatorio)
  return mes_aleatorio

def gerar_dia():
  dia_aleatorio = rng.integers(low=1, high=12)
  dia_aleatorio = transformar_em_str(dia_aleatorio)
  return dia_aleatorio









for i in range(11):
  data_aleatoria = '2023-'+gerar_mes()+'-'+gerar_dia()
  print(f"update aluno_curso set data_inscricao_curso = '{data_aleatoria}' where id_alunocurso = {i+1};")
















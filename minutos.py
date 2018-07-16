segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = segundos // 86400
seg_restantes = segundos % 86400
horas = seg_restantes // 3600
seg_restantes_final = seg_restantes % 3600
minutos = seg_restantes_final // 60
segundosf = seg_restantes_final % 60
print(dias, 'dias,', horas, 'horas, ', minutos, 'minutos e', segundosf, 'segundos.')
ovoshi=['огурец', 'тыква', 'морковь', 'капуста']
ovosh=input('добавьте к списку овощ:')
ovosh1=input('добавьте к списку ещё один овощ:')
ovoshi.append(ovosh)
ovoshi.append(ovosh1)
for prod in ovoshi:
    print(prod)
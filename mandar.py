ds = {
    "Thomas": [5,5,5,5,5]
}

with open ("alunos_3ds.html",'w',encoding="utf-8") as file:
    file.write(
        '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notas 3°DS</title>
    </head>
    <body>
      '''  
    )
    for c,v in ds.items():
        file.write(c)
        for itens in v:
            file.write("<br>")
            file.write(str(itens))
    file.write('''    
    </body>
</html>
'''
    )
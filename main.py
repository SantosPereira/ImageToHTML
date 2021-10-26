import cv2

htmlTemplate = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imagem</title>

    <style>
        #imagem {
            width: 600;
            height: 400;
        }

        
    '''

imagem = cv2.imread('user.png')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagem_saida = []

cont = 0
for i in range(len(imagem)):
    for j in range(len(imagem[i])):
        cont += 1
        style = '''#'''+str(cont)+''' {
            width: 1px;
            heigth: 1px;
            background-color: rgb(0,0,'''+str(imagem[i][j])+''');
        }'''
        div = '<div id="'+str(cont)+'"></div>\n'
        imagem_saida.append((style, div))
        
for item in imagem_saida:
    htmlTemplate += item[0]

htmlTemplate += '''
        </style>
    </head>
    <body>
        <div id="imagem">
        '''

for item in imagem_saida:
    htmlTemplate += item[1]

htmlTemplate += '''
    </div>
</body>
</html>
'''
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(htmlTemplate)
    file.close()
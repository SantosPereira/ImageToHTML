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

        
    </style>
</head>
<body>
    <div id="imagem">

    </div>
</body>
</html>
'''

imagem = cv2.imread('user.png')

print(imagem)




with open('page.html', 'w', encoding='utf-8') as file:
    file.write()
    file.close()
from ast import Return
import PySimpleGUI as pg
import json
from datetime import date
from PIL import Image
import os

TypeCourse = 1
TypePost = 1

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
f = open('Polos.JSON')
data = json.load(f)

y = 0
original = 0
dir = ''
curso = ''
i = 1
n = 0

pg.theme('DarkAmber')

path = ''
layout = [
          [pg.Text('Aspert Automático', font='Helvetica 38 bold')],
          [pg.Text('Tipo de Promocional')],

          [pg.Radio('Graduação', "CURSOS", default = True, key='graduacao'),
	       pg.Radio('Pós-Graduação', "CURSOS", key='pos'),
	       pg.Radio('Técnico', "CURSOS", key='tecnico'),
	       pg.Radio('Profissionalizante', "CURSOS", key='prof')],
	       
          [pg.Text('Formato do Promocional')],

          [pg.Radio('Post', "FORMATO", default = True, key='post'),
	       pg.Radio('Stories', "FORMATO", key='stories')],
	       
	      [pg.FileBrowse('Procurar Arquivo', key='input'),
           pg.Text('', key='file')],

	      [pg.Button('Começar'),
           pg.Button('Visualizar', key='view')],

          [pg.Image(key='image', expand_x=True, expand_y=True)]
         ]


window = pg.Window('Window Title', layout)


path1 = dir_path + '/Centro Sul/'
for f in os.listdir(path1):
    os.remove(os.path.join(path1,f))

path2 = dir_path + '/Sul/'
for f in os.listdir(path2):
    os.remove(os.path.join(path2,f))

path3 = dir_path + '/Serra Gaucha/'
for f in os.listdir(path3):
    os.remove(os.path.join(path3,f))

def getCourse(values):
    if values['graduacao']: TypeCourse = 1
    if values['pos']: TypeCourse = 2
    if values['tecnico']: TypeCourse = 3
    if values['prof']: TypeCourse = 4

    return TypeCourse

def getDirectory(TypeCourse):

    if TypeCourse == 1:
        
        dir = dir_path + '/Enderecos/'
        return dir

    if TypeCourse == 2:
        
        dir = dir_path + '/Enderecos/POS/'
        return dir

    if TypeCourse == 3:
       
        dir = dir_path + '/Enderecos/' 
        return dir

    if TypeCourse == 4:
        
        dir = dir_path + '/Enderecos/'
        return dir
    
def getNameCourse(TypeCourse):
    if TypeCourse == 1:

        return 'Graduacao'

    if TypeCourse == 2:

        return 'Pos Graduacao'

    if TypeCourse == 3:

        return 'Tecnico'

    if TypeCourse == 4:

        return 'Profissionalizante'

def getPosttype(values):
    if values['post']: TypePost = 1
    if values['stories']: TypePost = 2

    return TypePost

def view(Directory):
    layout = [[pg.Image(Directory, key="new", expand_x=True, expand_y=True)]]
    window = pg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == pg.WIN_CLOSED:
            break



while True:
    event,values = window.read()

    if event == 'Procurar Arquivo':
        window['file'].update(values['input'])

    if event == 'Começar':
        path = values['input']
        im1 = Image.open(path)

        dir = getDirectory(getCourse(values))
        curso = getNameCourse(getCourse(values))
        
        if getPosttype(values) == 1:
            y = 4186
            original = (1200,1200)
            im1 = im1.resize((5001,5001))

        if getPosttype(values) == 2:
            y = 7000
            original = (1080,1920)
            im1 = im1.resize((5016,8918))

        while i <= 11:        
            directory1 = dir + str(i) + '.png'
            directory2 = dir_path + '/Centro Sul/' + (data["Polos"][n]) + ' - ' + str(date.today()) + ' - ' + curso + '.png'
            im2 = Image.open(directory1)
            copied = im1.copy()
            copied.paste(im2,(5,y))
            copied = copied.resize(original)
            copied.save(directory2 , quality=95)
            i+=1
            n+=1


        while i > 11 and i <= 25:
            directory1 = dir + str(i) + '.png'
            directory2 = dir_path + '/Sul/' + (data["Polos"][n]) + ' - ' + str(date.today()) + ' - ' + curso + '.png'
            im2 = Image.open(directory1)
            copied = im1.copy()
            copied.paste(im2,(5,y))
            copied = copied.resize(original)
            copied.save(directory2 , quality=95)
            i+=1
            n+=1

        while i > 25 <= 38:
            directory1 = dir + str(i) + '.png'
            directory2 = dir_path + '/Serra Gaucha/' + (data["Polos"][n]) + ' - ' + str(date.today()) + ' - ' + curso + '.png'
            im2 = Image.open(directory1)
            copied = im1.copy()
            copied.paste(im2,(5,y))
            copied = copied.resize(original)
            copied.save(directory2 , quality=95)
            i+=1
            n+=1
    
    if event == 'view':
        
        path = values['input']
        im1 = Image.open(path)

        dir = getDirectory(getCourse(values))
        curso = getNameCourse(getCourse(values))
        
        if getPosttype(values) == 1:
            y = 4186
            original = (500,500)
            im1 = im1.resize((5001,5001))

        if getPosttype(values) == 2:
            y = 7000
            original = (501,891)
            im1 = im1.resize((5016,8918))

        directory1 = dir + '1.png'
        directory2 = dir_path + '/Centro Sul/View.png'
        im2 = Image.open(directory1)
        copied = im1.copy()
        copied.paste(im2,(5,y))
        copied = copied.resize(original)
        copied.save(directory2 , quality=95)

        view(directory2)


    if event == pg.WINDOW_CLOSED:
        break

window.close()
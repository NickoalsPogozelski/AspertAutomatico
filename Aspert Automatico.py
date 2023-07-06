from ast import Return
from tkinter import font
from weakref import finalize
import PySimpleGUI as pg
import json
from datetime import date
from PIL import Image
import os

#Variable Assignment

TypeCourse = 1
TypePost = 1
original = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
f = open('Polos.JSON')
data = json.load(f)

i = 1
n = 0
y = 0
original = 0

dir = ''
curso = ''

post = 4186
stories = 7000

#Window Theme

pg.theme('LightGray1')

#Window Layout

path = ''
layout = [
          [pg.Text('Aspert Automático', font=("Neo Sans Pro Ultra", 38, "bold"))],
          [pg.Text('TIPO DE PROMOCIONAL', font=("Neo Sans Pro Medium", 12, "bold"), text_color = "#00aea9")],

          [pg.Radio('Graduação', "CURSOS", default = True, key='graduacao',  font=("Neo Sans Pro", 12)),
	       pg.Radio('Pós-Graduação', "CURSOS", key='pos', font=("Neo Sans Pro", 12)),
	       pg.Radio('Técnico', "CURSOS", key='tecnico', font=("Neo Sans Pro", 12)),
	       pg.Radio('Profissionalizante', "CURSOS", key='prof', font=("Neo Sans Pro", 12))],
	       
          [pg.Text('FORMATO DO PROMOCIONAL', font=("Neo Sans Pro Medium", 12, "bold"), text_color = "#00aea9")],

          [pg.Radio('Post', "FORMATO", default = True, key='post', font=("Neo Sans Pro", 12)),
	       pg.Radio('Stories', "FORMATO", key='stories', font=("Neo Sans Pro", 12))],
	       
	      [pg.FileBrowse('Procurar Arquivo', key='input'),
           pg.Text('', key='file', text_color="#fada00")],

	      [pg.Button('Começar'),
           pg.Button('Visualizar', key='view'),
           pg.Push(),
           pg.Image('Logos.png', expand_x=True, expand_y=True)]
           

         ]


window = pg.Window('Window Title', layout, finalize=True, icon='Icon.ico')
window.set_title("ASPERT AUTOMÁTICO")

#Region Folders' Path

path1 = dir_path + '/Centro Sul/'
for f in os.listdir(path1):
    os.remove(os.path.join(path1,f))

path2 = dir_path + '/Sul/'
for f in os.listdir(path2):
    os.remove(os.path.join(path2,f))

path3 = dir_path + '/Serra Gaucha/'
for f in os.listdir(path3):
    os.remove(os.path.join(path3,f))

###FUNCTIONS###

#Gets Value from selected Radio element

def getCourse(values):
    if values['graduacao']: TypeCourse = 1
    if values['pos']: TypeCourse = 2
    if values['tecnico']: TypeCourse = 3
    if values['prof']: TypeCourse = 4

    return TypeCourse

#Assigns directory based on values (That's the directory where the adresses are at)

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
    
#Returns course name based on values

def getNameCourse(TypeCourse):

    if TypeCourse == 1:

        return 'Graduacao'

    if TypeCourse == 2:

        return 'Pos Graduacao'

    if TypeCourse == 3:

        return 'Tecnico'

    if TypeCourse == 4:

        return 'Profissionalizante'

#Gets value from radio elements

def getPosttype(values):

    if values['post']: TypePost = 1
    if values['stories']: TypePost = 2

    return TypePost

#Defines View window's layout

def view(Directory):
    layout = [[pg.Image(Directory, key="new", expand_x=True, expand_y=True)],
              [pg.Button('↑', key='up'),
               pg.Button('↓', key='down')]]
    window = pg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == pg.WIN_CLOSED:
            break

#Main Loop

while True:
    event,values = window.read()

    if event == 'Procurar Arquivo':
        
        window['file'].update(values['input'])

    if event == 'Começar':

        #Getting image from input field

        path = values['input']
        im1 = Image.open(path)

        #Getting directory and course name

        dir = getDirectory(getCourse(values))
        curso = getNameCourse(getCourse(values))
        
        #Setting address' position on the y axis based on post type

        if getPosttype(values) == 1:
            y = post
            original = (1200,1200)
            im1 = im1.resize((5001,5001))

        if getPosttype(values) == 2:
            y = stories
            original = (1080,1920)
            im1 = im1.resize((5016,8918))
        
        #Image Pasting
        #Centro Sul

        while i <= 11: 

            #Setting directory 1 to address folder and directory 2 to final folder

            directory1 = dir + str(i) + '.png'
            directory2 = dir_path + '/Centro Sul/' + (data["Polos"][n]) + ' - ' + str(date.today()) + ' - ' + curso + '.png'

            #Opening address image, copying and pasting it on top of the promo

            im2 = Image.open(directory1)
            copied = im1.copy()
            copied.paste(im2,(5,y))

            #Resizing the final image so it's not too big and saving it

            copied = copied.resize(original)
            copied.save(directory2 , quality=95)

            #Increase Counter

            i+=1
            n+=1

        #Sul

        while i > 11 and i <= 25:

            #Setting directory 1 to address folder and directory 2 to final folder

            directory1 = dir + str(i) + '.png'
            directory2 = dir_path + '/Sul/' + (data["Polos"][n]) + ' - ' + str(date.today()) + ' - ' + curso + '.png'

            #Opening address image, copying and pasting it on top of the promo

            im2 = Image.open(directory1)
            copied = im1.copy()
            copied.paste(im2,(5,y))

            #Resizing the final image so it's not too big and saving it

            copied = copied.resize(original)
            copied.save(directory2 , quality=95)

            #Increase Counter

            i+=1
            n+=1

        #Serra Gaucha

        while i > 25 and i <= 38:

            #Setting directory 1 to address folder and directory 2 to final folder
            
            directory1 = dir + str(i) + '.png'
            directory2 = dir_path + '/Serra Gaucha/' + (data["Polos"][n]) + ' - ' + str(date.today()) + ' - ' + curso + '.png'

            #Opening address image, copying and pasting it on top of the promo

            im2 = Image.open(directory1)
            copied = im1.copy()
            copied.paste(im2,(5,y))

            #Resizing the final image so it's not too big and saving it

            copied = copied.resize(original)
            copied.save(directory2 , quality=95)

            #Increase Counter
            
            i+=1
            n+=1

        i = 1
        n = 0

        
    #Handles View Button

    if event == 'view':
        
        #Open Image

        path = values['input']
        im1 = Image.open(path)

        #get Directory and Course Name

        dirc = getDirectory(getCourse(values))
        curso = getNameCourse(getCourse(values))
        
        #Resizing images based on post Type

        if getPosttype(values) == 1:
            y = stories
            original = (500,500)
            im1 = im1.resize((5001,5001))

        if getPosttype(values) == 2:
            y = stories
            original = (501,891)
            im1 = im1.resize((5016,8918))

        #Getting First Picture on Addresses List

        directory1 = dirc + '1.png'
        directory2 = dir_path + '/Centro Sul/View.png'

        #Copying and Pasting images

        im2 = Image.open(directory1)
        copied = im1.copy()
        copied.paste(im2,(5,y))
 
        #Resizing to original size so it's not too big

        copied = copied.resize(original)
        copied.save(directory2 , quality=95)

        view(directory2)

    if event == pg.WINDOW_CLOSED:
        break

window.close()
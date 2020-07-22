import kivy
kivy.require('1.11.1')

from math import inf
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
#Kivy properties will help to interchange data between the py and the kv file
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

class BoxTicTacToe(BoxLayout):
    tic = NumericProperty(1)

    #tells us whether the  game is on. Can be set to 1 by pressing the button
    play = NumericProperty(0)

    #this is what we'll display later on the tiles/buttons
    image = StringProperty('')
    
    #array of the fields. First all are not occupied, hence infinity. Later on 1 and 0 will be for the values of the player
    tictactoe = ObjectProperty([inf for i in range(9)])
    
    def selecCell(self):
        if self.tic :
            self.tic=0
        else:
            self.tic=1
    
    def imageCell(self):
        #self.inserting(3,1)
        
        if self.tic : 
            self.image = 'X'
        else:
            self.image = 'O'
    
    def inserting(self,ind,val):
        #insert the value at the given index. First check that there this field is in fact free 
        if self.tictactoe[ind] != inf:
            pass
        else:
            self.tictactoe[ind] = val

    def gameover(self):
        rows = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
        if self.tictactoe.count(inf)==0:
            self.play = 0
            popup = Popup(title='Gameover', content=Label(text='Draw'),size_hint_y=0.25,size_hint_x = 0.75)
            popup.open()
            self.tictactoe = [inf for i in range(9)]
            #write in the statistics file
            return(2)
        for L in rows:
            sum = self.tictactoe[L[0]]+self.tictactoe[L[1]]+self.tictactoe[L[2]]
            if sum==0:
                self.play = 0
                popup = Popup(title='Gameover', content=Label(text='Congratulations!! Player O has won'),size_hint_y=0.25,size_hint_x = 0.75)
                popup.open()
                self.tictactoe = [inf for i in range(9)]
                #write in the statistics file
                return(0)
            if sum==3:
                self.play = 0
                popup = Popup(title='Gameover', content=Label(text='Congratulations!! Player X has won'),size_hint_y=0.25,size_hint_x = 0.75)
                popup.open()
                self.tictactoe = [inf for i in range(9)]
                #write in the statistics file
                return(1)
        #checks whether a player has won and raises the final message
    
    def reset_game(self):
        self.tictactoe = [inf for i in range(9)]
        self.tic = 1

class Statistics(BoxLayout):
    def read_data(self):
        pass
    

        

class TicTacToeApp(App):
    icon = 'cover_ttt.png'
    def build(self):
        self.title = "TIC-TAC-TOE"
        return BoxTicTacToe()
        #return Statistics()

if __name__=='__main__':
    Config.set('graphics','width','800')
    Config.set('graphics','height','800')
    game = TicTacToeApp()
    game.run()

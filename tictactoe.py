import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton

Window.size = (360,660)

class TicTacToe(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        helper = Builder.load_file("tictactoeui.kv")
        return helper
    
    turn = 1
    theme = "light"

    def event_handling(self):
        btn1 = self.root.ids.btn1.background_normal
        btn2 = self.root.ids.btn2.background_normal
        btn3 = self.root.ids.btn3.background_normal
        btn4 = self.root.ids.btn4.background_normal
        btn5 = self.root.ids.btn5.background_normal
        btn6 = self.root.ids.btn6.background_normal
        btn7 = self.root.ids.btn7.background_normal
        btn8 = self.root.ids.btn8.background_normal
        btn9 = self.root.ids.btn9.background_normal

        popup = ""

        if btn1 == btn2 == btn3:
            popup = btn1
        elif btn4 == btn5 == btn6:
            popup = btn4
        elif btn7 == btn8 == btn9:
            popup = btn7
        elif btn1 == btn4 == btn7:
            popup = btn1
        elif btn2 == btn5 == btn8:
            popup = btn2
        elif btn3 == btn6 == btn9:
            popup = btn3
        elif btn1 == btn5 == btn9:
            popup = btn1
        elif btn3 == btn5 == btn7:
            popup = btn3
        elif self.root.ids.btn1.disabled == True and self.root.ids.btn2.disabled == True and self.root.ids.btn3.disabled == True and self.root.ids.btn4.disabled == True and self.root.ids.btn5.disabled == True and self.root.ids.btn6.disabled == True and self.root.ids.btn7.disabled == True and self.root.ids.btn8.disabled == True and self.root.ids.btn9.disabled == True:
            popup = 'draw'

        if popup == 'x.jpg':
            self.dialog = MDDialog(title="X WON",buttons=[MDRectangleFlatButton(text = "New Game",on_release = self.newgame)])
            self.dialog.open()
        elif popup == 'o.jpg':
            self.dialog = MDDialog(title="O WON",buttons=[MDRectangleFlatButton(text = "New Game",on_release = self.newgame)])
            self.dialog.open()
        elif popup == 'draw':
            self.dialog = MDDialog(title="GAME DRAW",buttons=[MDRectangleFlatButton(text = "New Game",on_release = self.newgame)])
            self.dialog.open()

    def game_draw(self):
        if self.root.ids.btn1.disabled == True and self.root.ids.btn2.disabled == True and self.root.ids.btn3.disabled == True and self.root.ids.btn4.disabled == True and self.root.ids.btn5.disabled == True and self.root.ids.btn6.disabled == True and self.root.ids.btn7.disabled == True and self.root.ids.btn8.disabled == True and self.root.ids.btn9.disabled == True:
            self.dialog = MDDialog(title="GAME DRAW",buttons=[MDRectangleFlatButton(text = "New Game",on_release = self.newgame)])
            self.dialog.open()
    
    def pressed(self,btn):
        if self.turn==1:
            btn.background_normal = "x.jpg"
            self.root.ids.labelx.text_color = (1,0,0,.3)
            self.root.ids.labelo.text_color = (0,0,1,1)
            btn.disabled = True
            btn.background_disabled_normal= "x.jpg"
            self.event_handling()
            self.turn=0
        else:
            btn.background_normal = "o.jpg"
            self.root.ids.labelo.text_color = (0,0,1,.3)
            self.root.ids.labelx.text_color = (1,0,0,1)
            btn.disabled = True
            btn.background_disabled_normal= "o.jpg"
            self.event_handling()
            self.turn=1

    def change_theme(self):
        if self.theme == "dark":
            self.theme_cls.theme_style = "Light"
            self.theme = "light"
        else:
            self.theme_cls.theme_style = "Dark"
            self.theme = "dark"

    def refresh(self):
        self.enable_btn()
        self.root.ids.btn1.background_normal = "blank.jpg"
        self.root.ids.btn2.background_normal = "blank.jpg"
        self.root.ids.btn3.background_normal = "blank.jpg"
        self.root.ids.btn4.background_normal = "blank.jpg"
        self.root.ids.btn5.background_normal = "blank.jpg"
        self.root.ids.btn6.background_normal = "blank.jpg"
        self.root.ids.btn7.background_normal = "blank.jpg"
        self.root.ids.btn8.background_normal = "blank.jpg"
        self.root.ids.btn9.background_normal = "blank.jpg"
        self.turn = 1

    def newgame(self,obj):
        self.refresh()
        self.dialog.dismiss()
        self.root.ids.labelx.text_color = (1,0,0,1)
        self.root.ids.labelo.text_color = (0,0,1,.3)

    def enable_btn(self):
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

    
TicTacToe().run()

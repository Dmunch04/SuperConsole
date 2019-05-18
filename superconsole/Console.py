import os
from DavesLogger import Logs

class OutConsole:
    def Print (self, _Message = ''):
        print (_Message)

    def Put (self, _Message = ''):
        print (_Message, end = ' ')

class InConsole:
    def Get (self, _Text = '', _Message = ''):
        Text = ''

        while Text != _Text:
            Text = input (_Message)

        return True

class Color:
    def __init__ (self):
        self.Reset = '\033[0m'
        self.End = '\033[0m'
        self.White = '\033[1;37m'
        self.LightGray = '\033[0;37m'
        self.Gray = '\033[1;37m'
        self.Black = '\033[0;30m'
        self.Red = '\033[0;31m'
        self.LightRed = '\033[1;31m'
        self.Blue = '\033[0;34m'
        self.LightBlue = '\033[1;34m'
        self.Green = '\033[0;32m'
        self.LightGreen = '\033[1;32m'
        self.Yellow = '\033[0;33m'
        self.LightYellow = '\033[1;33m'
        self.Purple = '\033[0;35m'
        self.LightPurple = '\033[1;35m'
        self.Cyan = '\033[0;36m'

class Logger:
    def __init__ (self):
        self.Debug = Logs.Debug
        self.Warning = Logs.Warning
        self.Error = Logs.Error
        self.Success = Logs.Success
        self.Server = Logs.Server

class Console:
    def __init__ (self, Title = ''):
        self.Title = Title
        self.Out = OutConsole ()
        self.In = InConsole ()
        self.Color = Color ()
        self.Logger = Logger ()

    def Tell (self, _Message = ''):
        print (f'<Tell.[{_Message}]@Console.Out>')

    def Clear (self):
        # Windows
        if os.name == 'nt':
            Clear = os.system ('cls')

        # MacOS and Linux
        else:
            Clear = os.system ('clear')

    def Dir (self):
        # Windows
        if os.name == 'nt':
            Files = os.system ('dir')

        # MacOS and Linux
        else:
            Files = os.system ('ls')

    def Move (self, _NewPath = '/'):
        # Windows
        if os.name == 'nt':
            Move = os.system ('cd ' + _NewPath)

        # MacOS and Linux
        else:
            Move = os.system ('cd ' + _NewPath)

    def Run (self, _Title = ''):
        if _Title == '':
            _Title = self.Title

        try:
            while True:
                Text = input (f'{_Title} >>> ')

        except KeyboardInterrupt:
            print ('Exiting..')
            return

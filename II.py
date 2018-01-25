class II:
    def __init__(self, msg):
        self.msg = msg
    
        if str(self.msg) == None:
            print("!!!")

        else:
            self.speak(self.msg)

    def speak(self, msg):
        if self.msg == "Привет" or self.msg == "привет":
            print(self._Speak([
                "Привет"
            ]))
        
    def _Speak(self, txt):
        return str(txt[0])


if __name__ == "__main__":
    msg = str(input("> "))
    
    ii = II(msg)
    
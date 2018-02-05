from lib.lib1 import STRS

class II:
    def __init__(self, msg):
        self.msg = msg
    
        if str(self.msg) is None:
            print("!!!")

        else:
            self.speak(self.msg)

    def speak(self, msg):
        if self.msg == STRS[1] or self.msg == STRS[1.1]:
            print(self._Speak({
                1: "Привет"
            }))

        elif self.msg == STRS[2] or self.msg == STRS[2.2]:
            print(self.plus())
        
    def _Speak(self, txt):
        return str(txt[1])

    def plus(self):
        try:
            num1 = int(input("> "))
            num2 = int(input("> "))

            return(num1 + num2)

        except:
            return "Введите число!"


if __name__ == "__main__":
    while True:
        msg = str(input("> "))
    
        ii = II(msg)

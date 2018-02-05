from lib.lib1 import STRS
from lib.classes.Base import Base


class II(Base):
    def __init__(self, msg):
        self.msg = msg

        if str(self.msg) is None:
            print("!!!")

        else:
            self.speak(self.msg)

    def speak(self, msg):
        if self.msg == STRS[1] or self.msg == STRS[1.2]:
            print(self._Speak({
                1: "Привет"
            }))

        elif self.msg == STRS[2] or self.msg == STRS[2.2]:
            self.plus()

        elif self.msg == STRS[3] or self.msg == STRS[3.2]:
            self.minus()

        elif self.msg == STRS[4] or self.msg == STRS[4.2]:
            self.umn()

        elif self.msg == STRS[5] or self.msg == STRS[5.2]:
            self.delen()

        elif self.msg == STRS[6] or self.msg == STRS[6.2]:
            self.step()

        else:
            print("Введите что-нобудь!")

    @staticmethod
    def _Speak(txt):
        return str(txt[1])

    def plus(self):
        super().plus()

    def minus(self):
        super().minus()

    def umn(self):
        super().umn()

    def delen(self):
        super().delen()

    def step(self):
        super().step()


if __name__ == "__main__":
    while True:
        msg = str(input("> "))

        ii = II(msg)

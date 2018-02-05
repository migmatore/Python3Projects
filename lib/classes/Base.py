class Base:
    def plus(self):
        try:
            num1 = int(input("> "))
            num2 = int(input("> "))

            print(num1 + num2)

        except:
            print("Введите число!")

    def minus(self):
        try:
            num1 = int(input("> "))
            num2 = int(input("> "))

            print(num1 - num2)

        except:
            print("Введите число!")

    def umn(self):
        try:
            num1 = int(input("> "))
            num2 = int(input("> "))

            print(num1 * num2)

        except:
            print("Введите число!")

    def delen(self):
        try:
            num1 = int(input("> "))
            num2 = int(input("> "))

            if num2 != 0:
                print(num1 / num2)

            else:
                print("Нельзя делить на 0!")

        except:
            print("Введите число!")

    def step(self):
        try:
            num1 = int(input("> "))
            num2 = int(input("> "))

            print(num1 ** num2)

        except:
            print("Введите число!")
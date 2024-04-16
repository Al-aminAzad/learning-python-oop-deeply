class Pritom:
    @staticmethod
    def greet():
        print("Hello from Pritom")

    @staticmethod
    def dance():
        Pritom.greet()
        print("Dance moyna")

    @classmethod
    def sing(cls):
        print(cls)
        cls.greet()
        print("Sing baby")


class Kundu(Pritom):

    @staticmethod
    def greet():
        print("Hello from Kundu")


Pritom.sing()

Kundu.sing()

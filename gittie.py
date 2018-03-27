def introduce():
    print("Hello, I'm gittie - What do you want?")
    print("Gyertya says you are cool!")


def add(a, b):
    print('A ket szam osszege:', a + b)
    print('Most ki is vonjuk oket:', a - b)


def joke():
    print("The first computer dates back to Adam and Eve. It was an Apple with limited memory," +
          "just one byte. And then everything crashed.")
    print('That was a joke. Did you get it?')


def shout():
    print("WHAT ARE YOU DOING?\n" * 50)


introduce()

a = int(input('Kerlek adj meg egy szamot!'))
b = int(input('Most pedig egy masikat szamot!'))

add(a, b)
shout()

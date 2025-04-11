class Kutya:
    def __init__(self,nev):
        self.nev=nev

    def ugat(self,uzenet):
        print(f"{uzenet}")

my_kutya = Kutya('Bodri')

my_kutya.ugat('vau1')

Kutya.ugat(my_kutya,'vau2')

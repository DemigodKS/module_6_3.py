
class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx
        #print(self.x_distance)

#horse = Horse()
#horse.run(10)
class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy
        #print(self.y_distance)

class Pegasus(Horse, Eagle):
    def get_pos(self):
        return (self.x_distance,self.y_distance)
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return (self.x_distance, self.y_distance)

    def voice(self):
        return (Horse.sound, Eagle.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(15, 23)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

print(p1.voice())



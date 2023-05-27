class Gep():
    def __init__(self, type, age, passangers, staff, speed, takeOffWeight, distance):
        self.type = type
        self.age = int(age)
        self.passangers = passangers
        self.staff = staff
        self.speed = int(speed)
        self.takeOffWeight = int(takeOffWeight)
        self.distance = distance
    def __str__(self):
        return f'{self.type} {self.age} {self.passangers} {self.staff} {self.speed} {self.takeOffWeight} {self.distance}'


def read_file():
    with open('utasszallitok.txt', 'r') as file:
        lines = file.readlines()
        aircrafts = []
        for line in range(1, len(lines)):
            attributes = lines[line].split(";")
            aircrafts.append(Gep(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6]))
        return aircrafts

def fifth_task(aircrafts):
    db = 0
    for aircraft in aircrafts:
        if "Boeing" in aircraft.type:
            db += 1
    return db

def sixth_task(aircrafts):
    max_passangers = 0
    winner_aircraft = None
    for aircraft in aircrafts:
        if "-" in aircraft.passangers:
            active = aircraft.passangers.split("-")
            if int(active[1]) > max_passangers:
                max_passangers = int(active[1])
                winner_aircraft = aircraft
        else:
            if int(aircraft.passangers) > max_passangers:
                max_passangers = int(aircraft.passangers)
                winner_aircraft = aircraft
    return winner_aircraft
        
def sebessegkategoria(speed):
    if speed < 500: return "Alacsony sebességű"
    elif speed < 1000: return "Szubszonikus"
    elif speed < 1200: return "Transzszonikus"
    else : return "Szuperszonikus"

def hetedik_task(aircrafts):
    speedtypes = {"Alacsony sebességű": 0, "Szubszonikus": 0, "Transzszonikus": 0, "Szuperszonikus": 0}
    for aircraft in aircrafts:
        speedtype = sebessegkategoria(aircraft.speed)
        speedtypes[speedtype] += 1
    for type,count in speedtypes.items():
        if count == 0:
            return type

        

def main():
    aircrafts = read_file()
    print(f'4. feladat: {len(aircrafts)} repülőgép adatai')
    print(f'5. feladat: {fifth_task(aircrafts)} db Boeing repülőgép van az adatok között')
    print(f"6. feladat: A legtöbb utast szállító repülőtípus\n Típus: {sixth_task(aircrafts).type}\n Gyártás éve: {sixth_task(aircrafts).age}\n Személyzet: {sixth_task(aircrafts).staff}\n Sebesség: {sixth_task(aircrafts).speed}\n Felszálló tömeg: {sixth_task(aircrafts).takeOffWeight}\n Hatótávolság: {sixth_task(aircrafts).distance}")
    print (f'7. feladat: {hetedik_task(aircrafts)} típusú repülőgép nem szerepel az adatok között')
    
    
main()
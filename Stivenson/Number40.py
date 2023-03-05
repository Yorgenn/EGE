QUITE_ROOM: int = 40
ALARM_CLOCK: int = 70
GAZ_MOWER: int = 106
JACKHAMMER: int = 130

db: int = int(input("Введите количество децибел: "))

if db < QUITE_ROOM:
    print("Меньше чем в тихой комнате ")
elif db == QUITE_ROOM:
    print("Децибелы равны тихой комнате")
elif QUITE_ROOM < db and db < ALARM_CLOCK:
    print("Децибелы между тихой комнатой и будильником ")
elif db == ALARM_CLOCK:
    print("Децибелы равны будильнику ")
elif ALARM_CLOCK < db and db < GAZ_MOWER:
    print("Децибелы находятся между будильником и газовой газонокосилкой ")
elif db == GAZ_MOWER:
    print("Децибелы равны газовой газонокосилке ")
elif GAZ_MOWER < db and db < JACKHAMMER:
    print("Децибелы находятся между газовой газонокосилкой и отбойным молотком ")
elif db == JACKHAMMER:
    print("Децибелы равны отбойному молотку ")
else:
    print("Децибелы больше чем у отбойного молотка ")

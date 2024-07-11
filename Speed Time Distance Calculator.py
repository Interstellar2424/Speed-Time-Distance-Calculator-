print("Speed Time and Distance Calculator -- A Project by Interstellar2424")
print("Kindly type in relevent units for appropriate answers and Do Not also type units along with constants.")
print("The Calculation will be based on units: km, m, hrs, sec, km/hrs, m/sec")

parat = ("speed, time", "distance, speed", "distance, time")

para = input("What are the two parameters (speed, time, distance) (write by seperating comma): ")

while para not in parat:
    para = input("what are the two parameters (speed, time, distance) (write by separating comma): ")

if para == "speed, time":
    speed1 = input("Speed: ")
    time1 = input("Time: ")
    distance = int(speed1) * int(time1)
    unit = input("unit (km, m): ")
    units = ("km", "m")
    while unit not in units:
        unit = input("unit (km, m): ")
    if unit == "km":
        print("|Speed (" + str(speed1) + ")|" + "*" + "|Time (" + str(time1) + ")|" "  -----> Distance: " + str(distance) + " km\n")
    elif unit == "m":
        print("|Speed (" + str(speed1) + ")|" + "*" + "|Time (" + str(time1) + ")|" "  -----> Distance: " + str(distance) + " m\n")

elif para == "distance, speed":
    speed2 = input("Speed: ")
    distance1 = input("Distance: ")
    time = int(distance1) / int(speed2)
    unit = input("unit (hrs, sec): ")
    units = ("hrs", "sec")
    while unit not in units:
        unit = input("unit (hrs, sec): ")
    if unit == "hrs":
        print("|Distance (" + str(distance1) + ")|" + "/" + "|Speed (" + str(speed2) + ")|" "  -----> Time: " + str(time) + " hrs\n")
    elif unit == "sec":
        print("|Distance (" + str(distance1) + ")|" + "/" + "|Speed (" + str(speed2) + ")|" "  -----> Time: " + str(time) + " sec\n")

elif para == "distance, time":
    distance2 = input("Distance: ")
    time2 = input("Time: ")
    speed = int(distance2) / int(time2)
    unit = input("unit (km/hrs, m/sec): ")
    units = ("km/hrs", "m/sec")
    while unit not in units:
        unit = input("unit (km/hrs, m/sec): ")
    if unit == "km/hrs":
        print("|Distance (" + str(distance2) + ")|" + "/" + "|Time (" + str(time2) + ")|" "  -----> Speed: " + str(speed) + " km/hrs\n")
    elif unit == "m/sec":
        print("|Distance (" + str(distance2) + ")|" + "/" + "|Time (" + str(time2) + ")|" "  -----> Speed: " + str(speed) + " m/sec\n")

formula = input("Type (f) to see Formula behind it and (no) to exit: ")

ft = ("f", "no")

while formula not in ft:
    formula = input("Type (f) to see Formula behind it and (no) to exit: ")

if formula == "f":
    print("           --")
    print("          |car|")
    print("           --")
    print("          O)  O)")
    print("")
    print("                    Distance = Speed * Time")
    print("                    Speed = Distance / Time")
    print("                    Time = Distance / Speed")
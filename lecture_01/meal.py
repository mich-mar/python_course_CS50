def main():
    time = input("What time is it? ")
    time = convert(time)

    print("time:", time)

    if(time>=7.0 and time<=8.0):
        print("Breakfast time")
    elif(time>=12.0 and time<=13.0):
        print("Lunch time")
    elif(time>=18.0 and time<=19.0):
        print("Dinner time")

def convert(time):
    time = time.split(':')
    return float(time[0]) + float(time[1])/60

main()

init = input("> ").lower()

if init == "help":
    print("start - to start the car")
    print("stop  - to stop the car")
    print("quit  - to quit the game")

    car_started = False

    while True:
        command = input("> ").lower()

        if command == "start":
            if car_started:
                print("Car already started!")
            else:
                car_started = True
                print("Car started... less goo ")

        elif command == "stop":
            if not car_started:
                print("Car is already stopped!")
            else:
                car_started = False
                print("Car stopped.")

        elif command == "quit":
            print("Game Ended")
            break

        else:
            print("I don't understand that command")
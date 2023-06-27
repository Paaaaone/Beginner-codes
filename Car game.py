started = False
while True:
    command = input(">")
    if command == "start":
        if started:
            print('already started')
        else:
            started = True
            print('car started lets go')
    elif command == "stop":
        if not started:
            print('already stopped')
        else:
            started = False
            print('car stopped')
    elif command == "quit":
        print('bye')
        break
    elif command == "help":
        print('Start - start car')
        print('Stop - stop car')
        print('quit - exit game')
    else:
        print('I dont understand dickhead')
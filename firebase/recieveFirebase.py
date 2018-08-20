from firebase import firebase
firebase =firebase.FirebaseApplication('https://python-3ff61.firebaseio.com/')
speed=255
def recieveData():
	recieve=firebase.get('/movement',None)
    return recieve



    # write this code in your code for recieving it
    #all commands
    # forward=recieve.get('forward')
    # backward=recieve.get('backward')
    # speed=recieve.get('speed')
    # right=recieve.get('right')
    # left=recieve.get('left')

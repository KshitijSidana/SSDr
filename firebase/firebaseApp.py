from firebase import firebase
firebase =firebase.FirebaseApplication('https://python-3ff61.firebaseio.com/')
speed=255
def forward(speed):
	firebase.patch('/movement',{"forward":1,"backward":0,"left":0,"right":0,"speed":speed})

def backward(speed):
	firebase.patch('/movement',{"forward":0,"backward":1,"left":0,"right":0,"speed":speed})

def left(speed):
	firebase.patch('/movement',{"forward":1,"backward":0,"left":1,"right":0,"speed":speed})

def right(speed):
    firebase.patch('/movement',{"forward":1,"backward":0,"left":0,"right":1,"speed":speed})





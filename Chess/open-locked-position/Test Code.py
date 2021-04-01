import tensorflow as tf
import numpy as np
import chess
import time

#Loading the saved model
model=tf.keras.models.load_model('FullModel')

#Creating a probability model to make predictions from the imported model
probmodel=tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

#All the conversions from fen into tensorflow readable data
PieceNum={'p':'0','n':'1','b':'2','r':'3','q':'4','k':'5','.':'6'}

def numreprgen(repres):
    splted=[repres[0:8],repres[8:16],repres[16:24],repres[24:32],repres[32:40],repres[40:48],repres[48:56],repres[56:64]]  
    numsplted=[]
    for j in splted:
        toappend=[]
        for k in j:
            toappend.append([PieceNum[k.lower()]])
        numsplted.append(toappend)
    for j in range(len(numsplted)):
        for k in range(8):
            numsplted[j][k][0]=int(numsplted[j][k][0])/6.0
    return numsplted
def reprgener(fen):
    brd=chess.Board()
    brd.set_fen(fen)
    bb=chess.BaseBoard()
    bb.set_board_fen(brd.board_fen())
    pcmap=bb.piece_map()
    repres=[]
    for i in range(64):
        if i in pcmap:
            repres.append(pcmap[i].symbol())
        else:
            repres.append('.')
    strrepres=''.join([elem for elem in repres])
    return strrepres

#Gettng the input fen
testfen=input('fen of the position to be tested ')

#Making the prediction
probs=probmodel(np.array([numreprgen(reprgener(testfen))]))

#Printing the result
print(np.argmax(probs[0]))
print('0 means fully open while 4 means fully locked. 2 means semi-locked. 1 and 3 can also come as results. Terminating code in 30 seconds.')
time.sleep(30)
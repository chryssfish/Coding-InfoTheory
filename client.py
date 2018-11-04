from sage.all import *
import socket
import pickle

def gencode(codeparams):
    golayCode = codes.GolayCode(GF(codeparams['size']), codeparams['extended'])
    return golayCode

def generateRandomWords(code, error):
    channel =  channels.StaticErrorRateChannel(C.ambient_space(), error)
    randomWords = []
    for i in range(20):
        randomWord = code.random_element() #dhmioyrghse tyxaia le3h
        print i, '. ', randomWord
        randomWord = channel.transmit(randomWord) #pros8ese la8os
        randomWords.append(randomWord)
    return randomWords

def send(codeparams, words):
    HOST = 'localhost'    # The remote server
    PORT = 50008              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((HOST, PORT)) #syndesoy sto server
    s.sendall(pickle.dumps({'codeparams' : codeparams, 'words' : words})) #steile perityligmena ta dedomena
    s.close() #kleise th syndesh
    print 'Ta words stal8hkan!'

    
#diabasma size
size = input("Dwste size gia to Golay Code (2-3): ")
while size != 2 and size != 3:
    size = input("Exete kanei la8os.\nDwste size gia to Golay Code (2-3): ")

#diabasma extended
extended = input("Einai to Golay Code extended; Dwste 1 ean einai, 0 ean oxi: ")
while extended != 0 and extended != 1:
    extended = input("Exete kanei la8os.\nEinai to Golay Code extended; Dwste 1 ean einai, 0 ean oxi: ")
if extended == 1:
    extended = True
else:
    extended = False
    
codeparams = {'size' : size, 'extended' : extended}    
C = gencode(codeparams)

print 'O kwdikas exei elaxisth apostash: ', C.minimum_distance()
print 'Epomenws to megisto plh8os lathwn poy mporei na diorthwsei einai: ', (C.minimum_distance() - 1) / 2
#diabasma error
error = input("Dwste tyxaio sfalma baroys: ")

if C is not None:
    if C.dual_code() is not None:
        C = C.dual_code()
    words2send = generateRandomWords(C, error)
    send(codeparams, words2send)
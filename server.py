import socket
from sage.all import *
import pickle

def gencode(codeparams):
    golayCode = codes.GolayCode(GF(codeparams['size']), codeparams['extended'])
    return golayCode

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1:
    print 'Waiting for connection ...'
    print 'Press Ctrl+C to kill'
    conn, addr = s.accept() #egine syndesh
    print 'Connected by', addr
    
    data = conn.recv(1024 * 1024) #lhpsh dedomenwn
    
    data = pickle.loads(data) #3etyli3e ta dedomena
    codeparams = data['codeparams'] #pare ta codeparams
    C = gencode(codeparams) #ftia3e ton kwdika symfwna me ta codeparams
    words = data['words'] # pare tis le3eis poy esteile o client
    i = 0
    for word in words:
        print i, '. ', C.decode_to_code(word) #apokwdikopoihse th le3h
        i += 1
    print 'ta words elhf8hsan!\n'
    conn.close() #kleise th syndesh
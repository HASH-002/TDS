# server.py
import rpyc
import pytz
from datetime import datetime
from rpyc.utils.server import ThreadedServer


@rpyc.service
class TestService(rpyc.Service):
    @rpyc.exposed
    def current_date_and_time(self):
        print('Returning current date and time.')
        current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
        return current_time

print('starting server')
server = ThreadedServer(TestService, port=18852)
server.start()
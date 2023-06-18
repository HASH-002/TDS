import rpyc

class CalculatorService(rpyc.Service):
    def exposed_add(self, x, y):
        return x + y

    def exposed_subtract(self, x, y):
        return x - y

    def exposed_multiply(self, x, y):
        return x * y

    def exposed_divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(CalculatorService, port=18851)
    t.start()
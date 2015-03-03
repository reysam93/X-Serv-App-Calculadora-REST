#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp


class restCalc(webapp.webApp):

    def __init__(self, hostname, port):
        self.operation = None
        webapp.webApp.__init__(self, hostname, port)

    def processGet(self):
        if self.operation is None:
            respond = "<html>No operation introduced</html>"
        else:
            respond = "<html><body><p>" + self.operation + "</p></body></html>"
        return respond

    def processPut(self, ops):
        if ops.find("+") != -1:
            try:
                op1 = float(ops.split("+")[0])
                op2 = float(ops.split("+")[1])
                self.operation = str(op1) + " + " + str(op2) + " = " +\
                            str(op1 + op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operation = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        elif ops.find("-") != -1:
            try:
                op1 = float(ops.split("-")[0])
                op2 = float(ops.split("-")[1])
                self.operation = str(op1) + " - " + str(op2) + " = " +\
                            str(op1 - op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operation = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        elif ops.find("*") != -1:
            try:
                op1 = float(ops.split("*")[0])
                op2 = float(ops.split("*")[1])
                self.operation = str(op1) + " * " + str(op2) + " = " +\
                            str(op1 * op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operation = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        elif ops.find("/") != -1:
            try:
                op1 = float(ops.split("/")[0])
                op2 = float(ops.split("/")[1])
                self.operation = str(op1) + " / " + str(op2) + " = " +\
                            str(op1 / op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operation = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        else:
            self.operation = None
        return code, respond

    def parse(self, request):
        print request
        parsedRequest = [request.split()[0], request.split()[-1]]
        return parsedRequest

    def process(self, request):
        if request[0] == "GET":
            code = "200 OK"
            respond = self.processGet()
        elif request[0] == "PUT":
            (code, respond) = self.processPut(request[1])
        else:
            code = "400 Error" 
            respond = "<html><h1>WRONG REQUEST</h1></html>"
        return (code, respond)

if __name__ == "__main__":
    try:
        calculator = restCalc("localhost", 9999)
    except KeyboardInterrupt:
        print "keyboard interrupt detected"

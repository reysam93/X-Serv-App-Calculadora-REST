#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp


class restCalc(webapp.webApp):

    def __init__(self, hostname, port):
        self.operations = {}
        self.ids = 0
        webapp.webApp.__init__(self, hostname, port)

    def processGet(self, resource):
        resource = resource[1:]
        if resource in self.operations:
            operation = self.operations[resource]
            code = "200 OK"
            if operation is None:
                respond = "<html>No operation introduced</html>"
            else:
                respond = "<html><body><p>" + operation + \
                            "</p></body></html>"
        else:
            self.ids += 1
            id = str(self.ids)
            self.operations[id] = None
            print "añadido", id
            code = "200 OK"
            respond = "<html><body><a href=" + id +">Tu operacion</a>\
                        </body></html>"
        return code, respond

    def processPut(self, body, id):
        id = id[1:]
        print "PROCESS PUT ID:", id
        if not id in self.operations:
            return  "400 Error", "<html><body>Wrong ID</body></html>"
        if body.find("+") != -1:
            try:
                op1 = float(body.split("+")[0])
                op2 = float(body.split("+")[1])
                self.operations[id] = str(op1) + " + " + str(op2) + " = " +\
                            str(op1 + op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operations[id] = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        elif body.find("-") != -1:
            try:
                op1 = float(body.split("-")[0])
                op2 = float(body.split("-")[1])
                self.operations[id] = str(op1) + " - " + str(op2) + " = " +\
                            str(op1 - op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operations[id] = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        elif body.find("*") != -1:
            try:
                op1 = float(body.split("*")[0])
                op2 = float(body.split("*")[1])
                self.operations[id] = str(op1) + " * " + str(op2) + " = " +\
                            str(op1 * op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                self.operations[id] = None
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        elif body.find("/") != -1:
            try:
                op1 = float(body.split("/")[0])
                op2 = float(body.split("/")[1])
                self.operations[id] = str(op1) + " / " + str(op2) + " = " +\
                            str(op1 / op2)
                code = "200 OK"
                respond = ""
            except ValueError:
                code = "400 Error"
                respond = "<html><body>Only numbers</body></html>"
        else:
            self.operation = None
            code = "400"
            respond = "<html><body>wrong operation</body></html>"
        return code, respond

    def parse(self, request):
        print request
        method = request.split()[0]
        resource = request.split()[1]
        if method == "PUT":
            body = request.split()[-1]
        else:
            body = ""
        return (method, resource, body)

    def process(self, request):
        (method, resource, body) = request
        if method == "GET":
            code, respond = self.processGet(resource)
        elif request[0] == "PUT":
            (code, respond) = self.processPut(body, resource)
        else:
            code = "400 Error" 
            respond = "<html><h1>WRONG REQUEST</h1></html>"
        return (code, respond)

if __name__ == "__main__":
    try:
        calculator = restCalc("localhost", 9999)
    except KeyboardInterrupt:
        print "keyboard interrupt detected"

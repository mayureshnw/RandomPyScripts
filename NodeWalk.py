#!/usr/bin/python

import ast, sys

class Visitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print "Node Name: ", type(node).__name__
        print "Full Dump:", ast.dump(node)
        ast.NodeVisitor.generic_visit(self, node)

x = Visitor()
code = open(sys.argv[1]).read()
x.visit(ast.parse(code))
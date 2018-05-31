############################
## Author: Caroline Cocca
## Date: 5-31-18
## Module: Network Analysis
## Title: Version0NA.py
############################

class Node:
    def __init__(self, label, size):
        self.label = label
        self.size = size

    def print_summary(self):
        print('Node', self.label, 'has the size', self.size)

def main():
    tester = Node('Umar', 4)
    tester.print_summary()

main()

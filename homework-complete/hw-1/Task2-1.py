import os
"""
Class Laptop create for aggregation. If i destroy Laptop instance, 
OperationSystem instance still exists.
"""


class Laptop:
    def __init__(self, operation_system):
        self.operation_system = operation_system

    def chek_memory(self):
        print(self.operation_system)


class OperationSystem:
    def __init__(self):
        pass

    @staticmethod
    def get_data_information():
        os.system('ls -ls')

    @staticmethod
    def get_name_of_computer():
        os.system('whoami')


if __name__ == '__main__':
    linux = OperationSystem()
    linux.get_data_information()
    linux.get_name_of_computer()
    dell = Laptop(linux)
    dell.chek_memory()

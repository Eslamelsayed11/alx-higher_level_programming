import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
list = ['hello', 'World']
lib.print_python_list_info(list)
del list[1]
lib.print_python_list_info(list)
list = list + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(list)
list = []
lib.print_python_list_info(list)
list.append(0)
lib.print_python_list_info(list)
list.append(1)
list.append(2)
list.append(3)
list.append(4)
lib.print_python_list_info(list)
list.pop()
lib.print_python_list_info(list)

#!/usr/bin/python3
"""Module that defines list_division"""


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists, returns a new list"""
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list

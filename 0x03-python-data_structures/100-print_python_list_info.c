#include <stdio.h>
#include <stdlib.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PuObject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	printf("[*] Size of the Python List = %d\n", Py_SIZE(p);
	printf("[*] Allocated = %d\n", Py_SIZE(p);
}

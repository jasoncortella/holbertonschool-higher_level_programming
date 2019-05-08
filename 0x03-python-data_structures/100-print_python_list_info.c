#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to PyObject struct
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int i, listlen = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", listlen);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < listlen; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

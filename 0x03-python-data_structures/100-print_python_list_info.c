#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyObject *py_item;
	unsigned long int len = 0, i;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < len; i++)
	{
		py_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(py_item)->tp_name);
	}
}

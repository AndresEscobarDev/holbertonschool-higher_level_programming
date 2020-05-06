#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyObject *py_item;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", (PyListObject *)p->allocated)
	for (i = 0; i < size; i++)
	{
		py_item = PyList_GetItem(p, i)
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

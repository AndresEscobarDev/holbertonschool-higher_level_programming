#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	char *s = NULL;
	long int len = 0, i;  

	printf("[.] bytes object info\n");
	if(!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &s, &len);
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", s);
	if (len < 10)
		printf("  first %ld bytes:", len + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= len && i < 10; i++)
		printf(" %02hhx", s[i]);
	printf("\n");
}
void print_python_list(PyObject *p)
{
	long int len = 0, i;
	PyListObject *py_item = (PyListObject *)p;
	const char *type;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", py_item->allocated);
	for (i = 0; i < len; i++)
	{
		type = (py_item->ob_item[i])->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(py_item->ob_item[i]);
	}
}

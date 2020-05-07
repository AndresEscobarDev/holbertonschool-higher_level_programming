#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	PyObject *py_item;
	unsigned long int len = 0, i;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < len; i++)
	{
		py_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(py_item)->tp_name);
	}
}
void print_python_bytes(PyObject *p)
{
	char *s = NULL;
	unsigned long int len = 0, i;  

	printf("[.] bytes object info\n");
	if(!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = PyBytes_AS_STRING(p);
	len = PyBytes_GET_SIZE(p);
	printf("  trying string: %s\n", s);
	printf("  size: %ld\n", len);
	if (len < 10)
		printf("  first %ld bytes:", len + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= len && i < 10; i++)
		printf(" %02hhx", s[i]);
	printf("\n");
}

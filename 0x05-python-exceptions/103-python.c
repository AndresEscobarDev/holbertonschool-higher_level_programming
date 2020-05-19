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
	s = ((PyBytesObject *)p)->ob_sval;
	len = ((PyVarObject *)p)->ob_size;
	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", s);
	if (len < 10)
		printf("  first %ld bytes:", len + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= len && i < 10; i++)
		printf(" %02hhx", s[i]);
	printf("\n");
	fflush(stdout);
}

void print_python_float(PyObject *p)
{
	double num = 0;

	printf("[.] float object info\n");
	if(!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	num = ((PyFloatObject *)p)->ob_fval;
	if (num - (int)num == 0)
		printf("  value: %.1f\n", num);
	else
		printf("  value: %.16g\n", num);
	fflush(stdout);
}

void print_python_list(PyObject *p)
{
	long int len = 0, i;
	PyListObject *py_item = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	if(!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	len = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", py_item->allocated);
	for (i = 0; i < len; i++)
	{
		type = (py_item->ob_item[i])->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(py_item->ob_item[i]);
		if (!strcmp(type, "float"))
			print_python_float(py_item->ob_item[i]);
	}
	fflush(stdout);
}
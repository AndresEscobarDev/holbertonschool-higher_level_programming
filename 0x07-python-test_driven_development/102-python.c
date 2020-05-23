#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    wchar_t *str;
    int type;

    printf("[.] string object info\n");
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    len = ((PyASCIIObject *)p)->length;
    str = PyUnicode_AsWideCharString(p, &len);
    type = PyUnicode_IS_COMPACT_ASCII(p);
    if(type == 0)
        printf("  type: compact unicode object\n");
    else
        printf("  type: compact ascii\n");
    printf("  length: %lu\n", len);
    printf("  value: %ls\n", str);
}

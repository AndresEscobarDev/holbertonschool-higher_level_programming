#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    unsigned long int size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated)
    for (i = 0; i < size; i++)
    {
        list = (PyList_GET_ITEM(p, i))->ob_item[i]->tp_name;
        printf("Element %d: %s\n", i, list);
    }
    
}
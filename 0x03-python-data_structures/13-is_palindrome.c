#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - Function that evaluates if a linked list is palindrome or not
 * 
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = NULL;
    int i, j;
    char *s = NULL;

    if (!current)
        return (1);
    current = *head;
    for (i = 0; current; i++)
        current = current->next;
    current = *head;
    s = malloc(sizeof(char) * (i + 1));
    for (i = 0; current; i++)
    {
        s[i] = current->n;
        current = current->next;
    }
    for (j = 0, i--; i > j; i--, j++)
    {
        if (s[i] != s[j])
        {
            free(s);
            return (0);
        }
    }
    return (1);
}
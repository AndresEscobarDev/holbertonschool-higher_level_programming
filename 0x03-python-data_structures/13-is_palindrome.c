#include "lists.h"
/**
 * is_palindrome - Function that evaluates if a linked
 * list is palindrome or not
 * @head: header of a linked list
 * Return: 1 if is palidrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int i, j;
	int *s = NULL;

	if (!*head)
		return (1);
	current = *head;
	for (i = 0; current; i++)
		current = current->next;
	current = *head;
	s = malloc(sizeof(int) * (i));
	for (i = 0; current; i++)
	{
		s[i] = current->n;
		current = current->next;
	}
	for (j = 0, i--; i > j; i--, j++)
	{
		if (s[i] != s[j])
		{

			return (0);
		}
	}

	return (1);
}

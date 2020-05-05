#include "lists.h"
/**
 * is_palindrome - Function that evaluates if a linked
 * list is palindrome or not
 * @head: header of a linked list
 * Return: 1 if is palidrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL, *end = NULL;
	int i, j;

	if (!*head)
		return (1);
	current = *head;
	for (i = 0; current; i++)
		current = current->next;
	current = *head;
	for (j = 0, i--; current; i++)
	{
		end = current;
		for (j = 0; j < i; j++)
			end = end->next;
		if (end->n != current->n)
			return (0);
		i -= 3;
		current = current->next;
	}
	return (1);
}

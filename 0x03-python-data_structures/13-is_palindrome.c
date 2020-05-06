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
	int i = 0, j = 0;
	int s[100];

	if (!*head || !head[0]->next)
		return (1);
	current = *head;
	while (current)
		current = current->next, i++;
	current = *head;
	while (current)
		s[j++] = current->n, current = current->next;
	i = 0;
	j--;
	while (i < j)
		if (s[i++] != s[j--])
			return (0);
	return (1);

}

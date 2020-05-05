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
	int i = 0, j;
	int *s = NULL;

	if (!*head || !(*head)->next)
		return (1);
	current = *head;
	while (current)
		current = current->next, i++;
	current = *head;
	s = malloc(sizeof(int) * (i));
	i = 0;
	while (current)
	{
		s[i++] = current->n;
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
	free(s);
	return (1);
}

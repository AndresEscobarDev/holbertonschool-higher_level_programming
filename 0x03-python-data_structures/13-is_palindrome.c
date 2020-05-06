#include "lists.h"
/**
 * be_or_not_be - Function that evaluates if a linked
 * list is palindrome or not
 * @head: header of a linked list
 * Return: 1 if is palidrome 0 if not
 */
int be_or_not_be(int i, listint_t *head)
{
	int s[i], j = 0;

	while (head)
	{
		s[j++] = head->n;
		head = head->next;
	}
	i = 0;
	j--;
	while (i < j)
	{

		if (s[i++] != s[j--])
			return (0);
	}
	return (1);
}
/**
 * is_palindrome - Function that evaluates if a linked
 * list is palindrome or not
 * @head: header of a linked list
 * Return: 1 if is palidrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int i = 0;

	if (!*head || !head[0]->next)
		return (1);
	current = *head;
	while (current)
		current = current->next, i++;
	return (be_or_not_be(i, *head));
}

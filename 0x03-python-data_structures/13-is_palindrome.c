#include "lists.h"
/**
 * reverse_listint - function that reverses a listint_t linked list.
 * @head: Head of the listint.
 * Return: pointer to the first node.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *h1, *h2 = 0;

	while (*head)
	{
		h1 = (*head)->next;
		(*head)->next = h2;
		h2 = *head;
		*head = h1;
	}
	*head = h2;
	return (*head);
}
/**
 * is_palindrome - Function that evaluates if a linked
 * list is palindrome or not
 * @head: header of a linked list
 * Return: 1 if is palidrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL, *middle = NULL;

	if (!*head || !head[0]->next)
		return (1);
	middle = current = *head;
	while (1)
	{
		current = current->next->next;
		if (!current)
		{
			middle = middle->next;
			break;
		}
		if (!current->next)
		{
			middle = middle->next->next;
			break;
		}
		middle = middle->next;
	}
	reverse_listint(&middle);
	current = *head;
	while (middle)
	{
		if (middle->n != current->n)
			return (0);
		middle = middle->next;
		current = current->next;
	}
	return (1);
}

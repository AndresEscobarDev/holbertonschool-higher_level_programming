#include "lists.h"
/**
 * add_nodeint - adds a new node at the beginning of a listint_t list.
 * @head: Head of the listint.
 * @n: new element.
 * Return: A pointer to the new element.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
 * is_palindrome - Function that evaluates if a linked
 * list is palindrome or not
 * @head: header of a linked list
 * Return: 1 if is palidrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL, *new = NULL;

	if (!*head || !head[0]->next)
		return (1);
	current = *head;
	while (current)
	{
		new = add_nodeint(&new, current->n);
		current = current->next;
	}
	current = *head;
	while (current)
	{
		if (current->n != new->n)
		{
			free_listint(new);
			return (0);
		}
		current = current->next;
		new = new->next;
	}
	return (1);
}

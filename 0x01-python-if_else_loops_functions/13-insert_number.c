#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Insert a sort node
 * @head: head of linked list
 * @number: number of the new member of the linked list
 * Return: The new address of the new member of the linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (current->n > number)
	{
		new->n = number;
		new->next = current;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->next->n > number)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}

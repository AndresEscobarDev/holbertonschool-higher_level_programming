#include "lists.h"
/**
 * check_cycle - Check if a list have a cycle.
 * @list: Linked list to check.
 * Return: 1 if have a cycle and 0 if doesn't.
 */
int check_cycle(listint_t *list)
{
	listint_t *o, *n;

	for (o = list, n = list; n && n->next;)
	{
		o = o->next;
		n = n->next->next;
		if (o == n)
		return (1);
	}
	return (0);
}

#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *p = list;
	listint_t *q = list;

	while (p && q && q->next)
	{
		p = p->next;
		q = q->next->next;
		if (p == q)
			return (1);
	}
	return (0);
}

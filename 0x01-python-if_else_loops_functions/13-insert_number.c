#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted
 *		singly linked list
 * @head: head of the list
 * @number: number to insert
 * Return: adress of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr1, *curr2, *tmp;

	tmp = malloc(sizeof(listint_t));
	if (!tmp)
		return (NULL);
	tmp->n = number;
	tmp->next = NULL;
	if ((*head) == NULL)
	{
		*head = tmp;
		return (tmp);
	}
	if ((*head)->n > number)
	{
		tmp->next = *head;
		(*head) = tmp;
		return (tmp);
	}
	curr1 = *head;
	curr2 = (*head)->next;
	while (curr2)
	{
		if (curr2->n > number)
		{
			tmp->next = curr2;
			curr1->next = tmp;
			return (tmp);
		}
		curr1 = curr1->next;
		curr2 = curr2->next;
	}
	curr1->next = tmp;
	return (tmp);
}

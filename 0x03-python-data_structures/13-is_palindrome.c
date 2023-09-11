#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - function that checks if a list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *start, *curr = *head;
	int i, l, flag = 0, len = 0;
	int *tmp;

	while (curr)
	{
		curr = curr->next;
		len++;
	}
	if (len % 2 == 0)
		l = len / 2;
	else
		l = len / 2, flag = 1;
	tmp = malloc(sizeof(int) * (l + 1));
	if (!tmp)
		return (-1);
	start = *head;
	for (i = 0; i < l; i++)
	{
		tmp[i] = start->n;
		start = start->next;
	}
	tmp[i] = '\0';
	if (flag == 1)
		start = start->next;
	for (i = l - 1; i >= 0; i--)
	{
		if (tmp[i] != start->n)
		{
			free(tmp);
			return (0);
		}
		start = start->next;
	}
	free(tmp);
	return (1);
}

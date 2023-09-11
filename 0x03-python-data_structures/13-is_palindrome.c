#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - function that checks if a list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *start, *curr = *head;
	int i, j, len = 0;
	char *tmp;

	while (curr)
	{
		curr = curr->next;
		len++;
	}
	tmp = malloc(sizeof(char) * (len + 1));
	if (!tmp)
		return (-1);
	start = *head;
	for (i = 0; i < len; i++)
	{
		tmp[i] = start->n;
		start = start->next;
	}
	tmp[i] = '\0';
	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		if (tmp[i] != tmp[j])
		{
			free(tmp);
			return (0);
		}
	}
	free(tmp);
	return (1);
}

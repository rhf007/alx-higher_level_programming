#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Check if linked list has a cycle
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	const listint_t *current;
	const listint_t *h_ptr;

	current = list;
	h_ptr = list;

	while (current != NULL)
	{
		current = current->next;
		if (current == h_ptr)
		{
			return (1);
		}
	}

	return (0);
}

#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: A singly linked list
 *
 * Return: 1 if a cycle does exist or 0 if it is not found
 */

int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *prev;

	p2 = list;
	prev = list;
	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;

		if (list == p2)
		{
			list = prev;
			prev =  p2;
			while (1)
			{
				p2 = prev;
				while (p2->next != list && p2->next != prev)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}

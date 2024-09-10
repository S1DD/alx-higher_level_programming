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
	listint_t *truck, *bugatti;

	if (list == NULL || list->next == NULL)
		return (0);

	truck = list->next;
	bugatti = list->next->next;

	while (truck && bugatti && bugatti->next)
	{
		if (truck == bugatti)
			return (1);

		truck = truck->next;
		bugatti = bugatti->next->next;
	}
	return (0);
}

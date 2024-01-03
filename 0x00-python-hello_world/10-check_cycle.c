#include "lists.h"

/**
 * check_cycle - check linked-list for cycle
 * @list: the linked-list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *step = list, *jump = list;

	while (jump && jump->next)
	{
		step = step->next;
		jump = jump->next->next;

		if (step == jump)
			return (1);
	}
	return (0);
}

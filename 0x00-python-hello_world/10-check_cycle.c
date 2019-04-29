#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop
 * @list: the linked list to check
 * Return: 0 - the linked list has no loop.
 *         1 - the linked list has a loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *snail, *cheetah;

	snail = cheetah = list;
	while (snail && cheetah && cheetah->next )
	{
		snail = snail->next;
		cheetah = cheetah->next->next;
		if (snail == cheetah)
			return (1);
	}
	return (0);
}

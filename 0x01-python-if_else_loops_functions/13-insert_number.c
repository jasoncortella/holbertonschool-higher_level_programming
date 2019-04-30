#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linekd list
 * @head: the linked list to insert the number into
 * @number: the number to insert into the linked list
 * Return: the address of the new node OR
 *         NULL upon failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!current)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	while (current->next && number > current->next->n)
		current = current->next;
	if (current == *head && number <= current->n)
		/* number < initial element, insert at front */
	{
		new->next = current;
		*head = new;
	}
	else
	{
		new->next = current->next;
		current->next = new;
	}
	return (new);
}

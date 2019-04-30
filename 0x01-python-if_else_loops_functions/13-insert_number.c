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

	if (!head)
		return (NULL);
	while (number > current->next->n)
		current = current->next;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = current->next;
	current->next = new;

	return (new);
}

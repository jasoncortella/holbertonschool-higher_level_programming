#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head of the linked list to be checked
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *array, i, len;

	if (!current || !current->next)
		return (1);
	len = listlen(*head);
	array = malloc(sizeof(int) * len);
	if (!array)
		return (0);
	for (i = len - 1; i >= 0; i--)
	{
		array[i] = current->n;
		current = current->next;
	}
	current = *head;
        for (i = 0; current; i++)
	{
		if (current->n == array[i])
			current = current ->next;
		else
			return (0);
	}
	return (1);
}

/**
 *listlen - returns the length of a linked list
 *@h: the list to check
 *Return: the length of the list
 */

int listlen(listint_t *h)
{
	int count = 0;
	listint_t *current = h;

	if (h == NULL)
		return (0);
	while (current)
	{
		count++;
		current = current->next;
	}
	return (count);
}

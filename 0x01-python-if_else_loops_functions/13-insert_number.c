#include "lists.h"
/**
 * insert_node-function in C that inserts a number
 * into a sorted singly linked list
 * @head: pointer to a pointer to the head
 * @number: number to be inserted
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *_recent;

	_recent = malloc(sizeof(listint_t));
	if (_recent == NULL)
		return (NULL);
	_recent->n = number;
	if (ptr == NULL || ptr->n >= number)
	{
		_recent->next = ptr;
		*head = _recent;
		return (_recent);
	}
	while (ptr && ptr->next && ptr->next->n < number)
	{
		ptr = ptr->next;
	}
	_recent->next = ptr->next;
	ptr->next = _recent;
	return (_recent);
}

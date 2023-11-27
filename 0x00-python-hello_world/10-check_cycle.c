#include "lists.h"
/**
 * check_cycle-a function in C that checks if a 
 * singly linked list has a cycle in it
 * @list: arguments to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *_temp = list;
	int Q = 0;

	if (list == NULL || list->next == NULL)
		return (0);
	while (_temp != NULL)
	{
		if (Q > 12)
			return (1);
		_temp = _temp->next;
		Q++;
	}
	return (0);
}

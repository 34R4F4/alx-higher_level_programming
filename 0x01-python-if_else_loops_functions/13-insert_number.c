#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function to insert value in order of linked-list
 * @number: the value to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *node_ptr = *head;

	if(!new_node)
		return(NULL);

	new_node->n = number;
	new_node->next = NULL;

	if(new_node->n < node_ptr->n || !head)
	{
		new_node->next = node_ptr;
		return(*head = new_node);
	}

	while(node_ptr)
	{
		if(new_node->n < node_ptr->next->n || !node_ptr->next)
		{
			new_node->next = node_ptr->next;
			node_ptr->next = new_node;
			return(node_ptr);
		}
		node_ptr = node_ptr->next;
	}
	return(NULL);
	
}

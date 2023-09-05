#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: double pointer to the head
 * @number: number to be stored in the node
 * 
 * Returns: address of the new added node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{

  listint_t *new_node;
  listint_t *prev;
  listint_t *nex;


  if (*head == NULL)
    return (NULL);
  
  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
    return (NULL);

  
  prev = *head;
  nex = prev->next;

  if (number <= prev->n)
    {
      new_node->n = number;
      new_node->next = *head;
      return (new_node);
    }

  while (nex)
    {
      if (number >= prev->n && number <= nex->n)
	{
	  new_node->n = number;
	  new_node->next = nex;
	  prev->next = new_node;

	  return (new_node);
	}
      prev = prev->next;
      nex = nex->next;
    }

  prev->next = new_node;
  return (new_node);
}

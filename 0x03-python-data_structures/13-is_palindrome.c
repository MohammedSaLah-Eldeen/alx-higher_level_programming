#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/*
* is_palindrome - function to know if the singly linked list is palindrome.
*
* @head: a double pointer to the starting node.
* 
* Returns: 1 if palindrome or 0 if it isn't
*/
int is_palindrome(listint_t **head)
{
  listint_t *front, *back, *tmp;
  int n_nodes;
  int it;
  int front_go;
  int back_go;

  if (*head == NULL)
    return (1);

  tmp = *head;
  for (n_nodes = 1; tmp->next != NULL; n_nodes++)
    tmp = tmp->next;

  if (n_nodes == 1)
    return (1);

  it = n_nodes / 2;
  front_go = 1;

  front = *head;
  while (front_go <= it)
    {
      back_go = n_nodes - front_go;
      back = *head;
      for (; back_go >= 1; back_go--)
	  back = back->next;

      if (front->n != back->n)
	return (0);

      front = front->next;
      front_go++;
      	
    }

  return (1);
  
}

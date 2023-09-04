#include "lists.h"


/**
* check_cycle - checks if a singly linked list has a loop or not
* @list: head of the list
*
* Return: 0 if not 1 if yes
*/
int check_cycle(listint_t *list)
{
listint_t *fast = list;
listint_t *slow = list;

while (fast)
{
fast = fast->next->next;
slow = slow->next;

if (fast == slow)
return (1);
}
return (0);
}

#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *p = *head,*q,*new_nead;
new_nead = malloc(sizeof(listint_t));
	new_nead->n = number;

	if (*head == NULL)
	{
		new_nead->next = *head;
                 *head = new_nead;
		return new_nead;
	}	
	
	q = p->next;
	if (p->n >number)
	{
		new_nead->next = p;
                 *head = new_nead;
		 return new_nead;
	}
	while (q != NULL)
	{ 
          if (q->n > number)
	  {
		  new_nead->next = q;
                    p->next = new_nead;
		    return new_nead;
	  }
          p = q;
	  q = p->next;

	}
	 new_nead->next = q;
	    p->next = new_nead;
         return new_nead;

}

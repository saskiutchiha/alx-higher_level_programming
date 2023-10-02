#include <stddef.h>
#include "lists.h"
int check_cycle(listint_t *list){
  listint_t *q = list->next;
  while(q != list)
{
    if (q == NULL)
   {
  return 0;
   }
   q = q->next;
}
return 1;

#include<stddef.h>
#include "lists.h"
#include<stdlib.h>
int is_palindrome(listint_t **head) {
        int *tab;
        listint_t *q = *head;
        int a=0;
         if (*head == NULL)
         {
                   return 1;
         }
         while (q != NULL)
         {
                 a++;
                 q = q->next;
         }
         q= *head;
          tab = malloc(a*sizeof(int));
          a=0;
          while (q != NULL)
          {
                  *(tab+a) = q->n;
                  a++;
                  q = q->next;
          }
          a--;
          while(tab < tab+a){
                  if(*(tab) != *(tab +a)){
                           return 0;
                  }
                   tab++;
                    a=a-2;

          }
          return 1;
}
~                          

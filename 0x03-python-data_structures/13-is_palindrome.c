#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid = NULL;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        /* Find the middle of the list and reverse the second half */
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;

            /* We need to keep track of the middle element for odd-length lists */
            prev_slow = slow;
            slow = slow->next;
        }

        /* If the list has odd length, the middle element belongs to both halves */
        if (fast != NULL)
        {
            mid = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_slow->next = NULL;
        reverse_list(&second_half);

        is_palindrome = compare_lists(*head, second_half);

        /* Restore the list */
        reverse_list(&second_half);
        if (mid != NULL)
        {
            prev_slow->next = mid;
            mid->next = second_half;
        }
        else
        {
            prev_slow->next = second_half;
        }
    }

    return is_palindrome;
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to pointer to head of list
 * Return: void
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two singly linked lists
 * @list1: pointer to head of first list
 * @list2: pointer to head of second list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;

        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}


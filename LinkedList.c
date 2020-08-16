#include <stdio.h>
#define NULL '\0'
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;

} node;

struct Node *head=NULL, *tail=NULL;

struct Node* createNode(int data)
{
    struct Node* temp;
    temp=(struct Node*)malloc(sizeof(struct Node));
    temp->next=NULL;
    (*temp).data=data;
    return temp;
};
void insert(int data)
{
    struct Node* item= createNode(data);
    if(head==NULL)
    {
        head=item;
        tail=item;
    }
    else
    {
        tail->next=item;
        tail=item;
    }

}

void display()
{
    node* temp=head;
    while(temp!=NULL)
    {
        printf("%d-->",temp->data);
        temp=temp->next;
    }
}
void main()
{
    int num,data;
    printf("Enter number of terms you wanna add : ");
    scanf("%d",&num);
    while(num--)
    {
        printf("\n Enter value: ");
        scanf("%d",&data);
        insert(data);
    }
    printf("\nThe elements of linked list are\n");
    display();
}

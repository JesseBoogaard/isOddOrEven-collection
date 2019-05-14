#include <stdio.h>
#include <stdlib.h>



// this algorithm checks whether or not the number is even using a stack
// you can further improve this algorithm by implementing a queue using 
// 2 stacks and then using 2 of these queues to make a stack (TODO)


// stack stuff
typedef struct element{
    int value;
    struct element* under;
} Element;

typedef struct stack{
    Element* top;
} Stack;

Stack* init();
void push(Stack* s, int element);
void pop(Stack* s);
int peek(Stack* s);
int isEmpty(Stack* s);


// main logic
int isEven(int num)
{
    int i, result;
    Stack *stack1 = init(), *stack2 = init();
    // handling negative numbers
    if(num < 0)
        num *= -1;

    for(i = 0; i < num; i++)
    {
        if(i % 2 == 0)
            push(stack1, i);
        else if(i % 2 == 1)
            push(stack2, i);
        else
            return 5; // because im so random xD
    }
    while(!isEmpty(stack1) && !isEmpty(stack2))
    {
        pop(stack1);
        pop(stack2);
    }

    result = isEmpty(stack1) && isEmpty(stack2);

    if(!isEmpty(stack1))
        pop(stack1);
    if(!isEmpty(stack2))
        pop(stack2);
    free(stack1);
    free(stack2);

    return result;
}


int main()
{
    int hmm;
    scanf("%d", &hmm);
    printf("%s", isEven(hmm) ? "even" : "odd");    
}


Stack* init()
{
    Stack* s = (Stack*) malloc(sizeof(Stack));
    if (s == NULL)
        exit(EXIT_FAILURE);
    s->top = NULL;
    return s;
}
void push(Stack* s, int element)
{
    Element* e = (Element*) malloc(sizeof(Element));
    if (e == NULL)
        exit(EXIT_FAILURE);
    e->value = element;
    e->under = s->top;
    s->top = e;
}

void pop(Stack* s)
{
    if(isEmpty(s))
        exit(EXIT_FAILURE);
    Element* toRemove = s->top;
    s->top = s->top->under;
    free(toRemove);
}

int peek(Stack* s)
{
    if(isEmpty(s))
        exit(EXIT_FAILURE);
    return s->top->value;
}
int isEmpty(Stack* s)
{
    return s->top == NULL;
}
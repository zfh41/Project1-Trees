#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Node {
    int val;
    struct Node *left, *right;
    int height;
    struct Node *parent;
};



int height(Node *lol)
{
    if(lol == NULL)
        return 0;
    return lol->height;
}

int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

struct Node *newNode(int val)
{
    Node* temp;
    temp = new Node;
    temp->val=val;
    temp->left=NULL;
    temp->right=NULL;
    temp->height=1;
    temp->parent=NULL;
    
    return temp;
}


Node *rightRotate(Node *y)
{
    Node *x=y->left;
    Node *T2=x->right;
    
    x->right=y;
    y->left=T2;
    
    y->height=max(y->left->height,y->right->height)+1;
    x->height=max(x->left->height, x->right->height)+1;
    
    return x;
}

int getBalance(Node *n)
{
    return height(n->left) - height(n->right);
}


Node *leftRotate(Node *x)
{
    Node *y = x->right;
    Node *T2=y->left;
    
    y->left=x;
    x->right=T2;
    
    
    x->height=max(height(x->left), height(x->right))+1;
    
    y->height=max(height(y->left), height(y->right))+1;
    
    return y;
}

Node *insertIter(Node* node, int num)
{
    if (node == NULL)
    {
        struct Node *lol = newNode(num);
        return lol;
    }
    
    return node;
    
//    while (node!=NULL)
//    {
//        if(num < node->val)
//            node=node->left;
//        else
//            node=node->right;
//    }
//
//    if (num < node->val)
//        node->left = newNode(num);
//    else
//        node->right = newNode(num);
    
    
//    node->height = max(height(node->left), height(node->right)) + 1;
//
//    int balance = getBalance(node);
//
//
//    // right rotation
//
//    if (balance > 1 && num < node->left->val)
//        return rightRotate(node);
//    // left rotation
//
//    if ( balance < -1 && num > node->right->val)
//        return leftRotate(node);
//
//    //left/right rotation
//
//    if (balance > 1 && num > node->left->val)
//    {
//        node->left = leftRotate(node->left);
//        return rightRotate(node);
//    }
//
//    //right/left rotation
//
//    if (balance < -1 && num < node->right->val)
//    {
//        node->right = rightRotate(node->right);
//        return leftRotate(node);
//    }
//    return node;
}

//Node *deleteIter(Node *node, int num)
//{
//    if (node == NULL) return node;
//
//
//    while (node!=NULL)
//    {
//        if(num < node->val)
//            node=node->left;
//        else
//            node=node->right;
//    }
//
//
//    if (node->left==NULL && node->right==NULL )
//    {
//        free(node);
//    }
//
//    if (node->left !=NULL)
//    {
//
//        swap(node->left, node);
//        remove(node);
//    }
//    if(node ->right != NULL)
//    {
//        swap(node->right, node);
//        remove(node);
//
//    }
//
//}




int findNextIter(struct Node* root, int elem)
{
    if (root==NULL)
    {
        return 0;
    }
    
    struct Node *curr;
    struct Node *node = root;
    
    while (node!=NULL)
    {
        if(elem < node->val)
            node=node->left;
        else
            node=node->right;
    }
    
    if(node->right!=NULL)
    {
        
        curr = root->right;
        while(curr->left!=NULL)
        {
            curr=curr->left;
        }
        return curr->val;
    }
    
    while (node->parent != NULL)
    {
        node=node->parent;
    }
    return node->val;
    
}

int findPrevIter(struct Node* root, int index)
{
    if (root==NULL)
    {
        return 0;
    }
    
    struct Node* curr;
    curr=root;
    
    if(root->left!=NULL)
    {
        curr = root->left;
        while(root->right!=NULL)
        {
            curr = curr->right;
        }
        return curr->val;
    }
    return 0;
        
}

int findMinIter(struct Node* node) {
  struct Node* current = node;
   
  /* loop down to find the leftmost leaf */
  while (current->left != NULL) {
    current = current->left;
  }
  return current->val;
}

int findMaxIter(struct Node* root)
{
    struct Node* current = root;
    
    while(current->right != NULL)
     {
         current=current->right;
     }
     return current->val;
}

int main()
{
    
    int keys[] = {15, 10, 20, 8, 12, 16, 25};
    Node *shamu = NULL;
    
    insertIter(shamu, 15);
    
    
    
    
}




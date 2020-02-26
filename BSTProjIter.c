#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node* left;
    struct node* right;
    struct node* parent;
};


struct node* newNode(int data)
{
  struct node* node = (struct node*)
                       malloc(sizeof(struct node));
  node->data   = data;
  node->left   = NULL;
  node->right  = NULL;
  node->parent = NULL;
    
  return(node);
}

int findMinIter(struct node* node) {
  struct node* current = node;
   
  /* loop down to find the leftmost leaf */
  while (current->left != NULL) {
    current = current->left;
  }
  return current->data;
}

int findMaxIter(struct node* root)
{
    struct node* current = root;
    
    while(current->right != NULL)
     {
         current=current->right;
     }
     return current->data;
    
}

struct node* insertIter(struct node* root, int val)
{
    struct node* newnode = newNode(val);
    struct node* whoa = root;
  
    struct node* yolo = NULL;
  
    while (whoa != NULL) {
        yolo = whoa;
        if (val < whoa->data)
            whoa = whoa->left;
        else
            whoa = whoa->right;
    }
  
    if (yolo == NULL)
        yolo = newnode;
  

    else if (val < yolo->data)
        yolo->left = newnode;
    else
        yolo->right = newnode;
  
    return yolo;
}

struct node* deleteIter (struct node* root, int data)
{
    if (root == NULL)
        return root;
    while(data<root->data)
    {
        root = root->left;
    }
    while(data>root->data)
    {
        root = root->right;
    }
    
    if(root->left == NULL)
    {
      struct node *temp = root->right;
      free(root);
      return temp;
    }
    else if (root->right == NULL)
    {
      struct node *temp = root->left;
      free(root);
      return temp;
    }
      struct node* temp = findMinIter(root->right);
      return temp;
}

int findNextIter(struct node* root, int elem)
{
    if (root==NULL)
    {
        return NULL;
    }
    
    struct node* curr;
    curr=root;
    
    if(root->right!=NULL)
    {
        
        curr = root->right;
        while(curr->left!=NULL)
        {
            curr=curr->left;
        }
        return curr->data;
    }
    else if(root->parent!=NULL)
    {
        return root->parent->data;
    }
    else
    {
        return NULL;
    }
    
}

int findPrevIter(struct node* root, int index)
{
    if (root==NULL)
    {
        return NULL;
    }
    
    struct node* curr;
    curr=root;
    
    if(root->left!=NULL)
    {
        curr = root->left;
        while(root->right!=NULL)
        {
            curr = curr->right;
        }
        return curr->data;
    }
    return NULL;
        
}
int main()
{
    // input should be here
}


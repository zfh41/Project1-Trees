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

struct node * findMinRec(struct node* node) {
  struct node* current = node;
    
  if (current->left != NULL) {
      return findMinRec(current->left);
  }
  return current;
}

struct node * findMaxRec(struct node* root)
{
    if(root->right != NULL)
    {
        return findMaxRec(root->right);
    }
 
    return root;
}

struct node* insertRec(struct node* node, int data)
{
  if (node == NULL)
    return(newNode(data));
  else
  {
    struct node *temp;
  
    if (data < node->data)
    {
         temp = insertRec(node->left, data);
         node->left  = temp;
         temp->parent= node;
    }
    else
    {
        temp = insertRec(node->right, data);
        node->right = temp;
        temp->parent = node;
    }
    return node;
  }
}

  
struct node *findNextRec(struct node *root, struct node *whoa)
{
  if(root == NULL)
      return NULL;

  struct node *successor = NULL;

  if(root->data >= whoa->data)
  {
      successor = root;
      successor->data = root->data;
  }

  if(root->right !=NULL && whoa->data > root->data)
      return findNextRec(root->right,whoa);

  if(root->left != NULL && whoa->data < root->data)
      return findNextRec(root->left ,whoa);

  return successor;
    
}

//Problem 2c

void sort(struct node* root)
{
    if (root==NULL)
    {
        return;
    }
    else{
        sort(root->left);
        printf("%d ", root->data);
        sort(root->right);
    }
}

struct node* deleteRec (struct node* root, int data)
{
    if (root == NULL)
        return root;
    if(data<root->data)
    {
        root->left=deleteRec(root->left, data);
    }
    else if(data>root->data)
    {
        root->right=deleteRec(root->right, data);
    }
    else
    {
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
      struct node* temp = findMinRec(root->right);
      return temp;
    }
    return root;
}
    
int findPrevRec(struct node* root, int index)
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
         int i;
        while(root->right!=NULL)
        {
            i=findPrevRec(curr->right, index);
        }
        return i;
    }
    return NULL;
        
}
    
int main()
{
   // input can be provided here
}


     




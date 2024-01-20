#include<bits/stdc++.h>
using namespace std;
struct Node
{
    public:
        int data;
        Node* next;
    public:
       Node(int data1){
        data = data1;
        next = NULL;
       }    
        
};
Node* deletehead(Node* head){
    if(head == nullptr) return nullptr;
    Node* temp = head;
    head = head->next;
    delete temp;
    return head;
}
void deletetail(Node* head){
    // if(head == nullptr || head->next == nullptr){
    //     return nullptr;
    // }
    // Node* temp = head;
    // while(temp->next->next != nullptr){
    //     temp = temp->next;

    // }
    // // delete temp->next;
    // temp->next = nullptr;
    // return head;
    if(head == NULL)return;
    if(head->next == NULL){
        head = NULL;
        return;
    }
    Node *temp = head;
    while(temp->next->next != NULL){
        temp= temp->next;
    }
    temp->next = NULL;
}
Node* deleletekthele(Node* head,int k){
    // if(head == nullptr){
    //     return head;
    // }
    // if(k == 1){
    //     Node* temp = head;
    //     head = head->next;
    //     delete temp;
    //     return head;   
    // }
    Node* temp = head;
    Node* prev = NULL;
    int c = 0;
    while(temp!= nullptr){
        c++;
        if( c== k){
            prev->next = prev->next->next;
            free (temp);
            break;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}
Node* deleteNode(Node *head,int x)
{   
    // if(head = NULL){
    //     return head;
        
    // }
    if(x == 1){
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    //Your code heret
    Node* temp = head;
    Node* prev = NULL;
    int c = 0;
    while(temp!=NULL){
        c++;
        if(c == x){
            prev->next = prev->next->next;
            free(temp);
            break;
            
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
    
}
Node* insertattail(Node* head,int x){
    Node* temp = head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    Node* k = new Node(x);
    temp->next = k;
    return head;
}
void Printll(Node *head){
    Node* temp = head;
    while(temp!=NULL){
        cout << temp->data;
        temp = temp->next;
    }
    cout << endl;
}
Node* inserthead(Node *head,int x){
    Node *temp = new Node(x);
    temp->next = head;
    return temp;
}

int main(){
    int n ;
    cin >> n;
    int arr[n];
    for(int i = 0;i<n;i++){
        cin >> arr[i];
    }
    Node* head = new Node(arr[0]);
    Node* mov = head;
    for(int i = 1;i<n;i++){
        Node* temp = new Node(arr[i]);
        mov->next = temp;
        mov = temp;
    }
    Printll(head);
    cout << endl;
    // Node* newhead = deletehead(head);
    // Printll(newhead);
    // Node* temp = head;
    // while(temp != nullptr){
    //     cout<< temp->data;
    //     temp = temp->next;
    // }
    // cout << temp;
    // Node* tail = deletetail(head);
    // Printll(tail);
    // int k;
    // cin >> k;
//    Node* p =deleteNode(head,k);
//    cout << ;
    // Printll(head);
    // int k;
    // cin >> k;
    // Node *app = insertattail(head,k);
    // Printll(app);
    deletetail(head);
    Printll(head);

}
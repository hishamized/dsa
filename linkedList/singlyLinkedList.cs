// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;
public class Node {
    public  int data;
    public Node next;
    public Node(int v){
        this.data = v;
        this.next = null;
    }
}
public class HelloWorld
{

    public static void Main(string[] args)
    {
        Node head = null;
        head = AppendNode(head, 10);
        head = AppendNode(head, 20);
        head = AppendNode(head, 30);
        head = AppendNode(head, 40);
        head = PrependNode(head, 9);
        head = PrependNode(head, 8);
        DisplayList(head);
        
    }
    static void DisplayList(Node head){
        if(head == null){
            Console.WriteLine("The linked list is empty\n");
            return;
        }
        Node temp = head;
        do {
            Console.Write(temp.data);
            temp = temp.next;
            if(temp != null)
                Console.Write("-->");
        }  while(temp != null);
    }
    
    static Node AppendNode(Node head, int data){
        Node n = new Node(data);
        if(head != null){
            Node temp = head;
            while (temp.next != null){
                temp = temp.next;
            }
            temp.next = n;
            n.next = null;
            return head;
        } else {
            head = n;
            head.next = null;
            return head;
        }
    }
    static Node PrependNode(Node head, int data){
        Node n = new Node(data);
        if(head == null){
            head = n;
            return head;
        }
        n.next = head;
        head = n;
        return head;
    }
}
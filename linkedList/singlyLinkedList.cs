// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;
using System.Formats.Tar;
using System.Transactions;
public class Node {
    public  int data;
    public Node? next;
    public Node(int v){
        this.data = v;
        this.next = null;
    }
}
public class HelloWorld
{
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
        Console.WriteLine("\n");
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
    static Node AddNodeAtPosition(Node head, int data, int pos)
    {
        Node n = new Node(data);
        if(head == null)
        {
            head = n;
            head.next = null;
            return  head;
        } 
        if(head.next == null && pos != 0)
        {
            Console.WriteLine("Position outside the bounds of the list");
            return head;
        }
        if (pos == 0)
        {
            n.next = head;
            return n;
        }
        int count = 0;
        Node prev = head;
        Node curr = head.next;
        while(count != pos - 1)
        {
            prev = prev.next;
            if(curr.next == null && pos - 2 != count)
            {
                Console.WriteLine("Position outside the bounds of the list");
                return head;
            }
            curr = curr.next!;
            count += 1;
        }
        prev.next = n;
        n.next = curr;
        return head;
    }
    static Node DeleteAtBeginning(Node head)
    {
        if(head == null)
        {
            Console.WriteLine("The linked list is empty");
        }
        head = head.next;
        return head;
    }
    static Node DeleteAtEnd(Node head)
    {
        if(head == null)
        {
            Console.WriteLine("The linked list is empty");
        }
        if(head.next == null)
        {
            return null;
        }
        Node prev = head;
        Node temp = head.next;
        while(temp.next != null)
        {
            prev = prev.next;
            temp = temp.next;
        }
        prev.next = null;
        return head;
    }
    static Node DeleteNodeAtIndex(Node head, int index)
    {
        if(head == null)
            Console.WriteLine("The linked list is empty");
        if(head!.next == null)
            return null;
        if(index == 0)
        {
            return head.next;
        }
        Node prev = head;
        Node temp = head.next;
        int count = 0;
        while(count != index - 1)
        {
            if(temp.next == null && count + 1 != index){
                Console.WriteLine("Input index out of the bounds of the linked list");
                return head;
            }

            prev = prev.next;
            temp = temp.next;
            count += 1;
        }
        if(temp!.next != null)
        {
            prev.next = temp.next;
        } else
        {
            prev.next = null;
        }
        return head;
    }
    static Node DeleteFirstNodeWithValue(Node head, int value)
    {
        if(head == null)
        {
            Console.WriteLine("The linked list is empty");
            return head;
        }
        if(head.data == value)
        {
            head = head.next;
            return head;
        }
        Node prev = head;
        Node curr = head.next;
        while(curr.data != value)
        {
            if(curr.next == null && curr.next.data != value)
            {
                Console.WriteLine("No node in the linked list contains the input value");
                return head;
            }
            prev = prev.next;
            curr = curr.next;
        }
        prev!.next = curr.next;
        return head;
    }
        public static void Main(string[] args)
    {
        Node head = null;
        head = AppendNode(head, 10);
        head = AppendNode(head, 20);
        head = AppendNode(head, 30);
        head = AppendNode(head, 40);
        head = PrependNode(head, 9);
        head = PrependNode(head, 8);
        head = AddNodeAtPosition(head, 900, 2);
        head = AddNodeAtPosition(head, 901, 0);
        head = AddNodeAtPosition(head, 902, 7);
        head = AddNodeAtPosition(head, 902, 9);
        head = AddNodeAtPosition(head, 903, 11);
        DisplayList(head);
        head = DeleteAtBeginning(head);
        DisplayList(head);
        head = DeleteAtEnd(head);
        DisplayList(head);
        head = DeleteNodeAtIndex(head, 4);
        DisplayList(head);
        head = AppendNode(head, 111);
        DisplayList(head);
        head = DeleteFirstNodeWithValue(head, 111);
        DisplayList(head);
    }

} 
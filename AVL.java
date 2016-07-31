import java.util.LinkedList;
import java.util.Queue;
import java.math.*;
import java.lang.StringBuffer;


class Node {
	// Nodester
	int val;   //Value
    int ht;      //Height
    Node left;   //Left child
    Node right;   //Right child 
    StringBuffer s;
    
    Node(int val, int ht, Node left, Node right){
    	this.val = val;
    	this.ht = ht;
    	this.left = left;
    	this.right = right;
    }
    
    Node(int val, int ht){
    	this.val = val;
    	this.ht = ht;

    }
    
    void LevelOrder(){
    	this.s = new StringBuffer();
        int d = MaxDepth(this);
        for(int i =0; i< d; i++){
        	String hstr = new String(new char[(int)Math.pow(2, d-i-1)]).replace('\0', ' ');

        	this.s.append(hstr);
        	
            dp(this, i);
            this.s.append('\n');
        }
    }


    void dp(Node n, int i){
        if(i > 0){
            if(n.left != null){
               dp(n.left, i-1);
            }else{this.s.append(" ");}
            if(n.right != null){
               dp(n.right, i-1);
            }else{this.s.append(" ");}
        }
        else if(i==0){
        	this.s.append(" " + n.val + " ");
        }
        else{
            return;
        }
    }

    public static int MaxDepth(Node root){
        if (root == null)
            return 0;
        else
            return Math.max(MaxDepth(root.left), MaxDepth(root.right)) + 1;
    }

    
    public String toString() {
  
    	LevelOrder();
    	return this.s.toString();
    }
    

}


public class AVL {
 
	
	static Node insert(Node root, int val){
		/*
		 * BFS styled insert for binary tree
		 * Hopefully self balancing
		 */
		Queue<Node> q = new LinkedList<Node>();
		q.add(root);
		while(q.size() > 0){
			Node n = q.poll();

			int v = n.val;
				
			if(val > v){
				if(n.right != null)
					q.add(n.right);
				else
					n.right = new Node(val, 0);
			}else{
				if(n.left != null)
					q.add(n.left);
				else
					n.left = new Node(val, 0);
			}				
			
			
		}
		return root;
	}
    
    
    

    public static void main(String[] args){
    	// h = 2^n -1 singleton set is of height 0
    	Node T = new Node(2,1,
    			          new Node(1, 0),
    			          new Node(3, 0));
    	Node TPrime = insert(T,4);
    	//System.out.println(TPrime);
    	//System.out.println("SUCCESS");
    	
    }
    
    
}


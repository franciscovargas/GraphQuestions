import java.lang.Math.*;

class Node{ 
       int val;   //Value
       int ht;      //Height
       Node left;   //Left child
       Node right;   //Right child
}

public class AVL{
    
    static int getHeight(Node node){
        if (node == null)
            return -1;
        return node.ht;
    }

    static int getBalanceFac(Node node){
        if(node == null)
            return 0;
        int l = getHeight(node.left);
        int r = getHeight(node.right);
        return l - r;
    }

    static Node balance(Node root){
        if(getBalanceFac(root) ==2){
            if(getBalanceFac(root.left) == -1 )
                root.left = rotateLeft(root.left);
            return rotateRight(root);
        }else if(getBalanceFac(root) == -2){
            if(getBalanceFac(root.right) == 1)
                root.right = rotateRight(root.right);
            return rotateLeft(root);
        }

        newHeight(root);
        return root;
        
    }


    static Node insert(Node root, int val){
        if (root == null){
            final Node node = new Node();
            node.val = val;
            node.ht = 0;
            return node;
        }

        if(val < root.val){
            root.left = insert(root.left, val);
        }else{
            root.right = insert(root.right, val);
        }

        root = balance(root);
        return root;
    }

    static Node rotateLeft(Node root){
        if (root == null){
            return root;
        }

        Node new_root = root.right;
        root.right = new_root.left;
        new_root.left = root;

        // recompute heights:
        newHeight(root);
        newHeight(new_root);

        return new_root;
    }

    static Node rotateRight(Node root){
        
        if (root == null){
            return root;
        }

        Node new_root = root.left;
        root.left = new_root.right;
        new_root.right = root;

        // recompute heights:
        newHeight(root);
        newHeight(new_root);
        return new_root;

    }

    static void newHeight(Node root){
        if(root != null)
            root.ht = Math.max(getHeight(root.left), getHeight(root.right)) +1;
    }

    public static void main (String[] args){

        System.out.println("AVL file ends");
    }

}

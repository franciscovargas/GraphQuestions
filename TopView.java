void printer(Node root, HashSet<Integer> v ){
	if(root == null) return;
	printer(root.left, v);
	if(v.contains(root.data) ) System.out.print(root.data + " ");
	printer(root.right, v);
}

void top_view(Node root){
	
	Queue<AbstractMap.SimpleEntry<Integer,Node>> q = new LinkedList<AbstractMap.SimpleEntry<Integer,Node>>();
	HashSet<Integer> visited = new HashSet<Integer>();
	HashSet<Integer> values = new HashSet<Integer>();
    
	q.add( new AbstractMap.SimpleEntry<Integer,Node>(0, root) );

	while(!q.isEmpty()){
		AbstractMap.SimpleEntry<Integer, Node> head = q.remove();
		Node n = head.getValue();

		if (!visited.contains(head.getKey())){
			visited.add(head.getKey());
			values.add(n.data);
		}
		if (n.left != null)
			q.add( new AbstractMap.SimpleEntry<Integer,Node>(head.getKey() - 1, n.left) );
		if (n.right != null)
			q.add( new AbstractMap.SimpleEntry<Integer,Node>(head.getKey() + 1, n.right) );

	}
    printer(root, values);

}

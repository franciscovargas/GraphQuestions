package test2;
import java.util.Queue;
import java.util.List;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Collections;

public class BFS {
	
	public static void search(HashMap<String, List<String>> G,  String root){
		Queue<String> queue = new LinkedList<String>();
		queue.add(root);
		
		HashSet<String> visited = new HashSet<String>();
		visited.add(root);
		
		while(!queue.isEmpty()){
			String parent = queue.poll();
			System.out.println(parent);
			for(String child: G.get(parent)){
				if(!visited.contains(child)){
					queue.add(child);
					visited.add(child);
				}
			}
		}
	}
	
	
	public static void main(String[] args){
		HashMap<String, List<String>> G = new HashMap<String, List<String>>();

		G.put("A", Arrays.asList( "B", "C", "D") );
		G.put("B", Arrays.asList("C"));
		G.put("D", Arrays.asList("E"));
		G.put("E", Collections.<String>emptyList());
		G.put("C", Collections.<String>emptyList());
		search(G, "A");
	}
}

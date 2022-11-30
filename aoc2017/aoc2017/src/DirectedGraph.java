import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class DirectedGraph <V>{
    int size;
    // ArrayList<Node<V>> nodes = new ArrayList<>();
    V root;
    HashMap<V, HashSet<V>> nodes;

    public DirectedGraph(V root) {
        this.size = 0;
        this.root = root;
        nodes = new HashMap<>();
        nodes.put(root, new HashSet<>());
    }


    public void addNeighbours(ArrayList<V> n, V r) {
        HashSet<V> set = new HashSet<>();
        for (V v : n) {
            set.add(v);
        }
        nodes.put(r, set);
    }
}

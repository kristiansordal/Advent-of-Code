import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day12<V>{
    public static void main(String[] args) throws FileNotFoundException {
        FileReader f = new FileReader("src/day12.in");
        Scanner sc = new Scanner(f);
        Pattern p = Pattern.compile("\\d+");
        ArrayList<Input<Integer>> input = new ArrayList<>();
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            Matcher m = p.matcher(line);
            ArrayList<Integer> in = new ArrayList<>();
            while (m.find()) {
                in.add(Integer.parseInt(m.group()));
            }
            input.add(new Input<Integer>(in));
        }
        sc.close();

        DirectedGraph<Integer> graph = new DirectedGraph<>(0);

        for (Input<Integer> in : input) {
            graph.addNeighbours(in.nodes, in.root);
        }

    }

}

class Input<V> {
    ArrayList<V> nodes;
    V root;

    public Input(ArrayList<V> nodes) {
        this.root = nodes.remove(0);
        this.nodes = nodes;
    }
}

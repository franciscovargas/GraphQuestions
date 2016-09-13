#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <deque>


using namespace std;

void BFS(unordered_map<string,unordered_set<string>> &graph, string node){


    deque<string> que = {node};
    unordered_set<string> cache = {node};

    while( !(que.empty()) ){

        string cur_node = que.front();
        que.pop_front();

        unordered_set<string> children = graph[cur_node];
        for(unordered_set<string>::iterator a = children.begin(); a != children.end(); ++a) {
            string child = *a;

            const bool b = !(cache.find(child) != cache.end());
            if(b ) {
                cout << child << endl;
                que.push_back(child);
                cache.insert(child);
            }
        }

    }
}


int main(){
    unordered_map<string, unordered_set<string>> graph;
    graph["A"] = {"B", "C"};
    graph["B"] = {"C"};
    graph["C"] = {"D"};
    graph["D"] = {"E"};
    BFS(graph, "A");
    return 0;
}

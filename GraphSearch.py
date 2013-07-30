'''
Created on Jul 30, 2013

@author: root
'''

class GraphSearch(object):
    '''
    classdocs
    '''
    def __init__(self, graph):
        self.graph = graph
        
    def find_path(self, start, end, path=[]):
        self.start = start
        self.end = end
        self.path = path
        
        self.path += [self.start]
        if self.start == self.end:
            return self.path
        if not self.graph.has_key(self.start):
            return None
        
        for node in self.graph[self.start]:
            if node not in self.path:
                newpath = self.find_path(node, self.end, self.path)
                if newpath:
                    return newpath
        return None

    def find_all_path(self, start, end, path=[]):
        self.start = start
        self.end = end
        
        self.finished = False
        path_tmp = path[:]
        self.path = path[:]
        
        path_tmp += [self.start]
        
        if self.start == self.end:
            self.finished = True
            return [path_tmp]
        
        if not self.graph.has_key(self.start):
            return []
        
        paths = []
        for node in self.graph[self.start]:
            if node not in path_tmp:
                newpaths = self.find_all_path(node, self.end, path_tmp)
                for newpath in newpaths:
                    paths.append(newpath)

            
        return paths

    def find_shortest_path(self, start, end, path=[]):
        self.start = start
        self.end = end
        
        self.finished = False
        path_tmp = path[:]
        self.path = path[:]
        
        path_tmp += [self.start]
        
        if self.start == self.end:
            self.finished = True
            return [path_tmp]
        
        if not self.graph.has_key(self.start):
            return []
        
        paths = []
        for node in self.graph[self.start]:
            if node not in path_tmp:
                newpaths = self.find_all_path(node, self.end, path_tmp)
                for newpath in newpaths:
                    paths.append(newpath)

        path_sel_idx = 0
        path_sel_len = len(paths[path_sel_idx])
        
        for path_idx in range(1, len(paths)):
            len_tmp = len(paths[path_idx])
            if len_tmp < path_sel_len:
                path_sel_len = len_tmp
                path_sel_idx = path_idx 
                
        return paths[path_sel_idx]
    
if __name__ == "__main__":
    graph = {'A':['B', 'C'],
             'B':['C', 'D'],
             'C':['D'],
             'D':['C'],
             'E':['F'],
             'F':['C'],
             }
    
    graph1 = GraphSearch(graph)
    print graph1.find_path("A", "D")
    print graph1.find_all_path("A", "D")
    print "The shortest path is:"
    print graph1.find_shortest_path("A", "D")
    
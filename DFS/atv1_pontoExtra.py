# Deve ler um arquivo chamdo matriz.txt, e encontrar um caminho entre os vertices da matriz de adjacência
# Um caminho eh uma trilha (não repete arestas) e que não repete os vertices

def getMatrixFromArchive(path : str):
    try:
        file = open(path, "r", )
    except FileNotFoundError as e:
        print(f"{e.filename} não encontrado")
        return None

    linhas = file.readlines()
    matrix_order = int(linhas[0].replace("\n",""))
    matrix = []
    initial_v, final_v  = linhas[-1].rsplit(" ")
    
    initial_v = int(initial_v) 
    final_v = int(final_v)
    
    for linha in linhas[1:-1]:
        linha = linha.replace("\n","")
        newMatrixLine = []
        
        for valor in linha:
            if valor != " ":
                newMatrixLine.append(int(valor))
        matrix.append(newMatrixLine)
    
    return (matrix_order, matrix, initial_v, final_v)

def findPath(m,initial_v,final_v):
        visited = []
        if DFS(m,initial_v,final_v,visited):
            print(f"{visited}")
        else:
            print(f"Caminho não encontrado entre {initial_v} e {final_v}")
            
        ...

def DFS(m, vactual, final_v, visited: list):    
    visited.append(vactual)
    
    if vactual == final_v:
        return True
    
    # Explorar os vizinhos
    for neighbor in getNeighbors(m,vactual):
        if neighbor not in visited:
            if DFS(m,neighbor, final_v, visited):
                return True
            pass
        pass
    visited.pop(visited.index(vactual))
    return False




def getNeighbors(m: list,vactual):
    neighbors = []
    for vertices in range(len(m)):
        if vertices == vactual:
            iterator = 0
            for edges in m[vertices]:
                if edges == 1:
                    neighbors.append(iterator)
                iterator+=1
    return neighbors



def main():
    m_order, m, initial_v, final_v = getMatrixFromArchive(r"DFS/matrix.txt")
    
    findPath(m, initial_v, final_v)


if __name__ == "__main__":
    main()
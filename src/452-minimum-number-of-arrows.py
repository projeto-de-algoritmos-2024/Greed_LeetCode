class Solution(object):
    def findMinArrowShots(self, points):
        # ordena pela primeira posicao e o criterio de 
        # desempate é o segundo
        sorted_points = sorted(points)
        
        # vai usar uma flecha
        arrows = 1
        a = sorted_points[0]

        # pega os balões em ordem 
        for i in range(1, len(points)):
            # se o fim do balão de referencia for menor que o
            # inicio do proximo, tem que gastar flecha e o balao
            # da vez é o de referência
            if a[1] < sorted_points[i][0]:
                arrows += 1
                a = sorted_points[i]
            if a[1] > sorted_points[i][1]:
                a = sorted_points[i]
                
        return arrows


def imprime(a):
    k = 0
    for p in a:
        if p[1] > k:
            k = p[1]
    
    a = sorted(a)
    m = [[' ' for _ in range(k+1)] for _ in range(len(a))]

    for i in range(len(a)):
        j = 0
        for j in range(k+1):
            if a[i][0] <= j and j <= a[i][1]:
                m[i][j] = '-'
                j += 1
    
    for i in range(len(a)):
        print('  '.join(m[i]))

s = Solution()

a5 = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]


imprime(a5)
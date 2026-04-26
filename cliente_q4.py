import rpyc
import sys
import time

if len(sys.argv) < 2:
    exit("Usage: {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

# Usuário define o tamanho do vetor
n = int(input("Digite o valor de n: "))

# Cria vetor de 0 a n-1
vetor = list(range(n))

conn = rpyc.connect(server, 18861)

# Mede o tempo total no cliente (inclui envio, processamento e retorno)
start = time.time()
resultado = conn.root.sum_vector(vetor)
end = time.time()

print(f"Soma dos elementos: {resultado}")
print(f"Tempo de execução no cliente: {end - start}")

import rpyc
import sys
import time

def soma(n, server):
    conn = rpyc.connect(server, 18861)
    # Cria vetor de 0 a n-1
    vetor = list(range(n))
    # Mede o tempo total no cliente (inclui envio, processamento e retorno)
    start = time.time()
    resultado, tempo_servidor = conn.root.sum_vector_with_time(vetor)
    end = time.time()
    return resultado, tempo_servidor, end - start

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Usage: {} SERVER".format(sys.argv[0]))

    server = sys.argv[1]

    # Usuário define o tamanho do vetor
    n = int(input("Digite o valor de n: "))

    resultado, tempo_servidor, tempo_cliente = soma(n, server)

    print(f"Soma dos elementos: {resultado}")
    print(f"Tempo de execução no cliente: {tempo_cliente}")
    print(f"Tempo de execução no servidor: {tempo_servidor}")


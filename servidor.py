import rpyc
import time


class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código executado quando uma conexão é iniciada
        print("Cliente conectado!")

    def on_disconnect(self, conn):
        # código executado quando uma conexão é finalizada
        print("Cliente desconectado!")

    def exposed_get_answer(self):  # método exposto
        return 42

    exposed_the_real_answer_though = 43  # atributo exposto

    def get_question(self):  # método NÃO exposto
        return "Qual é a cor do cavalo branco de Napoleão?"

    def exposed_sum_vector(self, vector):
        """Recebe um vetor e retorna a soma dos elementos."""
        start = time.time()
        resultado = sum(vector)
        end = time.time()
        print(f"Tempo de execução no servidor: {end - start}")
        return resultado
    
    def exposed_sum_vector_with_time(self, vector):
        """Recebe um vetor e retorna a soma dos elementos e o tempo de execução."""
        start = time.time()
        resultado = sum(vector)
        end = time.time()
        return [resultado, end-start]


# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    print("Servidor iniciado na porta 18861...")
    t.start()

import rpyc
import time
import json
from datetime import datetime
from cliente_q4 import soma

# Constantes
NUM_EXECUCOES = 10
TAMANHO_VETOR = 10000
# 192.168.1.13
SERVIDOR = "localhost"
PORTA = 18861

# Listas para armazenar resultados
resultados = []
tempos_cliente = []
tempos_servidor = []

# Executa o cliente múltiplas vezes
for i in range(NUM_EXECUCOES):
    try:
        resultado, tempo_servidor, tempo_cliente = soma(TAMANHO_VETOR, SERVIDOR)
        
        # Armazena os resultados
        tempos_cliente.append(tempo_cliente)
        tempos_servidor.append(tempo_servidor)
        resultados.append({
            "execucao": i + 1,
            "soma": resultado,
            "tempo_cliente": tempo_cliente,
            "tempo_servidor": tempo_servidor
        })
        
        print(f"Execução {i + 1}/{NUM_EXECUCOES}: Cliente={tempo_cliente:.15f}s, Servidor={tempo_servidor:.15f}s")
        
    except Exception as e:
        print(f"Erro na execução {i + 1}: {e}")

# Calcula médias
media_cliente = sum(tempos_cliente) / len(tempos_cliente) if tempos_cliente else 0
media_servidor = sum(tempos_servidor) / len(tempos_servidor) if tempos_servidor else 0

# Adiciona resumo
resumo = {
    "configuracao": {
        "num_execucoes": NUM_EXECUCOES,
        "tamanho_vetor": TAMANHO_VETOR,
        "servidor": SERVIDOR,
        "porta": PORTA
    },
    "resultados": resultados,
    "resumo": {
        "media_tempo_cliente": media_cliente,
        "media_tempo_servidor": media_servidor,
        "timestamp": datetime.now().isoformat()
    }
}

# Salva em arquivo JSON
nome_arquivo = f"{TAMANHO_VETOR}_{SERVIDOR}.json"
with open(nome_arquivo, 'w') as f:
    json.dump(resumo, f, indent=2)

# Exibe resumo
print(f"\n{'='*50}")
print("RESUMO DOS RESULTADOS")
print(f"{'='*50}")
print(f"Execuções: {NUM_EXECUCOES}")
print(f"Tamanho do vetor: {TAMANHO_VETOR}")
print(f"Tempo médio no cliente: {str(media_cliente).replace('.', ',')}")
print(f"Tempo médio no servidor: {str(media_servidor).replace('.', ',')}")
print(f"Resultados salvos em: {nome_arquivo}")

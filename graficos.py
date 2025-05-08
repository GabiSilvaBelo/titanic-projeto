import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar ao banco de dados
conexao = sqlite3.connect("titanic.db")

# Carregar os dados da tabela em um DataFrame
df = pd.read_sql_query("SELECT * FROM passageiros", conexao)

# Gráfico 1: Distribuição de sobreviventes
sobreviventes = df["sobrevivente"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(["Não Sobreviveu", "Sobreviveu"], sobreviventes, color=["red", "green"])
plt.title("Distribuição de Sobreviventes")
plt.ylabel("Quantidade")
plt.savefig("grafico_sobreviventes.png")
plt.show()

# Gráfico 2: Média de idade por classe
media_idade = df.groupby("classe")["idade"].mean()
plt.figure(figsize=(6, 4))
media_idade.plot(kind="bar", color="skyblue")
plt.title("Média de Idade por Classe")
plt.xlabel("Classe")
plt.ylabel("Idade Média")
plt.savefig("grafico_idade_classe.png")
plt.show()

# Gráfico 3: Sexo x Taxa de Sobrevivência
taxa_sobrevivencia = df.groupby("sexo")["sobrevivente"].mean() * 100
plt.figure(figsize=(6, 4))
taxa_sobrevivencia.plot(kind="bar", color=["purple", "orange"])
plt.title("Taxa de Sobrevivência por Sexo")
plt.ylabel("Taxa (%)")
plt.savefig("grafico_taxa_sobrevivencia.png")
plt.show()

# Fechar conexão
conexao.close()

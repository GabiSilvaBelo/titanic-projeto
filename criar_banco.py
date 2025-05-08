import sqlite3
import csv

# Conectar ao banco
conexao = sqlite3.connect("titanic.db")
cursor = conexao.cursor()

# Criar tabela (apague se já existir para recomeçar do zero)
cursor.execute("DROP TABLE IF EXISTS passageiros")
cursor.execute("""
CREATE TABLE passageiros (
    id INTEGER PRIMARY KEY,
    sobrevivente INTEGER,
    classe INTEGER,
    nome TEXT,
    sexo TEXT,
    idade REAL
)
""")

# Abrir o CSV e inserir os dados
with open("titanic.csv", newline='', encoding="utf-8") as csvfile:
    leitor = csv.DictReader(csvfile)
    for linha in leitor:
        cursor.execute("""
            INSERT INTO passageiros (id, sobrevivente, classe, nome, sexo, idade)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            int(linha["PassengerId"]),
            int(linha["Survived"]),
            int(linha["Pclass"]),
            linha["Name"],
            linha["Sex"],
            float(linha["Age"]) if linha["Age"] else None
        ))

conexao.commit()
conexao.close()
print("✅ Banco criado e dados inseridos com sucesso.")

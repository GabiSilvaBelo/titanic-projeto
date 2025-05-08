import sqlite3

# Conecta ao banco
conexao = sqlite3.connect("titanic.db")
cursor = conexao.cursor()

print("\n1. Total de passageiros:")
cursor.execute("SELECT COUNT(*) FROM passageiros")
print(cursor.fetchone()[0])

print("\n2. Total de sobreviventes:")
cursor.execute("SELECT COUNT(*) FROM passageiros WHERE sobrevivente = 1")
print(cursor.fetchone()[0])

print("\n3. Média de idade por classe:")
cursor.execute("""
    SELECT classe, ROUND(AVG(idade), 2) 
    FROM passageiros 
    WHERE idade IS NOT NULL 
    GROUP BY classe
""")
for linha in cursor.fetchall():
    print(f"Classe {linha[0]}: {linha[1]} anos")

print("\n4. Quantidade de homens e mulheres:")
cursor.execute("""
    SELECT sexo, COUNT(*) 
    FROM passageiros 
    GROUP BY sexo
""")
for linha in cursor.fetchall():
    print(f"{linha[0]}: {linha[1]}")

print("\n5. Taxa de sobrevivência por sexo:")
cursor.execute("""
    SELECT sexo, ROUND(AVG(sobrevivente) * 100, 2)
    FROM passageiros
    GROUP BY sexo
""")
for linha in cursor.fetchall():
    print(f"{linha[0]}: {linha[1]}%")

# Fecha a conexão
conexao.close()

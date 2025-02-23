import os
import subprocess
import sys

# Função para verificar se o Python está instalado
def verificar_python():
    try:
        subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python está instalado.")
    except subprocess.CalledProcessError:
        print("Python não encontrado. Certifique-se de que o Python está instalado.")
        sys.exit(1)

# Função para criar o ambiente virtual
def criar_ambiente():
    ambiente_path = "env"
    
    # Verifica se o ambiente já existe
    if os.path.exists(ambiente_path):
        print(f"O ambiente virtual já existe em '{ambiente_path}'.")
    else:
        print("Criando o ambiente virtual...")
        subprocess.run([sys.executable, "-m", "venv", ambiente_path], check=True)
        print(f"Ambiente virtual '{ambiente_path}' criado com sucesso.")

# Função para ativar o ambiente virtual
def ativar_ambiente():
    ambiente_path = "env"
    
    # Verifica se o ambiente foi criado
    if not os.path.exists(ambiente_path):
        print("O ambiente virtual não foi criado. Abortando.")
        sys.exit(1)
    
    # Determina o script de ativação baseado no sistema operacional
    if os.name == "nt":  # Windows
        ativar_script = os.path.join(ambiente_path, "Scripts", "activate.bat")
    else:  # Linux/Mac
        ativar_script = os.path.join(ambiente_path, "bin", "activate")

    # Executa o script de ativação
    print(f"Ativando o ambiente virtual com o script {ativar_script}...")
    subprocess.run(ativar_script, shell=True)

def main():
    verificar_python()  # Verificar se o Python está instalado
    criar_ambiente()    # Criar o ambiente virtual
    ativar_ambiente()   # Ativar o ambiente virtual

if __name__ == "__main__":
    main()

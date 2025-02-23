import os
import subprocess

def criar_ambiente_virtual(nome_ambiente):
    # Cria o ambiente virtual
    subprocess.run(f'python -m venv {nome_ambiente}', shell=True)
    print(f'Ambiente virtual "{nome_ambiente}" criado com sucesso.')

def ativar_ambiente_virtual(nome_ambiente):
    # Ativa o ambiente virtual
    activate_script = os.path.join(nome_ambiente, 'Scripts', 'activate.bat')
    subprocess.run(activate_script, shell=True)
    print(f'Ambiente virtual "{nome_ambiente}" ativado com sucesso.')

if __name__ == "__main__":
    nome_ambiente = "meu_ambiente"
    criar_ambiente_virtual(nome_ambiente)
    ativar_ambiente_virtual(nome_ambiente)

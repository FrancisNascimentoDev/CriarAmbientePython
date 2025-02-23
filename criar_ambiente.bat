@echo off
:: Verificar se o Python está instalado
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python não encontrado! Certifique-se de que o Python está instalado.
    pause
    exit /b
)

:: Criar um novo ambiente virtual
echo Criando ambiente virtual...
python -m venv env

:: Verificar se a criação foi bem-sucedida
IF NOT EXIST "env\Scripts\activate.bat" (
    echo Falha na criação do ambiente virtual.
    pause
    exit /b
)

:: Ativar o ambiente virtual
echo Ambiente virtual criado com sucesso! Ativando...
call env\Scripts\activate.bat

:: Confirmar se o ambiente foi ativado
IF "%VIRTUAL_ENV%"=="" (
    echo Falha ao ativar o ambiente virtual.
    pause
    exit /b
)

echo Ambiente virtual ativado com sucesso!
pause

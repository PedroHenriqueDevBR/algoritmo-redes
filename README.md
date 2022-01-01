# algoritmo-redes

Apresentação de trabalho para a disciplina de redes de computadores.

# Verificação CRC

A verificação cíclica de redundância é um método de detecção de erros normalmente usada em redes digitais e dispositivos de armazenamento para detectar mudança acidental em cadeias de dados.

**Testando algoritmo**

```bash
# Acesse o diretório com o algoritmo em  CRC/ e execute o método que você preferir

> python receptor.py
> python transmitter.py
```

Forneça as informações como no exemplo abaixo

```
venv) ╭─ubuntu@ubuntu ~/Cloud/github/algoritmo-redes ‹master●› 
╰─$ python CRC/receptor.py # execução do algoritmo 
Enter the CRC message (Ex. 10011101100): 10011101100
Enter the generator (Ex. 1001): 1001 

Entered CRC message: 10011101100
Entered generator: 1001

Remainder is: 000
No error is present in the received message
```

# Código de Hamming

O código de Hamming é um código de bloco linear, foi desenvolvido por Richard Hamming, é utilizado no processamento de sinal e nas telecomunicações. A sua utilização permite a transferência e armazenamento de dados de forma segura e eficiente.

**Testando algoritmo**

Para executar o código de Hamming você vai precisar instalar o django

```bash
# Acesse o diretório com o algoritmo em  CRC/ e execute o método que você preferir

pip3 install django

# acesse a aplicação django

cd hamming/graphic_interface/g_interface/

# Execute a aplicação e acesse em localhost:8000

python manage.py runserver

```
# Extrai Imagem

Este é um programa de linha de comando (CLI) em Python que extrai todos os frames de um arquivo de vídeo e os salva como imagens no formato PNG. Os frames são armazenados em uma pasta chamada `image_output`, que é criada dentro de uma pasta com o nome do arquivo de vídeo original (sem a extensão).

## Requisitos

- Python 3.6 ou superior
- Dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone este repositório ou copie o arquivo `app.py` para o seu ambiente local.
2. Instale as dependências necessárias com o comando:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Execute o script passando o caminho do arquivo de vídeo como argumento:

```bash
    python app.py video.mp4
```

## Mensagens de Erro

- **Erro: O arquivo 'arquivo.mp4' não foi encontrado.**

  - Certifique-se de que o caminho para o arquivo de vídeo está correto.

- **Erro: Não foi possível abrir o arquivo de vídeo arquivo.mp4'.**

  - Verifique se o arquivo de vídeo está corrompido ou em um formato incompatível.

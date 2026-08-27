# Hand-Tracking-com-OpenCV-e-MediaPipe
Este projeto demonstra o uso das bibliotecas OpenCV e MediaPipe para rastreamento de mãos em tempo real. O código captura vídeo da câmera, processa a imagem para detectar e desenhar marcos das mãos, e exibe as informações na tela.



🛠️ Tecnologias Utilizadas
-
- OpenCV: Biblioteca para processamento de imagem e vídeo.
- MediaPipe: Biblioteca do Google para modelos de aprendizado de máquina que realiza o rastreamento de mãos.

🔍 Como Funciona
-
- Configuração da Câmera: Define a largura e altura do vídeo da câmera.
- Inicialização do MediaPipe Hands: Configura o modelo de detecção de mãos.
- Captura e Processamento de Frames:
- Captura o frame atual da câmera.
- Converte o frame para o formato RGB.
- Processa a imagem para detectar mãos.
- Desenha marcos das mãos e suas conexões sobre a imagem.
- Exibe os IDs dos pontos de referência das mãos.

Exibição e Controle:
- 
  Mostra a imagem processada com marcos desenhados.
  Permite sair do loop de visualização pressionando a tecla 'q'.



---

Este projeto é a base de extração de landmarks que evoluiu para o
[detector de sinais de Libras](https://github.com/alissonamorim2004/IA-de-Reconhecimento-de-Libras),
meu TCC — reconhecimento em tempo real com CNN, premiado em competição na
faculdade.

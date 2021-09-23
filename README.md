# Tft bot

Bot para farmar pontos do Passe de Batalha do TFT

## Descrição

A cada partida de tft jogada você ganha 100 pontos no passe, porém você não precisa jogar a partida toda, basta jogar até a rodada 3-4 e dar surrender. O bot irá dar queue, aceitar a partida
jogar até a rodada 3-4, dar surrender e dar play again. Também irá reconectar caso por algum motivo sua partida caia.

O bot funciona com reconhecimento de imagens

### Dependencias

* Python 3.9.6
* Módulos pyautogui e imagesearch
* O bot foi configurado em um monitor 1920x1080 e a resolução do client (tela onde coloca na fila) em 1280x720. Caso queira que funcione em outra resolução basta tirar os prints das imagens na resolução que você deseja usar

### Executando

* Basta executar o arquivo .py e colocar o lol nesta tela
* ![Image1](https://i.imgur.com/UZV3KiS.png)

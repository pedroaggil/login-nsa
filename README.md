# Bot para login no NSA

O Novo Sistema Acadêmico (NSA) é essencial para o estudante do Centro Paula Souza. No entanto, o sistema não permanece logado depois de você fechar a página, tornando o movimento de login *repetitivo, cansativo e estressante*.

No entanto, como bom estudante que detesta movimentos repetitivos, cansativos e estressantes, ***automatizei*** o processo com o desenvolvimento de um bot feito a partir de **Selenium**.

##

Resumidamente, o sistema abre o seu navegador, abre a página do NSA e realiza o login. Simples, rápido e eficiente. Leva menos de 10s para finalizar e o único passo que você precisa realizar é executar o código.

Para usar, você deverá ter instalado previamente o selenium, dessa forma:

`pip install selenium`

Você também deverá definir o seu navegador.

Primeiro, veja a versão de seu navegador. Usarei como modelo o Chrome, mas é possível adaptar.
```
Menu -> Ajuda -> Sobre
```
A versão estará exposta nesta área; pesquise pela versão do **chromedriver** correspondente.
Veja no link < https://chromedriver.chromium.org/downloads >.

Após baixar, mova o arquivo para a pasta correspondete ao seu IDE (seja ele o Jupyter, PyCharm etc). Caso não saiba, procure pelo arquivo `python.exe`.
Um exemplo comum para Jupyter, veja:
```
C:\Users\seuusuario\anaconda3
```

Note que você deverá ter previamente instalado o Python em seu sistema para executar o código.
Após isso, o selenium já estará funcionando em sua máquina.

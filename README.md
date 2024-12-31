# Merge PDFs

This application merge two PDFs in one.

Download realese Mac or Windows.

<br>


![Home](https://github.com/fabioacarvalho/merge-pdfs/blob/main/assets/img/image.png?raw=true)

<br>


Download QtDesign (Win and Mac): https://build-system.fman.io/qt-designer-download

## Utils for Developers

- Command to convert `.ui` to `.py`:

```bash
pyside6-uic ./src/design.ui -o ./src/design.py
```

<br>

- Generate files executable for (Mac and Win):


```bash
pyinstaller --onefile --noconsole --windowed main.py
```

<br>

> --onefile: Gera um único arquivo executável.
> --noconsole: Remove a janela do console em aplicativos GUI.
> --windowed (ou -w): Gera uma aplicação de GUI sem terminal (necessário para macOS).

<br>

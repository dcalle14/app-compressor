Project developed by Santiago Cordoba Fuentes and Gustavo Andres Mendez Barrera

# Text compressor and decompressor.

Data compression is the reduction of the volume of data that can be processed to represent a certain information using a smaller amount of space. In this project, the use of RLE compression or Run-length encoding is a very simple form of data compression in which data sequences with the same consecutive value are stored as a single value plus its count.

## Prerequisites

- To run the program it is important to have Visual Studio Code and the Python programming language extension installed.
- To run the program from the console you must run the following command: `src\console\rle_compression_console.py`

## Project Architecture

In this project the library used for the validation of unit tests is *unittest* which provides us with a set of tools to build and execute tests.

## Files description 

This project is structured as follows:

```
Text Compressor/
├── .vscode
│   └── settings.json
│
│
├── src
│   ├── console
│   │    └── rle_compression_console.py  # Lógica para la interfaz de línea de comandos
│   │    
│   └── functionalities
│       ├── _init_.py
│       └── rle_compression.py      # Lógica de las funcionalidades para compresión y descompresión texto 
│
│
├── tests
│   ├── _init_.py
│   └── rle_compression_tests.py    # Pruebas para la lógica de compresión y descompresión de texto
│ 
│
├── .gitignore    # Rutas excluidas del control de versión
├── LICENSE       # Licencia del proyecto
└── README.md     # Documentación del proyecto
```

## Program use

In this section I will explain the way in which you can run both the unit tests and the program console for greater experience.

1. To run the unit tests, from the src folder, use the command: `tests\rle_compression_tests.py` In order to run from the root folder, you must indicate the search path where the modules are located, including the following lines at the beginning of the test module.
2. To run the program from the console you must run the following command: `src\console\rle_compression_console.py`

This is a second part of the release for this project after doing some refactoring and applying clean code principles.
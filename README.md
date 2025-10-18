
# QR Code Inventory Manager (Python + OpenCV + Pyzbar)

> PT/BR: *Sistema simples e funcional para leitura de QR Codes com webcam, registro automático de produtos e controle de inventário em arquivo CSV.*  

> EN: *A simple and functional QR Code reader using a webcam, with automatic product registration and inventory control stored in a CSV file.*

---

## Languages
- [PT/BR - Versão em Português](#ptbr---versão-em-português)
- [EN - English Version](#en---english-version)

---

## PT/BR - Versão em Português

### Gerenciador de Inventário por QR Code  

Um sistema em **Python** que utiliza **OpenCV** e **Pyzbar** para realizar a leitura de **QR Codes em tempo real** pela webcam.  
Cada QR Code representa um produto armazenado em um arquivo CSV, permitindo **cadastrar novos produtos** ou **atualizar quantidades existentes** através de um menu interativo no terminal.

---

### Funcionalidades
- Leitura de QR Codes em tempo real pela câmera.  
- Registro e atualização automática de produtos.  
- Armazenamento de dados em arquivo CSV.  
- Menu interativo em linha de comando.  
- Estrutura simples, expansível e intuitiva.

---

### Tecnologias
- **Python 3.13**  
- **OpenCV** (`cv2`)  
- **Pyzbar** (`pyzbar.pyzbar`)  
- **CSV** (biblioteca nativa)  
- **OS**, **Time**

---

### Como Executar
1. Clone este repositório:  
```bash
   git clone https://github.com/seuusuario/qr-code-inventory.git
   cd qr-code-inventory
````

2. Instale as dependências:
```bash
   pip install opencv-python pyzbar
````

3. Execute o script:
```bash
   python main.py
````

---

### Armazenamento de Dados

Todos os produtos são salvos no arquivo:

```
produtos.csv
```

Estrutura do CSV:

| ID | Produto | QRCode | Quantidade |
| -- | ------- | ------ | ---------- |

---

### Melhorias Futuras

* Interface gráfica com CustomTkinter.
* Integração com banco de dados (SQLite/MySQL).
* Autenticação de usuários e permissões.
* Geração de QR Codes para novos produtos.

---

**Desenvolvido em Python para gestão prática de inventário e aprendizado de visão computacional.**

---

## EN - English Version

### QR Code Inventory Manager

A **Python-based system** that uses **OpenCV** and **Pyzbar** to scan **QR Codes in real time** via webcam.
Each QR Code corresponds to a product stored in a CSV file, allowing the user to **register new products** or **update existing quantities** through an interactive terminal menu.

---

### Features

* Real-time QR Code scanning using the webcam.
* Automatic product registration and quantity updates.
* Data stored in a structured CSV file.
* Interactive command-line menu for user actions.
* Simple, modular, and extensible design.

---

### Technologies

* **Python 3.13**
* **OpenCV** (`cv2`)
* **Pyzbar** (`pyzbar.pyzbar`)
* **CSV** (native library)
* **OS**, **Time**

---

### How to Run

1. Clone this repository:
```bash
   git clone https://github.com/yourusername/qr-code-inventory.git
   cd qr-code-inventory
````

2. Install dependencies:
```bash
   pip install opencv-python pyzbar
````

3. Run the script:
```bash
   python main.py
````

---

### Data Storage

All registered products are saved in the file:

```
produtos.csv
```

CSV structure:

| ID | Product | QRCode | Quantity |
| -- | ------- | ------ | -------- |

---

### Future Improvements

* GUI interface using Tkinter or PyQt.
* Database integration (SQLite/MySQL).
* User authentication and role-based permissions.
* QR code generation for new products.

---

**Developed in Python for efficient inventory control and computer vision learning.**

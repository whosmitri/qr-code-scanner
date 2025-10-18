
# IMPORTANDO BIBLIOTECAS IMPORTANTES

import cv2
from pyzbar.pyzbar import decode
import csv
import os
import time

print('Diretório atual:', os.getcwd())

# CONFIGURANDO CSV

# arquivo para salvamento dos produtos
arquivo_csv = "produtos.csv"

# cria o arquivo CSV com cabeçalho se não existir
if not os.path.exists(arquivo_csv):
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Produto", "QRCode", "Quantidade"])      # este é o cabeçalho



# FUNÇÕES

# função que abre o arquivo CSV e lê os produtos existentes
def carregar_registros():
    registros = []
    with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            registros.append(row)
    return registros

# função que salva novos produtos no arquivo CSV
def salvar_registros(registros):
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Produto", "QRCode", "Quantidade"])
        writer.writeheader()
        writer.writerows(registros)
        
# mostra o menu de opções
def menu_interativo(qr_code, produto_existe, produto_nome=None, quantidade=None):
    while True:
        print("\nMENU")
        if produto_existe:
            print("[1] Adicionar quantidade ao produto existente")
        else:
            print("[1] Inserir nome do novo produto")
        print("[2] Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registros = carregar_registros()
            if produto_existe:
                for r in registros:
                    if r["QRCode"] == qr_code:
                        r["Quantidade"] = str(int(r["Quantidade"]) + 1)
                        produto_nome = r["Produto"]
                        quantidade = r["Quantidade"]
                        print(f"[OK] Produto '{produto_nome}' atualizado para quantidade {quantidade}")
                        break
            else:
                produto_nome = input("Digite o nome do novo produto: ")
                novo_id = len(registros) + 1
                quantidade = "1"
                registros.append({
                    "ID": str(novo_id),
                    "Produto": produto_nome,
                    "QRCode": qr_code,
                    "Quantidade": quantidade
                })
                print(f"[OK] Produto '{produto_nome}' cadastrado com ID {novo_id}, QR {qr_code}, Quantidade = 1")

            salvar_registros(registros)
            return produto_nome, quantidade, False  # False = não sair

        elif escolha == "2":
            print("Encerrando o programa...")
            return produto_nome, quantidade, True  # True = sair do programa
        else:
            print("Opção inválida, tente novamente.")



# LER O QR CODE

cap = cv2.VideoCapture(0)  # 0 = câmera padrão



# INICIAR O PROGRAMA:

while True:

    ret, frame = cap.read()     # lê cada frame da câmera
    if not ret:
        break

    qr_detectados = decode(frame)       # busca qr codes dentro da imagem
    qr_atual_frame = set()      # qr codes presentes neste frame

    # para cada qr code encontrado
    for qr in qr_detectados:
        dados = qr.data.decode("utf-8")     # ele converte o qr code para um código em texto
        qr_atual_frame.add(dados)

        # processa apenas se o QR não estava visível no frame anterior
        if dados not in qrs_na_tela:
            registros = carregar_registros()
            produto_existente = next((r for r in registros if r["QRCode"] == dados), None)

            # delay antes de abrir o menu
            time.sleep(1)

            if produto_existente:
                produto, qtd, sair_programa = menu_interativo(
                    dados, True, produto_existente["Produto"], produto_existente["Quantidade"]
                )
            else:
                produto, qtd, sair_programa = menu_interativo(dados, False)

            if sair_programa:
                cap.release()
                cv2.destroyAllWindows()
                exit()

        else:
            # qr já processado no frame anterior, só desenha
            x, y, w, h = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
            r = carregar_registros()
            produto = next((reg["Produto"] for reg in r if reg["QRCode"] == dados), "")
            qtd = next((reg["Quantidade"] for reg in r if reg["QRCode"] == dados), "")
            texto = f"{produto} (Qtd: {qtd})"
            cv2.putText(frame, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 0), 2)

    # atualiza os QR codes visíveis na tela
    qrs_na_tela = qr_atual_frame

    # abre uma janela com a câmera para ler os qr codes
    cv2.imshow("Leitor QR Code", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
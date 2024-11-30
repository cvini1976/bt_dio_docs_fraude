import streamlit as st
import os
from services.blob_services import upload_blob
from services.credit_card_service import analize_credit_card
def config_inteface():
    st.title("Upload do arquivo DIO - Desafio 1 - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo",type=["png", "jpg", " jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Enviar para o blob storage
        blob_storage = upload_blob(uploaded_file, fileName)
        if blob_storage:
            st.write(f"Arquivo carregado: {fileName} com sucesso no Blob Storage!!!")
            credit_card_info = analize_credit_card(blob_storage) #Chamar a funcao de deteccao de informacoes de cartao de credito.
            show_image_and_validation(blob_storage, credit_card_info)
        else:
            st.write(f"Arquivo carregado: {fileName} com sucesso, mas não foi possível enviar para o Blob Storage.")
            credit_card_info = "" #Chamar a funcao de deteccao de informacoes de cartao de credito.

def show_image_and_validation(blob_storage, credit_card_info):
    # Mostrar a imagem
    st.image(blob_storage, caption="Imagem enviada", use_column_width=True)

    # Validar o arquivo
    # Implementar a validacao do arquivo com as regras de deteccao de fraude

    # Exibir o resultado da validacao
    st.write("Resultado da validacao do arquivo:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green'>Credit Card Validation</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de validacao: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red'>Credit Card Validation</h1>", unsafe_allow_html=True)
        st.write("Nenhum cartao encontrado.")

    # Mostrar o resultado da validacao
    st.write("Resultado da validacao do cartao encontradas:")
    
    st.write(credit_card_info)

if __name__ == "__main__":
    config_inteface()
import streamlit as st

def main():
    st.title("Abrir Chat do WhatsApp")
    st.write("Insira o número com DDD (ex: 5511999999999) e clique no botão para abrir a conversa:")

    # Campo de entrada de texto para o número
    numero_completo = st.text_input("Número completo", value="5511999999999")

    # Quando clica no botão, monta o link e exibe
    if st.button("Abrir WhatsApp"):
        link_whatsapp = f"https://wa.me/{numero_completo}"
        st.markdown(f"[Clique aqui para iniciar o chat]({link_whatsapp})")

if __name__ == "__main__":
    main()

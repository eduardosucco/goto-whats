import streamlit as st
from urllib.parse import quote

def main():
    st.title("Abrir Conversa no WhatsApp")

    numero = st.text_input("Digite o número completo", "21981664493")
    mensagem = st.text_input("Mensagem (opcional)", "Olá, tudo bem?")
    
    if st.button("Gerar link"):
        # Codifica a mensagem para ficar no formato URL (espacos viram %20 etc.)
        msg_codificada = quote(mensagem)
        link_whatsapp = f"https://wa.me/55{numero}?text={msg_codificada}"

        # Ao invés de meta refresh, simplesmente exiba o link
        st.markdown(f"**Clique para abrir:** [Abrir WhatsApp]({link_whatsapp})")

if __name__ == "__main__":
    main()

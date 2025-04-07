import streamlit as st

def main():
    st.title("Abrir Chat do WhatsApp")
    st.write("Insira o número com DDD (ex: 5511999999999) e clique no botão para abrir a conversa:")

    numero_completo = st.text_input("Número completo", value="11999999999")

    if st.button("Abrir WhatsApp"):
        link_whatsapp = f"https://wa.me/55{numero_completo}"
        # Injetamos um JavaScript que faz redirecionamento imediato
        js_redirect = f"""
        <script>
        window.location.href = "{link_whatsapp}";
        </script>
        """
        st.markdown(js_redirect, unsafe_allow_html=True)
        st.write("Abrindo WhatsApp...")

if __name__ == "__main__":
    main()

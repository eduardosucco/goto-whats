import streamlit as st

def main():
    st.title("Abrir Conversa no WhatsApp (via Meta Refresh)")
    st.write("Digite o número (exemplo: 5511999999999) e clique em abrir.")

    numero = st.text_input("Número completo (com DDD)", "11999999999")

    if st.button("Abrir WhatsApp"):
        st.write("Tentando abrir WhatsApp via meta refresh…")
        link_whatsapp = f"https://wa.me/55{numero}"
        meta_tag = f'<meta http-equiv="refresh" content="0; url={link_whatsapp}"/>'
        st.markdown(meta_tag, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

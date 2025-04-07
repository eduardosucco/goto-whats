import streamlit as st

def main():
    st.title("Abrir Chat do WhatsApp (meta refresh)")

    numero = st.text_input("Número completo", "5511999999999")

    if st.button("Abrir WhatsApp"):
        st.write("Tentando abrir WhatsApp via meta refresh…")
        link_whatsapp = f"https://wa.me/{numero}"
        meta_tag = f'<meta http-equiv="refresh" content="0; url={link_whatsapp}"/>'
        st.markdown(meta_tag, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

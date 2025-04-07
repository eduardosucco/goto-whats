import streamlit as st

def main():
    st.title("Abrir Chat do WhatsApp")
    st.write("Clique no botão para abrir a conversa no WhatsApp.")

    # Exemplo de número fictício
    numero_completo = "5511999999999"  # +55 11 99999-9999
    link_whatsapp = f"https://wa.me/{numero_completo}"

    if st.button("Abrir WhatsApp"):
        # Quando o botão for clicado, mostra um link clicável na interface.
        # Em um ambiente mobile, ao clicar nesse link, vai abrir direto o app do WhatsApp.
        st.markdown(f"[Clique aqui para iniciar o chat]({link_whatsapp})")

if __name__ == "__main__":
    main()

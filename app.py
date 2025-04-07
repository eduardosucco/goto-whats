import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Abrir Chat do WhatsApp (tentando redirecionar automático)")
    numero = st.text_input("Número completo (com DDD, ex: 5511999999999)", "5511999999999")

    if st.button("Abrir WhatsApp agora!"):
        link_whatsapp = f"https://wa.me/{numero}"
        # O JS abaixo abre o link na mesma aba (_self).  
        # Se preferir outra aba, troque '_blank'.
        js_code = f"""
        <script>
            window.open('{link_whatsapp}', '_self');
        </script>
        """
        # Mostra mensagem e injeta o JS:
        st.write("Tentando abrir WhatsApp...")
        components.html(js_code, height=0)

if __name__ == "__main__":
    main()

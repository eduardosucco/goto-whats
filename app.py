import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Abrir Chat do WhatsApp (função declarada antes)")

    # Declaramos a função JavaScript
    st.markdown("""
    <script>
      function abrirWhatsAppAgora(numero) {
          const link = "https://wa.me/" + numero;
          window.open(link, "_self");
      }
    </script>
    """, unsafe_allow_html=True)

    numero = st.text_input("Número completo", "5511999999999")

    if st.button("Abrir WhatsApp"):
        st.write("Tentando abrir WhatsApp...")
        call_js = f"<script>abrirWhatsAppAgora('{numero}');</script>"
        components.html(call_js, height=0)

if __name__ == "__main__":
    main()

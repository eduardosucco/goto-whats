import streamlit as st
import streamlit.components.v1 as components

def main():
    numero = st.text_input("Número completo", "21981664493")

    if st.button("Abrir WhatsApp agora!"):
        link_whatsapp = f"https://wa.me/55{numero}"
        js_code = f"""
        <script>
            window.open('{link_whatsapp}', '_self');
        </script>
        """
        st.write("Tentando abrir WhatsApp...")
        components.html(js_code, height=0)

if __name__ == "__main__":
    main()

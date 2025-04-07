import streamlit as st

def main():
    st.title("Abrir Chat do WhatsApp")
    st.write("Insira o número com DDD (ex: 5511999999999) e clique no botão para abrir a conversa:")

    # 1) Primeiro: Defina o script que faz o redirecionamento
    st.markdown("""
    <script>
      function abrirWhatsApp() {
          var numero = document.getElementById("numero_wa").value;
          var url = "https://wa.me/55" + numero;
          window.location.href = url; // Faz o redirecionamento
      }
    </script>
    """, unsafe_allow_html=True)

    # 2) Criar o input que terá ID "numero_wa" para usar dentro do JS
    numero = st.text_input("Número completo", value="11999999999", key="numero_wa")

    # 3) Quando clica no botão, chamamos a função do passo 1
    if st.button("Abrir WhatsApp"):
        # Mensagem temporária
        st.write("Tentando abrir o WhatsApp...")
        # Chama a função via JS
        st.markdown("<script>abrirWhatsApp();</script>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

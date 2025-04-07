import time
import streamlit as st
from urllib.parse import quote

def main():
    start_time = time.time()

    # Título do App
    st.title("Abrir Conversa no WhatsApp")

    st.write("""
    Este exemplo gera um link para abrir uma conversa no WhatsApp.
    - Insira seu número (apenas dígitos, sem '+', parênteses ou hífen).
    - Você pode limitar a quantidade de caracteres no 'text_input' para evitar inputs maiores que o esperado.
    """)

    # Número de telefone (máx. 13 dígitos, por ex.: 55 + DDD + número)
    numero = st.text_input("Digite o número completo (somente dígitos):", 
                           value="5511999999999", 
                           max_chars=13)

    # Mensagem opcional (máx. 140 caracteres, exemplo de limite)
    mensagem = st.text_input("Mensagem (opcional):", 
                             value="Olá, tudo bem?", 
                             max_chars=140)

    # Botão para gerar o link
    if st.button("Gerar link"):
        # Codifica a mensagem para formato URL
        msg_codificada = quote(mensagem)

        # Monta o link oficial "wa.me" (WhatsApp)
        link_whatsapp = f"https://wa.me/{numero}?text={msg_codificada}"

        # Em vez de tentar abrir automaticamente (o que pode ser bloqueado),
        # exibimos o link para que o usuário possa clicar.
        st.markdown(f"**Clique para abrir no WhatsApp:** [Abrir WhatsApp]({link_whatsapp})")
        st.write("Se você estiver no celular, ao clicar deve abrir o app do WhatsApp. "
                 "No desktop, abrirá o WhatsApp Web ou pedirá para abrir o aplicativo do WhatsApp.")

    # Mostra o tempo total de execução
    end_time = time.time()
    tempo_exec = end_time - start_time
    st.write(f"Tempo total de execução: {tempo_exec:.2f} segundos")

    st.write("""
    **Dica**: Para evitar que a tela recarregue a cada caractere digitado, 
    vá em **Settings (ícone de engrenagem) > Rerun on...** e selecione 
    **Only when I press the button** ou algo similar, dependendo da versão do Streamlit.
    """)

if __name__ == "__main__":
    # Antes de rodar, garanta que o Streamlit esteja instalado/atualizado:
    # pip install --upgrade streamlit
    st.set_page_config(page_title="WhatsApp Link Generator", layout="centered")
    main()

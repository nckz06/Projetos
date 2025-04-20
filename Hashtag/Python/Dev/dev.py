# PASSO 0 - Importar o FLET
import flet as ft

def main(pagina):

# PASSO 1 - Título do Chat
    titulo = ft.Text("NickChat")
    usuario = ft.TextField(label="Escreva seu nome")
    
    chat = ft.Column()

    def msg_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(msg_tunel)
    
    def enviar(evento):
        txt_msg = f"{usuario.value}: {campo_msg.value}"
        pagina.pubsub.send_all(txt_msg)
        campo_msg.value = ""
        pagina.update()

    campo_msg = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar)
    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar)
    
    def entrar(evento):
        popup.open = False
        pagina.remove(btn_iniciar)
        pagina.add(chat)
        linha_msg = ft.Row([campo_msg, btn_enviar])
        pagina.add(linha_msg)
        entrou = f"{usuario.value} entrou no chat"
        pagina.pubsub.send_all(entrou)
        pagina.update()
    
    # PopUp
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem-vindo ao NickChat!"),
        content=usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar)]
        )

# PASSO 2 - Botão para o Chat
    def iniciar(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    btn_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar)



# PASSO 3 - Chat
    # Pessoa entrou no chat
    # Mensagens do Usuário


# PASSO 4 - Caixa de Texto


# PASSO 5 - Botão de Enviar


    pagina.add(titulo)
    pagina.add(btn_iniciar)

ft.app(main, view=ft.WEB_BROWSER)
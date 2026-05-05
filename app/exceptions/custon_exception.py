class ErroCustomizado(Exception):
    
    def __init__(self, mensagem: str):
        super().__init__(mensagem)
        self.mensagem = mensagem

    def getter_mensagem(self) -> str:
        return self.mensagem

    def setter_mensagem(self, mensagem: str) -> None:
        self.mensagem = mensagem
# Estudos de Programação Orientada a Objetos em Python  

Este repositório tem como objetivo documentar meus estudos em POO.  

## 1. Encapsulamento  
[Exemplo de código](https://github.com/GuisLima/Estudo_POO/blob/main/encapsulamento/exemplo1.py)  

Inicialmente, tive bastante dificuldade para entender como aplicar e manipular as propriedades (`@property`), respeitando o conceito de encapsulamento. Com a ajuda da IA (ChatGPT e Deepseek), fui esclarecendo algumas dúvidas importantes:  

### a) Encapsular ou não um atributo de descrição?  
Tinha um atributo de descrição que podia ser alterado a qualquer momento e me perguntei: *seria válido não encapsulá-lo?*  

- A resposta foi **não**. Entendi que encapsular é importante para garantir a reutilização do código e permitir futuras validações, mesmo para atributos aparentemente simples.  
- Durante meus estudos na DIO, o professor Guilherme mencionou: *"Durante as validações, é aí que a `property` brilha"*. Depois da prática, consegui compreender essa ideia na prática.  

### b) Encapsulamento ao instanciar objetos  
Outra dúvida que surgiu foi: *se eu defini construtores na classe, atribuir valores diretamente ao instanciar um objeto quebraria o encapsulamento?*  

- Descobri que definir **valores padrão** no construtor, como `valor=0` e `'Sem Descrição'`, permite instanciar corretamente o objeto sem quebrar o encapsulamento.  
- Depois, os valores podem ser modificados com os *setters*, garantindo que as regras de encapsulamento sejam respeitadas.  

# Conclusão do Estudo: 
- Compreendi que o encapsulamento é essencial para escrever um código mais organizado e sustentável. Ele garante a integridade dos dados e facilita a manutenção. Ao utilizar setters, posso aplicar validações e regras de negócio, tornando o código mais seguro.
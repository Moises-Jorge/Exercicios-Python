 A composição acontece quando uma classe contém outra classe como um atributo, e essa dependência é tão forte que, se a classe externa for destruída, a interna também será.

Exemplo: Um Carro é composto por um Motor. Se o carro deixar de existir, o motor também não faz mais sentido.

Explicação:
O Carro tem um Motor como atributo.
O Motor não existe fora do Carro — é criado diretamente dentro dele.
Se o Carro for destruído, o Motor também será.



A agregação também é uma relação "tem-um", mas neste caso, o objeto agregado pode existir separadamente da classe principal.

Exemplo: Uma Escola pode ter vários Professores, mas os professores podem existir sem a escola.

Explicação:
A Escola tem uma lista de Professores.
Os Professores podem existir fora da Escola e serem usados separadamente.
Se a Escola for destruída, os professores ainda existirão.


 
 Diferença entre Composição e Agregação

Característica |	Composição |	Agregação
Dependência	   |    Um objeto depende do outro para existir |	Os objetos podem existir separadamente
Criação        | 	O objeto interno é criado dentro da classe principal  |	O objeto é passado como parâmetro
Exemplo	       |  Um Carro tem um Motor	|  Uma Escola tem Professores


Vantagens da Composição/Agregação
✅ Modularidade – Cada classe tem uma única responsabilidade.
✅ Reutilização – Podemos usar a classe Motor em Barco, Moto, etc.
✅ Facilidade de manutenção – Podemos modificar Motor sem mudar Carro.


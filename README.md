## Objetivo:
* Desenvolvimento de uma solução para Gestão e Controle Financeiro e das
atividades das empresas de consultoria.
## Vantagens:
* Automatização do processo de marcação das horas;
* Consolidação automática e diária das horas de toda a empresa;
* Geração de relatórios e consultas em diversos níveis;
* Indicadores e gráficos para análises
* Eliminação de processo manual realizado em pastas de Excel;
Plataforma:
Intranet
Itens chaves:
Usabilidade / Acessibilidade / Funcionalidade

Escopo do sistema / Visão geral:
O Sistema será sincronizado com integração entre seus módulos.
Como segue:
## 5o Módulo: Funcionários
* Cada funcionário irá acessar o sistema através de senha pessoal e intransferível;
* Para esse módulo, imagino uma tela além dos campos Nome e Departamento do
Funcionário, mais os seguintes campos:

### 1 Horário de inicio: (preenchimento automaticamente) pelo botão
(Iniciar);
### 2 Nome de Projeto: (preenchimento por lista de opções); Os nomes
dos Projetos serão cadastrados pelos coordenadores. Mais
informação abaixo no módulo Coordenador.
### 3 Tipo de Atividade: (preenchimento por lista de opções); Os
nomes das Atividades serão incluídas pelos coordenadores. Mais
informação abaixo no módulo Coordenador.
### 4 Horário Fim: (preenchimento automaticamente) pelos botões
(Pausar) ou (Parar/Interromper);

* Apenas para ilustrar:
### Momento 1: Chegando pela manhã, o funcionário vai até sua pagina no botão
(Inicio); Em seguida, no campo Atividade escolhe a atividade a ser executada;
### Momento 2: Após 1 hora, decide pausar a atividade botão (Pausar). Esta opção
de botão mantém a mesma atividade em execução, porém, precisou pausar
apenas.

### Momento 3: Após 3 horas, o funcionário foi para uma reunião em outro
departamento, ele clicou no botão (Parar/Interromper). Antes de ir, ele poderá
abrir uma nova linha de registro com a atividade (Reunião) ou deixar para
registrar quando voltar dela.
Em resumo, o funcionário utilizará sempre os três botões (Iniciar, Pausar e
Parar/Interromper).
* Outra característica prevista são os horários oficiais. Aqueles definidos pela
empresa, exemplo, horário de entrada para inicio das atividades e o horário de
fim de expediente.
* Outro exemplo, apenas para ilustrar:
Chegando à empresa, agora após horário oficial de entrada. Ao abrir o sistema,
automaticamente abrirá uma linha com a hora inicio preenchida
automaticamente (hora oficial de entrada) aguardando o preenchimento da
atividade realizada nesse período. Ou seja, o funcionário deverá registrar a
atividade / projeto realizado nesse intervalo. Caso nenhuma atividade foi
realizada será interpretado como atraso e registrado no banco de horas do
funcionário;
Um funcionário que foi direto para um cliente. Após 2 horas do horário oficial
de entrada ele acessa o sistema. Novamente, o sistema de forma
automaticamente indicará o horário inicio com a hora oficial de entrada. Uma
atividade e projeto deverão ser preenchidos pelo funcionário. Por fim, o horário
fim será preenchido automaticamente com o mesmo horário que o sistema foi
aberto. Nesse caso, o funcionário deverá ser como atividade a opção (Transito
para Cliente). E na segunda linha, por exemplo, Reunião com cliente.
Por fim, para concluir essa parte de hipóteses, temos a hora de almoço.
Antes de almoçar, o funcionário deverá clicar no botão (Parar/Interromper) a
atividade em execução e sair para o almoço. Nesse momento o sistema passa a
contar como inicio do almoço esse horário.
Ao voltar, o funcionário deverá clicar no botão (Termino/Interromper)
automaticamente o sistema definirá esse horário como fim da atividade
(Almoço).
Caso o funcionário exceda ao horário definido pela empresa (exemplo 1 hora), o
tempo em excesso será lançado como Débito para o funcionário em um controle
que a principio será chamado de “Controle Saldos de horários”. Similar a um
Extrato Bancário com Débitos e Créditos.
Importante: “Controle Saldos de horários” valerá para os casos de Entrada, Hora
de Almoço e Saída. Este controle será por dia e ficará disponível para o
funcionário, seu gestor e módulo RH.

## 4o Módulo: Coordenadores
* Cada Coordenador terá sua página no sistema;
* O acesso será por meio de senha pessoal e intransferível;
* Nela, terá visão dos registros realizados pelos funcionários sob sua coordenação;
* Após alinhamento com os Diretores, cada coordenador registrará essas
atividades em sua pagina que serão redistribuídas a seus subordinados;
* O coordenador poderá realizar o cadastramento de novos projetos, alterações,
inclusões das atividades e indicação do funcionário(s) alocado(s) em cada
projeto. Também indicará as horas contratadas em cada projeto.
* Acompanhamento diário das horas contratadas x realizadas/registradas;
* Acompanhamento por meio de gráficos e indicadores.
* Visão pelo departamento, por projeto, por funcionário, por atividade;
* Visão pelo projeto mais critico em termos de hora, pelo projeto mais bem
sucedido, enfim, terá consultas para uma melhor gestão;
* Uma visão coordenada de toda sua área.

## 3o Módulo: Departamento de RH
Principais vantagens:
* Extinção do processo manual de consolidação de horas. Já que os registros de
toda empresa será on-line e consolidado ao final de cada dia;
Podemos pensar em um módulo ou ficha consolidada para esse módulo;
* Controle on-line do Banco de Horas e acompanhamento desses saldos por
funcionário. Podendo gerar consultas pelos critérios: maiores saldos positivos e
negativos entre outros;
* Consulta das horas em diversos níveis: consolidada pela empresa, cliente,
departamento, funcionário, projetos e atividades;
* Enfim, a área de RH terá uma visão coordenada de todas as áreas da empresa,
possibilitando a tomada de decisão e soluções antecipadas.
## 2o Módulo: FINANCEIRO
Principais vantagens:
* Maior controle das horas a serem faturadas. Nesse módulo, a pessoa da área
financeira terá uma visão clara e objetiva das horas liberadas para faturamento
(por cliente, projeto, atividade).
* Após validação dos Diretores ou Coordenadores essas horas serão
disponibilizadas em um extrato visualizado somente pela área financeira;
* Após emissão da Nota Fiscal, a pessoa do financeiro, voltará ao sistema e
confirmará a emissão da nota clicando no campo (confirmação do faturamento)
em um campo disponível digitará o número da Nota Fiscal.

* A vantagem é que a comunicação entre os diretores e a área financeira será on-
line dentro do mesmo sistema, evitando desencontros de informações.

## 1o Módulo: Diretores
* Para este nível, o sistema reserva importantes funções e funcionalidades
importantes nas tomadas de decisões;
* Controle e gestão das informações financeiras da empresa, como exemplo,
custos e margem de lucro apurado em cada projeto, seja em execução ou aqueles
ainda em negociação;
* Consulta histórico dos custos/preços médios por cliente ou por projeto/atividade,
facilitando a elaboração de novas propostas.
Outros relatórios e consultas:
* Análise da evolução das horas contratadas;
* Análise da rentabilidade;
* Consulta dos projetos concluídos;
* Consulta das horas autorizadas para faturamento;
* Consulta das horas a serem faturadas;
* Todas realizadas por cliente, departamento, projeto ou atividade;
* A inclusão dos custos/preços e outras informações financeiras poderão ser
imputadas pelos próprios diretores ou seus coordenadores;
* Controle e acompanhamento dos projetos sob controle dos gestores;
* Troca de informações dentro do próprio sistema com qualquer pessoa pela
função (fast track). disponível somente neste nível.

======
TheZoo é um projeto criado para tornar a possibilidade de análise de malware aberta e disponível ao público. Uma vez que descobrimos que quase todas as versões de malware são muito difíceis de obter de uma forma que permita a análise, decidimos reunir todas elas para você de uma forma acessível e segura.
O zoo nasceu por Yuval tisf Nativ e agora é mantido por Shahak Shalev.

** theZoo é aberto e acolhedor visitantes! **
aviso Legal
==========
O objetivo do theZoo é permitir o estudo de malware e permitir que as pessoas interessadas em análise de malware (ou talvez como parte de seu trabalho) tenham acesso a malware ao vivo, analisem as maneiras como operam e talvez até habilitem pessoas avançadas e experientes Para bloquear malware específico dentro de seu próprio ambiente.

** Lembre-se que estes são malware vivo e perigoso! Eles vêm criptografados e bloqueados por uma razão! Não executá-los a menos que você esteja absolutamente certo do que você está fazendo! Eles devem ser usados ​​apenas para fins educacionais (e nós queremos dizer que!)! **

Recomendamos executá-los em uma VM que não tenha conexão à Internet (ou uma rede virtual interna, se for necessário) e sem adições de convidados ou quaisquer equivalentes. Alguns deles são vermes e automaticamente tentam se espalhar. Executá-los sem restrições significa que você vai infectar você mesmo ou outros com malware vicioso e perigoso! **


GPL 3
======
TheZoo - a mais incrível base de dados gratuita de malware no ar
Direitos autorais (C) 2015, Yuval Nativ, Lahad Ludar, 5fingers

Este programa é software livre: você pode redistribuí-lo e / ou modificar
Sob os termos da Licença Pública Geral GNU publicada pela
A Free Software Foundation, quer a versão 3 da Licença, quer
(À sua escolha) qualquer versão posterior.

Este programa é distribuído na esperança de que seja útil,
Mas SEM NENHUMA GARANTIA; Sem a garantia implícita de
COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
GNU General Public License para mais detalhes.

Você deve ter recebido uma cópia da GNU General Public License
Juntamente com este programa. Caso contrário, consulte <http://www.gnu.org/licenses/>.


Documentação e Notas
========================

## Fundo:
O objetivo do theZoo é oferecer uma maneira rápida e fácil de recuperar amostras de malware e código-fonte de forma organizada na esperança de promover a pesquisa de malware.

## Root Files:
Desde a versão 0.42, o Zoo tem sofrido mudanças dramáticas. Agora ele é executado nos modos CLI e ARGVS. Você pode chamar o programa com os mesmos argumentos de linha de comando como antes.
O estado padrão atual do runtime do Zoo é o CLI. Os seguintes arquivos e diretórios são responsáveis ​​pelo comportamento do aplicativo.

Conf
A pasta conf contém arquivos relevantes para a execução específica do programa, mas não fazem parte do aplicativo. Você pode encontrar o arquivo EULA no conf e muito mais.
### / imports
Contém arquivos de importação .py e .pyc usados ​​pelo resto do aplicativo
### / malwares / Binários
As amostras de malwares reais - tenha cuidado!
### / malware / Source
Código fonte de malware :)


## Estrutura do Diretório:
Cada diretório é composto de 4 arquivos:
- Arquivos de malware em um arquivo ZIP criptografado.
- SHA256 soma do primeiro arquivo.
- MD5 soma do primeiro arquivo.
- Arquivo de senha para o arquivo.



## Estrutura de maldb.db
Maldb.db é o DB que theZoo está agindo para encontrar malware indexado em sua unidade.
A estrutura é a seguinte:

Uid, localização, tipo, nome, versão, autor, idioma, data, arquitetura, plataforma, comentários, tags

- UID - Determinado com base no processo de indexação.
- Localização - A localização na unidade do malware que você procurou.
- Tipo - Classifica os diferentes tipos de malware que existem. Até agora nós classificamos por: Vírus, Trojans, Botnets, Ransomware, Spyware
- Nome - Apenas o nome do malware.
- Versão - Nada a dizer aqui também.
- Autor - ... Eu não sou isso em documentação ...
- Linguagem de Programação - O estado do malware em relação à fonte, bin, ou qual tipo de fonte. C / cpp / bin ...
- Data - Veja a seção 'Autor'.
- Arquitetura - O arco da plataforma foi construído para. Pode ser x86, x64, arm7 ....
- Plataforma - Win32, Win64, * nix32, * nix64, iOS, android e assim por diante.
- Comentários - Qualquer comentário pode ser sobre o item.
- Tags - Tags correspondentes ao item.

Uma linha de exemplo será exibida da seguinte forma:

    104, Fonte / Original / Dexter, trojan, Dexter, 2, desconhecido, c, 00/05/2013, x86, win32, NULL, Source

Bugs e Relatórios
=================
O repositório que contém todos os arquivos está
Https://github.com/ytisf/theZoo

## Log de Mudança para v0.60:
- [x] Mover DB para SQLite3.
- [x] Procurando uma revisão para uma moda freestyle.
- [x] Corrigido o comando "get".
- [x] Mais e mais malwares.

## Registro de alterações para v0.50:
- [x] UI melhor e mais fácil.
- [x] Impressão alinhada de malwares.
- [x] Os argumentos da linha de comando estão funcionando.
- [x] Adicionado 10 malwares mais (cool ones) para o DB.

## Registro de alterações para v0.42:
- [x] Corrija o EULA para obter a renúncia adequada.
- [x] Pesquisa mais precisa e indexação incluindo plataforma e muito mais.
- [x] Adicionado 10 novos malwares.
- [x] Git atualização de plataforma e novos malwares.
- [x] Corrigir a exibição da pesquisa.
- [x] Ativar suporte para plataforma e arquitetura na indexação.
- [x] Separar entre banco de dados e aplicativo.
- [x] melhorias na interface do usuário.

## Registro de alterações para v0.43:
- [X] Verifique se o argv está funcionando corretamente. (Correções em v0.5)
- [X] Virus-Total upload e indexação módulo. - Não é possível devido a restrições de VT.
- [X] Sistema de relatório automático para malwares que não são indexados na estrutura.

## Registro de alterações para v0.50:
- [X] Pacote de análise de malware foi removido para reduzir o tamanho do clone.
- [X] Mais documentação foi adicionada.
- [X] Removido a função de depuração que estavam mortos no código.

## Log de Mudanças Previsíveis para v1.0
- [X] Corrigir o preenchimento automático de estruturas de malware. (Graças a 5fingers)
- [X] Considere mudar DB para XML ou SQLite3. (Sheksa - feito :))
- [] Mover malwares para outro repo.
- [] Melhor UI recursos.

Se você tiver alguma sugestão ou malware que você tenha indexado (da maneira descrita na documentação), por favor, envie para nós - yuval [] morirt [dot] com - para que possamos adicioná-lo para todos os prazeres.
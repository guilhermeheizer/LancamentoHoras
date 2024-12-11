
# ChatGT vs Python  
Nós desenvolvedores estamos utilizando a Inteligência Artificial a nosso favor no dia-a-dia do nosso trabalho com o ojetivo de o melhorar trechos de códigos, adaptar o código para as regras do SonarLint, preparar testes unitários para sistemas construídos em Python, C#, Java e outras linguagens.

Então, preparei uma explicação para que o ChatGT 3.0 construa uma aplicação desktop para lançamento de horas de estudo ou trabalho que faça inserção dos dados num banco de dados MySQL.

Segue a explicação da aplicação que inseri no ChatGT:

Criar um sistema em Pyton 3.9 utilizando a biblioteca Tkinter para lançamento de horas de estudo como o nome 'Lanca Horas'

O banco de dados será o MySql e o database de nome "horas". Segue abaixo o schema do banco "horas" com as tabelas: atividade, pessoa e horaslancadas.

use horas;

CREATE TABLE `atividade` (
  `atividade` varchar(5) NOT NULL,
  `atividade_nome` varchar(80) DEFAULT NULL,
  `atividade_tipo` char(1) NOT NULL,
  `atividade_descricao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`atividade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `pessoa` (
  `idPessoa` int NOT NULL,
  `pessoa_nome` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPessoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `horaslancadas` (
  `hrlancto_data` date NOT NULL,
  `hrlancto_hr_inicio` time NOT NULL,
  `hrlancto_hr_fim` time DEFAULT NULL,
  `hrlancto_detalhe` varchar(300) DEFAULT NULL,
  `Pessoa_idPessoa` int NOT NULL,
  `Atividade_atividade` varchar(5) NOT NULL,
  PRIMARY KEY (`Pessoa_idPessoa`,`Atividade_atividade`,`hrlancto_data`,`hrlancto_hr_inicio`),
  KEY `fk_HorasLancadas_Atividade1` (`Atividade_atividade`),
  CONSTRAINT `fk_HorasLancadas_Atividade1` FOREIGN KEY (`Atividade_atividade`) REFERENCES `atividade` (`atividade`),
  CONSTRAINT `fk_HorasLancadas_Pessoa` FOREIGN KEY (`Pessoa_idPessoa`) REFERENCES `pessoa` (`idPessoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

O sistema em Python deverá possuir uma tela com as opções de Menu:
- Cadastrar Pessoa
- Cadastrar Atividade
- Lançar horas

A opção do menu 'Cadastrar Pessoa' vai acessar a tabela 'Pessoa' e deve possibilitar realizar consultas, inserts, update e delate na tabela 'Pessoa'.

A opção do menu 'Cadastrar Atividade' vai acessar a tabela 'Atividade' e deve possibilitar realizar consultas, inserts, update e delate na tabela 'Atividade'.

A opção do menu 'Lançar horas vai acessar a tabela 'horaslancadas' e deve possibilitar realizar consultas, inserts, update e delate na tabela 'horaslancadas'.

Executei a aplicação através do VS Code.
É necessário rodar: pip install mysql-connector-python

```
O projeto esta disponível no github: https://github.com/guilhermeheizer/LancamentoHoras

```


## Autor

- [@guilhermeheizer](https://www.github.com/guilhermeheizer)


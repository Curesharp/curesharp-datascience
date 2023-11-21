# Data Science Lab
Neste laboratório, estão armazenados os datasets, a análise estatística exploratória das bases de dados, gráficos informativos e os modelos preditivos de inteligência artificial. A API em Flask integra os modelos de inteligência artificial a aplicação da Cure Sharp. No notebook, estão mais detalhadas as motivações do grupo e a implementação da solução.

<h2>Servidor Flask</h2>

  - Abaixo estão as instalações necessárias para rodar a aplicação. O Flask roda por padrão na porta 5000.

```sh
$ pip install -U scikit-learn scipy matplotlib
$ pip install -U scikit-learn==1.2.2
$ pip install -U pickle
```

> Para importar os modelos, é necessário criar um arquivo de texto 'paths.txt' com um dicionário com os caminhos dos arquivos dos modelos preditivos materno e fetal nas chaves 'maternal' e 'fetal'.

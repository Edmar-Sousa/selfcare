# selfcare

## Sobre o projeto
selfcare é um projeto de um ecommerce, full-stack, inspirado no projeto front-end do devchallenge,
neste sistema é possivel registrar-se, registrar produtos, buscar produtos e ver os detalhes. O principal
objetivo deste projeto é praticar os principais conceitos do framework web, Django, como authenticate, models, 
view, urls e entre outros.

## Design do projeto
![index](https://github.com/Edmar-Sousa/selfcare/blob/master/gitimage/index.png)

![search](https://github.com/Edmar-Sousa/selfcare/blob/master/gitimage/search-products.png)

![profile](https://github.com/Edmar-Sousa/selfcare/blob/master/gitimage/profile.png)

![details](https://github.com/Edmar-Sousa/selfcare/blob/master/gitimage/product-details.png)

## Tecnologias usadas

### Back-end
- Python
- Django

### Front-end
- HTML
- CSS
- JavaScript

## Como executar o projeto
```bash
  # Crie um ambiente virtual com virtual env e ative o ambiente virtual, no windows o seguite comando
  python -m venv selfcare
  cd selfcare
  
  # ativando o ambiente virtual
  cd Scripts && activate
  cd ..
  
  # instalar o Django e o pillow
  pip install django
  pip install pillow
  
  # a estrutura do projeto deve algo como
  # selfcare
  #    - Include
  #    - Lib
  #    - Scripts
  
  # crie um diretorio para o codigo
  mkdir src
  
  # clone o projeto dentro da pasta src
  git clone https://github.com/Edmar-Sousa/selfcare.git
  cd selfcare
  
  # execute as migraçoes
  python manage.py makemigrations
  python manage.py migrate
  
  # execute o servidor
  python manage.py runserver

```

## Author
- Edmar Sousa. <br><br>
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/edmar-sousa-9666b0201/)
[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Edmar-Sousa)

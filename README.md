IBGE Data Extraction and Email Automation
Introduction
This Python script is designed to automate the following processes:

Accessing the IBGE website ("https://cidades.ibge.gov.br/")
Extracting specific information from each Brazilian state, including:
Gentilic ("Gentílico")
Capital ("Capital")
Governor ("Governador")
Estimated Population ("População Estimada")
Human Development Index ("IDH")
Generating an Excel file ("*.xlsx") containing the extracted data for easy visualization in MS Excel.
Automatically sending an email containing this Excel file as an attachment.
Important Links
IBGE Website
Extracted Data
The following information is extracted for each state:

Gentilic ("Gentílico")
Capital ("Capital")
Governor ("Governador")
Estimated Population ("População Estimada")
Human Development Index ("IDH")
Code Explanation
The script utilizes Selenium for web scraping and Pandas for data manipulation. It automates the process of navigating through each state's page on the IBGE website, extracting the required information, and then saving it into an Excel file. Additionally, it sends an email with the generated Excel file as an attachment using the SMTP protocol.

Instructions
Ensure you have the necessary Python libraries installed. You can install them via pip:
Copy code
pip install pandas selenium
Make sure you have a compatible web driver for Selenium. This script is configured to use Chrome, so you will need the ChromeDriver. Download it from here and ensure it's in your system PATH.

Replace the sender's and recipient's email addresses and password in the script with your own.

Run the script. Upon execution, it will perform the designated tasks and send the email with the extracted data.

Disclaimer
Please use this script responsibly and ensure compliance with the terms of use of the IBGE website. Automated access to websites may be subject to legal restrictions or terms of service. This script is provided for educational purposes only.

---

PT-BR

Extração de dados e automação de e-mail do IBGE
Introdução
Este script Python foi projetado para automatizar os seguintes processos:

Acessando o site do IBGE (“https://cidades.ibge.gov.br/”)
Extração de informações específicas de cada estado brasileiro, incluindo:
Gentílico ("Gentílico")
Capital (“Capital”)
Governador ("Governador")
População Estimada ("População Estimada")
Índice de Desenvolvimento Humano (“IDH”)
Geração de arquivo Excel ("*.xlsx") contendo os dados extraídos para fácil visualização em MS Excel.
Envio automático de um e-mail contendo este arquivo Excel como anexo.
Links importantes
Site do IBGE
Dados extraídos
As seguintes informações são extraídas para cada estado:

Gentílico ("Gentílico")
Capital (“Capital”)
Governador ("Governador")
População Estimada ("População Estimada")
Índice de Desenvolvimento Humano (“IDH”)
Explicação do código
O script utiliza Selenium para web scraping e Pandas para manipulação de dados. Ele automatiza o processo de navegação pelas páginas de cada estado no site do IBGE, extraindo as informações necessárias e salvando-as em arquivo Excel. Além disso, envia um e-mail com o arquivo Excel gerado como anexo utilizando o protocolo SMTP.

Instruções
Certifique-se de ter as bibliotecas Python necessárias instaladas. Você pode instalá-los via pip:
Copiar código
pip instalar pandas selênio
Certifique-se de ter um driver web compatível com Selenium. Este script está configurado para usar o Chrome, então você precisará do ChromeDriver. Baixe-o aqui e certifique-se de que esteja no PATH do seu sistema.

Substitua os endereços de e-mail e a senha do remetente e do destinatário no script pelos seus próprios.

Execute o script. Após a execução, ele realizará as tarefas designadas e enviará o email com os dados extraídos.

Isenção de responsabilidade
Utilize este script com responsabilidade e garanta o cumprimento dos termos de uso do site do IBGE. O acesso automatizado a websites pode estar sujeito a restrições legais ou termos de serviço. Este script é fornecido apenas para fins educacionais.

# 🔐 STRIDE Analyzer – Detecção de Vulnerabilidades em Arquiteturas

Este projeto faz parte de um desafio de curso, onde precisei implementar uma API em **Python** utilizando **FastAPI** e **Azure OpenAI** para analisar arquiteturas de sistemas e identificar possíveis ameaças com base na metodologia **STRIDE**.

---

## 📚 O que eu aprendi

Durante o desenvolvimento, aprendi que a **segurança** deve ser pensada desde o início do projeto, e não apenas depois que o sistema já está em produção.  
A metodologia **STRIDE** ajuda justamente nisso: mapear **ameaças potenciais** em diagramas de arquitetura antes que elas se tornem falhas exploráveis.

A sigla STRIDE representa 6 categorias de ameaças:

- **S**poofing → Falsificação de identidade  
- **T**ampering → Manipulação de dados  
- **R**epudiation → Negação de ações  
- **I**nformation Disclosure → Vazamento de informações  
- **D**enial of Service → Negação de serviço  
- **E**levation of Privilege → Elevação de privilégios  

Ao aplicar essa análise em diagramas de arquitetura, conseguimos prever pontos críticos de segurança como:
- autenticação fraca,  
- dados não criptografados,  
- falhas de auditoria,  
- riscos de disponibilidade,  
- privilégios excessivos.  

---

## 🛠️ Tecnologias utilizadas

- **Python 3.11+**
- **FastAPI** → Framework para criação da API REST  
- **Uvicorn** → Servidor ASGI  
- **Azure Computer Vision** → Para extrair texto das imagens dos diagramas  
- **Azure OpenAI (Chat Completions)** → Para gerar a análise STRIDE via engenharia de prompts  
- **Docker** → (opcional) para empacotar a aplicação  

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/stride-analyzer.git
cd stride-analyzer
2. Criar ambiente virtual e instalar dependências
bash
Copiar código
python3 -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\Activate      # Windows

pip install -r requirements.txt
3. Configurar variáveis de ambiente
Copiar .env.example para .env:

bash
Copiar código
cp .env.example .env
E preencher com as chaves do Azure:

ini
Copiar código
CV_ENDPOINT=https://<seu-endpoint-computer-vision>.cognitiveservices.azure.com/
CV_KEY=<sua-chave-computer-vision>

OAI_ENDPOINT=https://<seu-resource-openai>.openai.azure.com/
OAI_KEY=<sua-chave-azure-openai>
OAI_DEPLOYMENT=<nome-do-deployment>
OAI_API_VERSION=2023-12-01-preview
4. Rodar servidor
bash
Copiar código
uvicorn app.main:app --reload
5. Testar API
Abrir no navegador:
👉 http://127.0.0.1:8000/docs

Aqui você pode enviar uma imagem com a arquitetura e receber a análise STRIDE automaticamente.

🧪 Exemplo de uso
Chamada via curl
bash
Copiar código
curl -X POST "http://127.0.0.1:8000/analyze/" \
  -F "file=@diagrama.png"
Chamada via Python
python
Copiar código
import requests

url = "http://127.0.0.1:8000/analyze/"
files = {"file": open("diagrama.png", "rb")}

response = requests.post(url, files=files)
print(response.json())
🌍 Reflexão final
Com esse projeto percebi que engenharia de segurança não é só sobre proteger sistemas prontos, mas também detectar vulnerabilidades antes mesmo do código estar em produção.
Utilizar IA (Azure OpenAI) junto com metodologias de segurança pode acelerar muito esse processo, tornando-o mais acessível e automatizado.

A segurança não é um extra: é parte essencial de qualquer arquitetura bem projetada.
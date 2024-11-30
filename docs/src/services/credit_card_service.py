from azure.core.credentials import AzureKeyCredentials
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from ultils.Config import Config

def analize_credit_card(card_url):
    try:
    # Obtendo a credencial do Azure
        credential = AzureKeyCredentials(Config.KEY)

    # Criando o cliente de análise de documentos
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    # Definindo a requisição de análise de documentos
       
        card_info = document_client.begin_analize_document("prebuilt-creditCard"), AnalyzeDocumentRequest(
                url=card_url
        )
        result = card_info.result
        for document in result.documents:
            fields = document.get('fields',{})
            return {
                'card_name': fields.get('cardHolderName',{}).get('content'),
                'card_number': fields.get('cardHolder',{}).get('content'),
                'bank_name': fields.get('IssuingBank', {}).get('content'),
                'expiry_date': fields.get('expiryDate',{}).get('content')              }
    
    except Exception as ex:
        print(f"Error ao analizar o cartão de crédito: {ex}")
        return None
    
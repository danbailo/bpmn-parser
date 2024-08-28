from legalops_commons.utils.bpmn.service_task import ServiceTask, ServiceTaskElement


def test_service_task(root):
    service_task = ServiceTask(root)
    assert service_task.list == [
        ServiceTaskElement(
            id='Activity_ConsultaDigesto',
            name='v0 - Consulta Digesto',
            execution_listeners=[],
            topic_name='consulta-digesto',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_PreTriagem',
            name='v0 - Pré-triagem',
            execution_listeners=[],
            topic_name='pre-triagem',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_OCRPreExtracao',
            name='v0 - OCR e pré-extração',
            execution_listeners=[],
            topic_name='ocr-pre-extracao',
            type='external',
        ),
        ServiceTaskElement(
            id='Activity_DefineFluxoSaida',
            name='v0 - Define fluxo saída',
            execution_listeners=[],
            topic_name='define-fluxo-saida',
            type='external',
        ),
    ]

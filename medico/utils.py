from medico.models import DadosMedico

def is_medico(user):
    '''
        Verificação se o usuário já é um médico cadastrado, se for 
        a página de cadastre-se(médico) não ira aparecer.
    '''
    return DadosMedico.objects.filter(user=user).exists()
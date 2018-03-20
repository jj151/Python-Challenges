from requests import get

cep = '64608000'

data = get('https://viacep.com.br/ws/' + cep + '/json/')
cep_info = data.json()

dado_retorno = {'tipo_logradouro': '', 'logradouro': cep_info['logradouro'], 'estado': cep_info['uf'], 'cidade':
                cep_info['localidade'], 'bairro': cep_info['bairro'], 'string_google_maps': '{}, {}, {}/{}'.
                format(cep_info['logradouro'], cep_info['bairro'], cep_info['localidade'], cep_info['uf'])}

print(dado_retorno)

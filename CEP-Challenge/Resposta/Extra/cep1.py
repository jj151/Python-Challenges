from requests import get

cep = input('Digite o seu CEP(Somente os números, sem espaços, pontos, traços ou vírgulas.): ')

data = get('https://viacep.com.br/ws/' + cep + '/json/')
cep_info = data.json()

dado_retorno = {'tipo_logradouro': '', 'logradouro': cep_info['logradouro'], 'estado': cep_info['uf'], 'cidade':
                cep_info['localidade'], 'bairro': cep_info['bairro'], 'string_google_maps': '{}, {}, {}/{}'.
                format(cep_info['logradouro'], cep_info['bairro'], cep_info['localidade'], cep_info['uf'])}

print('\n\nO CEP informado é referente ao seguinte endereço: {}.'.format(dado_retorno['string_google_maps']))

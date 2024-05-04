import os


# restaurants = ['Boi Douro', 'Pipus']

dicio_restaurants = [{'name':'Boi Douro', 'category':'Churrascaria', 'active':False},
                      {'name':'Cia Paulista', 'category':'Pizzaria', 'active':True},
                      {'name':'Laurentina', 'category':'Tipica Portuguesa', 'active':False}]

def show_title():
    print('\t𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')

def display_subtitle(text):
    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def show_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. ALternar status do restaurante')
    print('4. Sair\n')

def create_new_restaurant():    
    '''This function create a new restaurant
    
    Inputs:
    - Name of restaurant
    - Category

    Outputs:
    - Add a new restaurant in the List   
    
    
    '''
    display_subtitle('Cadastro de novos restaurantes')
    restaurant_name = input('Digite o nome do estabelecimento: ')
    category = input(f'Digite a categoria do estabelecimento {restaurant_name}: ')
    datas_of_restaurants = {'name':restaurant_name, 'category':category, 'active':False}
    dicio_restaurants.append(datas_of_restaurants)
    print(f'\nO restaurante {restaurant_name} foi adicionado com sucesso!\n')

    back_to_main_menu()

def list_of_restaurant():    
    display_subtitle('Listando os restaurantes cadastrados')

    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(21)} | {'Status'}')
    for restaurant in dicio_restaurants:
        name_restaurant = restaurant['name']
        category = restaurant['category']
        active = 'Ativado' if restaurant['active'] else 'Desativado' 
        print(f'.{name_restaurant.ljust(20)} | .{category.ljust(20)} | .{active}')

    back_to_main_menu()

def turn_status_of_restaurant():
    display_subtitle('Alternando o status do restaurante')

    restaurant_name = input('Digite o nome do restaurante: ')
    restaurant_found = False
    for restaurant in dicio_restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'O restaurante {restaurant_name} foi ativado com sucesso' if restaurant['active'] else f'O restaurante {restaurant_name} foi desativado com sucesso'
            print(message)
    if not restaurant_found:
        print('O restaurante não foi encontrado.')
            #message = f'O {restaurant_name} teve seu status alternado para {act}' 

    back_to_main_menu()

def quit_app():
    display_subtitle('Aplicação encerrada.')

def back_to_main_menu():
    input('\nPrima qualquer tecla para voltar ao menu principal')
    main()

def invalid_option():
    print('Opção invalida\n')
    back_to_main_menu()

def chosen_option():
    try: 
        chosen_option = int(input('Escholha uma opção: '))

        if chosen_option == 1:
            create_new_restaurant()
        elif chosen_option == 2:
            list_of_restaurant()
        elif chosen_option == 3:
            turn_status_of_restaurant()
        elif chosen_option == 4:
            quit_app()
        else:
            invalid_option()
    except:
        invalid_option()    

def main():
    os.system('cls')
    show_title()
    show_menu()
    chosen_option()

if __name__ == '__main__':
    main()
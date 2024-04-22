import os


restaurants = ['Boi Douro', 'Pipus']

def show_title():
    print('\t𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')

def show_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def create_new_restaurant():    
    display_subtitle('Cadastro de novos restaurantes')
    restaurant_name = input('Digite o nome do estabelecimento: ')
    restaurants.append(restaurant_name)
    print(f'O restaurante {restaurant_name} foi adicionado com sucesso!\n')
    back_to_main_menu()

def list_of_restaurant():    
    display_subtitle('Listando os restaurantes cadastrados')

    for restaurant in restaurants:
        print(f'.{restaurant}')

    back_to_main_menu()

def quit_app():
    display_subtitle('Aplicação encerrada.')

def back_to_main_menu():
    input('\nPrima qualquer tecla para voltar ao menu principal')
    main()

def display_subtitle(text):
    os.system('cls')
    print(text)
    print()

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
            print('Ativar restaurante')
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
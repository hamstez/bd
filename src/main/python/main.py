from src.database.db import create_tables, insert_sample_data
from src.repository.repository import Repository
import os

DB_FILE = "orders.db"

def main():
    if not os.path.exists(DB_FILE):
        create_tables(DB_FILE)
        insert_sample_data(DB_FILE)
    repo = Repository(DB_FILE)

    while True:
        print('\nВыберите действие:')
        print("1 - Вход как пользователь")
        print("2 - Вход как оператор")
        print("3 - Вход как курьер")
        print("0 - Выход")
        choice = input("Ваш выбор: ")
        if choice == '1':

            print("\nВыберите действие:")
            print("1 - Посмотреть все товары")
            print("2 - Посмотреть статус заказа")
            print("3 - Оформить заказ")
            print("4 - Обновить адрес")
            print("5 - Обновить контактные данные")
            print("0 - Выход")
            choice = input("Ваш выбор: ")

            if choice == '1':
                orders=repo.get_all_orders()
                for order in orders:
                    print(f'{order.id}. {order.name}. {order.price}')
            
            elif choice == "2":
                id=int(input("Введите ID товара: "))
                order=repo.get_order(id)
                print(f'{order.id}: {order.status}')

            elif choice == '3':
                id=int(input("Введите ID товара, который хотите заказать: "))
                repo.make_order(id)
                print("Готово")
            elif choice == "4":
                address=input("Введите адрес: ")
                repo.update_cleint_address(address)
                print("Готово")
            
            elif choice == '5':
                details=input('Введите контактные данные: ')
                repo.update_cleint_details(details)
                print("Готово")

        elif choice == '2':
            if input("Введите пароль: ") == '123123':
                print("\nВыберите действие:")
                print('1 - Отследить заказ')
                print("2 - Выдать курьеру задачу")
                print("3 - Узнать адрес клента")
                print("4 - Узнать контактные данные клиента")
                print("5 - Узнать контактные данные курьера")
                print("0 - Выход")
                choice=input("Ваш выбор: ")
                if choice == '1':
                    id=int(input("Введите ID товара: "))
                    order=repo.get_order(id)
                    print(f'{order.id}: {order.status}')
                
                if choice == '2':
                    id=int(input("Введите ID товара: "))
                    repo.give_courier_task(id)
                    print("\nГотово")
                

            else:
                print("\nОшибка!")


        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    repo.close()

if __name__ == "__main__":
    main()

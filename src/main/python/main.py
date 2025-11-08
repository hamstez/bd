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
                    print(f'{order.id}, {order.name}, {order.price}')
            
            elif choice == "2":
                id=int(input("Введите ID товара: "))
                order=repo.get_order(id)
                print(f'{order.id}: {order.status}')

            elif choice == '3':
                id=int(input("Введите ID товара, который хотите заказать: "))
                order = repo.get_order(id)
                if order.status!="На складе":
                    print("Нельзя заказать товар!")
                else:
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
                print("2 - Посмотреть новые заказы")
                print("3 - Выдать курьеру задачу")
                print("4 - Узнать адрес клента")
                print("5 - Узнать контактные данные клиента")
                print("6 - Узнать контактные данные курьера")
                print("0 - Выход")
                choice=input("Ваш выбор: ")
                if choice == '1':
                    id=int(input("Введите ID товара: "))
                    order=repo.get_order(id)
                    print(f'{order.id}: {order.status}')

                elif choice == '2':
                    orders=repo.get_new_order()
                    for order in orders:
                        print(f'{order.id}, {order.name}, {order.status}')

                elif choice == '3':
                    id=int(input("Введите ID товара: "))
                    repo.update_courier_task(id)
                    print("\nГотово")

                elif choice == '4':
                    cleint=repo.get_cleint()
                    print(f'\n{cleint.address}')

                elif choice == '5':
                    cleint=repo.get_cleint()
                    print(f'\n{cleint.details}')

                elif choice == '6':
                    courier=repo.get_courier()
                    print(f'\n{courier.details}')

        elif choice == '3':
            if input("Введите пароль: ") == '234234':
                print("\nВыберите действие:")
                print('1 - Отследить заказ')
                print('2 - Обновить статус заказа')
                print('3 - Посмотреть адрес клиента')
                print('4 - Посмотреть контактные данные клиента')

                print("0 - Выход")
                choice=input("Ваш выбор: ")
                if choice == '1':
                    id=int(input("Введите ID заказа: "))
                    order=repo.get_order(id)
                    print(f'{order.status}')

                elif choice == '2':
                    id = int(input("\nВведите ID заказа: "))
                    status = input("\nВведите новый статус: ")
                    repo.update_order_status(id, status)
                    print("\nГотово")

                elif choice == "3":
                    cleint=repo.get_cleint()
                    print(f'\n{cleint.address}')

                elif choice == '4':
                    cleint=repo.get_cleint()
                    print(f'\n{cleint.details}')


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

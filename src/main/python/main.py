from src.database.db import create_tables, insert_data
from src.repository.repository import Repository
import os

DB_FILE = "orders.db"

def main():
    if not os.path.exists(DB_FILE):
        create_tables(DB_FILE)
        insert_data(DB_FILE)
    repo = Repository(DB_FILE)
    create_tables(DB_FILE)
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
            print("6 - Узнать контактные данные курьера")
            print("0 - Выход")
            choice = input("Ваш выбор: ")

            if choice == '1':
                orders=repo.get_all_orders()
                for order in orders:
                    print(f'{order.id}, {order.name}, {order.price}')
            
            elif choice == "2":
                try:
                    id=int(input("Введите ID товара: "))
                except ValueError:
                    print("\nОшибка ввода!")
                    return
                if len(repo.get_all_o(id))>0:
                    order=repo.get_order(id)
                    print(f'{order.id}: {order.status}')
                else:
                    print("\nНет такого заказа!")

            elif choice == '3':
                try:
                    id=int(input("Введите ID товара, который хотите заказать: "))
                except ValueError:
                    print("\nОшибка ввода!")
                    return
                if len(repo.get_all_o(id))>0:
                    order = repo.get_order(id)

                    if order.status!="На складе":
                        print("Нельзя заказать товар!")

                    else:
                        repo.make_order(id)
                        print("\nГотово")
                else:
                    print("Нет такого товара!")

            elif choice == "4":
                address=input("Введите адрес: ")
                repo.update_client_address(address)
                print("Готово")
            
            elif choice == '5':
                details=input('Введите контактные данные: ')
                repo.update_client_details(details)
                print("Готово")

            elif choice == '6':
                try:
                    id_cour=int(input("\nВведите ID курьера: "))
                except ValueError:
                    print("\nОшибка ввода!")
                    return
                if len(repo.get_all_c(id_cour))>0:
                    courier=repo.get_courier(id_cour)
                    print(f"{courier.id}, {courier.details}")
                else:
                    print("\nНет такого курьера!")

            else:
                print("\nНеверный выбор!")

        elif choice == '2':
            if input("Введите пароль: ") == '123123':
                print("\nВыберите действие:")
                print('1 - Отследить заказ')
                print("2 - Посмотреть новые заказы для курьера")
                print("3 - Выдать курьеру задачу")
                print("4 - Узнать адрес клента")
                print("5 - Узнать контактные данные клиента")
                print("6 - Узнать контактные данные курьера")
                print("7 - Посмотреть всех курьеров")
                print('8 - Изменить статус курьера')
                print("0 - Выход")
                choice=input("Ваш выбор: ")
                if choice == '1':
                    try:
                        id=int(input("Введите ID товара: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    if len(repo.get_all_o(id))>0:
                        order=repo.get_order(id)
                        print(f'{order.id}: {order.status}')
                    else:
                        print("\nНет такого заказа!")

                elif choice == '2':
                    try:
                        id_cour=int(input("\nВведите ID курьера: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    if len(repo.get_all_c(id_cour))>0:
                        orders=repo.get_new_order(id_cour)
                        for order in orders:
                            print(f'{order.id}, {order.name}, {order.status}')
                    else:
                        print("\nНет такого курьера!")

                elif choice == '3':
                    try:
                        id1=int(input("Введите ID товара: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    try:
                        id2=int(input("\nВведите ID курьера: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    if len(repo.get_all_c(id2))>0 and len(repo.get_all_o(id1))>0:
                        repo.update_courier_task(id1,id2)
                        print("\nГотово")
                    else:
                        print("\nНет такого товара или такого курьера!")

                elif choice == '4':
                    client=repo.get_client()
                    print(f'\n{client.address}')

                elif choice == '5':
                    client=repo.get_client()
                    print(f'\n{client.details}')

                elif choice == '6':
                    try:
                        id=int(input("\nВведите ID курьера: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    courier=repo.get_courier(id)
                    print(f'\n{courier.details}')

                elif choice == '7':
                    couriers=repo.get_all_couriers()
                    for courier in couriers:
                        print(f'{courier.id}, {courier.status}')

                elif choice == "8":
                    status=input("\nВведите новый статус курьера: ")
                    try:
                        id=int(input("\nВведите ID курьера: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    if len(repo.get_all_c(id))>0:
                        repo.update_courier_status(status, id)
                    else:
                        print("\nНет такого курьера!")
                    print('\nГотово')

                else:
                    print("\nНеверный выбор!")

            else:
                print("\nНеверный пароль!")

        elif choice == '3':
            ok=False
            new_id=0
            while not ok:
                try:
                    cour_id=int(input("Введите ID курьера: \n"))
                except ValueError:
                    print("\nОшибка ввода!")
                    return
                try:
                    cour_pass=int(input("Введите пароль курьера: \n"))
                except ValueError:
                    print("\nОшибка ввода!")
                    return
                if len(repo.get_all_c(cour_id))>0 and (cour_pass==repo.get_courier(cour_id).password):
                    new_id=cour_id
                    ok=True
                else:
                    print("\nНет такого курьера или неверный пароль")


            print("\nВыберите действие:")
            print('1 - Отследить заказ')
            print("2 - Посмотреть новые заказы")
            print('3 - Обновить статус заказа')
            print('4 - Посмотреть адрес клиента')
            print('5 - Посмотреть контактные данные клиента')

            print("0 - Выход")
            choice=input("Ваш выбор: ")
            if choice == '1':
                try:
                    id=int(input("Введите ID заказа: "))
                except ValueError:
                    print("\nОшибка ввода!")
                    return
                if len(repo.get_all_o(id))>0:
                    order=repo.get_order(id)
                    print(f'{order.status}')
                else:
                    print("\nНет такого заказа!")

            elif choice == "2":
                    orders=repo.get_new_order(new_id)
                    for order in orders:
                        print(f'{order.id}, {order.name}, {order.status}')

            elif choice == '3':
                    try:
                        id = int(input("\nВведите ID заказа: "))
                    except ValueError:
                        print("\nОшибка ввода!")
                        return
                    status = input("\nВведите новый статус: ")
                    if len(repo.get_all_o(id))>0:
                        repo.update_order_status(id, status)
                        print("\nГотово")
                    else:
                        print("\nНет такого заказа!")

            elif choice == "4":
                    client=repo.get_client()
                    print(f'\n{client.address}')

            elif choice == '5':
                    client=repo.get_client()
                    print(f'\n{client.details}')

            else:
                print("\nНеверный выбор!")

        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
    try:
        os.makedirs('out')
    except FileExistsError:
        pass

    repo.make_json()
    repo.make_csv()
    repo.make_xml()
    repo.make_yaml()
    repo.close()
if __name__ == "__main__":
    main()
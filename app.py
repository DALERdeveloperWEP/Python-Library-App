"""
Kutubxona Boshqaruv Tizimi (Library Management System)
CLI ilova - kitoblarni qo'shish, ko'rish, o'chirish, yangilash va qidirish
"""


import sys

from rich.console import Console
from rich.table import Table

console = Console()

def manu():
    menu = Table(title="Kutubxona Boshqaruv Tizimi", title_style="bold green")
    menu.add_column("№", style="cyan", justify="center")
    menu.add_column("Amal", style="yellow")

    menu.add_row("1", "Kitob qo'shish")
    menu.add_row("2", "Kitoblarni ko'rish")
    menu.add_row("3", "Kitobni o'chirish")
    menu.add_row("4", "Kitobni yangilash")
    menu.add_row("5", "Status o'zgartirish")
    menu.add_row("6", "Qidirish")
    menu.add_row("7", "Filterlash")
    menu.add_row("8", "Chiqish")

    console.print(menu)

def add_book(library: list[list[str, str, int, bool]]) -> None:
    """
    Foydalanuvchidan kitob nomi, muallif va yilni qabul qiladi.
    Ularni tekshiradi va listga yangi kitob qo'shadi (status default = False).
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """
    # [title – sarlavha / nom, author – muallif, year – yil, status – holat / maqom]
    get_title = input("Enter book Title: ")
    get_author = input("Enter book author: ")
    get_year = input("Enter book year: ")
    library.append([get_title,get_author,get_year,False])
    


def show_books(library: list[list[str, str, int, bool]]) -> None:
    """
    Kutubxonadagi barcha kitoblarni jadval ko'rinishida chiqaradi.
    Agar library bo'sh bo'lsa, mos xabar beradi.
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """
    # [title – sarlavha / nom, author – muallif, year – yil, status – holat / maqom]
    table = Table(title="Library",title_style="bold green on blue")
    table.add_column("№", style="blue")
    table.add_column("Title",style="white")
    table.add_column("author",style="yellow")
    table.add_column("Years", style="green")
    table.add_column("Status")

    for index, lib in enumerate(library,start=1):
        if lib[3]:
            table.add_row(str(index),lib[0],lib[1],str(lib[2]),"O'qilgan")
        else:
            table.add_row(str(index),lib[0],lib[1],str(lib[2]),"O'qilmagan")
    
    console.print(table)


def delete_book(library: list[list[str, str, int, bool]]) -> None:
    """
    Indeks bo'yicha kitobni o'chiradi.
    Avval kitoblar ro'yxati ko'rsatiladi, so'ng tanlangan indeks tekshiriladi va o'chiriladi.
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """
    show_books(library)
    if library:
        get_delete_book_num = int(input("Enter delete book number: "))
        if get_delete_book_num > 0 and get_delete_book_num <= len(library):
            library.pop(get_delete_book_num - 1)
            show_books(library)
        else:print("Siz notogri kitob raqamini tanladingiz!")
    else:print("Sizda kitob Mavjud emas!")


def update_book(library: list[list[str, str, int, bool]]) -> None:
    """
    Indeks bo'yicha tanlangan kitobning title va author qiymatlarini yangilaydi.
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """
    if library:
        get_edit_book_num = int(input("Enter edit book number: "))
        if get_edit_book_num > 0 and get_edit_book_num <= len(library):
            get_new_title = input("Enter new title: ")
            get_new_author = input("Enter new author: ")
            library[get_edit_book_num - 1][0] = get_new_title
            library[get_edit_book_num - 1][1] = get_new_author
            show_books(library)
        else:print("Siz notogri kitob raqamini tanladingiz!")
    else:print("Sizda kitob Mavjud emas!")


def change_status(library: list[list[str, str, int, bool]]) -> None:
    """
    Indeks bo'yicha tanlangan kitobning statusini (o'qilgan/o'qilmagan) almashtiradi.
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """
    show_books(library)
    if library:
        get_status_book_num = int(input("Enter status book number: "))
        if get_status_book_num > 0 and get_status_book_num <= len(library):
            library[get_status_book_num - 1][3] = not library[get_status_book_num - 1][3]
            show_books(library)
        else:print("Siz notogri kitob raqamini tanladingiz!",len(library))
    else:print("Sizda kitob Mavjud emas!")


def search_books(library: list[list[str, str, int, bool]]) -> None:
    """
    Foydalanuvchidan qidirish parametri olinadi (nom, muallif yoki yil).
    Mos keladigan kitoblarni chiqaradi.
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """

    search_table = Table(title="Qidirov natijalari",title_style="bold green")
    search_table.add_column("№", style="blue")
    search_table.add_column("Title",style="white")
    search_table.add_column("author",style="yellow")
    search_table.add_column("Years", style="green")
    search_table.add_column("Status")

    search = input("Qidiruv (nom/muallif/yil): ").lower()

    isSearch = False

    for index, lib in enumerate(library, start=1):
        if  search in lib[0].lower() or search in lib[1].lower() or search in str(lib[2]) :
            isSearch = True
            if lib[3]:
                search_table.add_row(str(index),lib[0],lib[1],str(lib[2]),"O'qilgan")
            else:
                search_table.add_row(str(index),lib[0],lib[1],str(lib[2]),"O'qilmagan")

    if isSearch:
        console.print(search_table)
    else:
        console.print("Xech narsa topilmadi", style="red")



def filter_books(library: list[list[str, str, int, bool]]) -> None:
    """
    Status bo'yicha filterlash: faqat o'qilgan yoki faqat o'qilmagan kitoblarni chiqaradi.
    
    Args:
        library: Kitoblar ro'yxati - har bir kitob [title, author, year, status] formatida
    """
    oqigan_kitob_table = Table(title="O'qilgan Kitoblar",title_style="bold green on green")
    oqigan_kitob_table.add_column("№", style="blue")
    oqigan_kitob_table.add_column("Title",style="white")
    oqigan_kitob_table.add_column("author",style="yellow")
    oqigan_kitob_table.add_column("Years", style="green")
    oqigan_kitob_table.add_column("Status")

    oqimagan_kitob_table = Table(title="O'qilmagan Kitoblar",title_style="bold green on yellow")
    oqimagan_kitob_table.add_column("№", style="blue")
    oqimagan_kitob_table.add_column("Title",style="white")
    oqimagan_kitob_table.add_column("author",style="yellow")
    oqimagan_kitob_table.add_column("Years", style="green")
    oqimagan_kitob_table.add_column("Status")

    for index, lib in enumerate(library,start=1):
        if lib[3]:
            oqigan_kitob_table.add_row(str(index),lib[0],lib[1],str(lib[2]),"O'qilgan")
        else:
            oqimagan_kitob_table.add_row(str(index),lib[0],lib[1],str(lib[2]),"O'qilmagan")
    
    console.print(oqigan_kitob_table)
    console.print(oqimagan_kitob_table)


def main():
    """
    Asosiy funksiya - menyuni ko'rsatadi va foydalanuvchi tanloviga qarab 
    yuqoridagi funksiyalarni chaqiradi.
    """
    library: list[list[str, str, int, bool]] = []  # [title – sarlavha / nom, author – muallif, year – yil, status – holat / maqom]

    manu()
    while True:
        choice = input("> ")
        if choice == '1':add_book(library)
        elif choice == '2':show_books(library)
        elif choice == '3':delete_book(library)
        elif choice == '4':update_book(library)
        elif choice == '5':change_status(library)
        elif choice == '6':search_books(library)
        elif choice == '7':filter_books(library)
        elif choice == '8':sys.exit()
        else:manu(),console.print("bunday menyu mavjud emas!", style="red")

main()
